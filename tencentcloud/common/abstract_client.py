# -*- coding: utf-8 -*-
#
# Copyright 2017-2021 Tencent Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import copy
from datetime import datetime
import hashlib
import json
import random
import sys
import time
import uuid
import warnings
import logging
import logging.handlers

try:
    from urllib.parse import urlencode
    from urllib.parse import urlparse
except ImportError:
    from urllib import urlencode
    from urlparse import urlparse

import tencentcloud
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.exception import TencentCloudSDKException as SDKError
from tencentcloud.common.http.request import ApiRequest, ResponsePrettyFormatter
from tencentcloud.common.http.request import RequestInternal
from tencentcloud.common.profile.client_profile import ClientProfile, RegionBreakerProfile
from tencentcloud.common.sign import Sign
from tencentcloud.common.circuit_breaker import CircuitBreaker
from tencentcloud.common.retry import NoopRetryer

warnings.filterwarnings("ignore", module="tencentcloud", category=UserWarning)

_json_content = 'application/json'
_multipart_content = 'multipart/form-data'
_form_urlencoded_content = 'application/x-www-form-urlencoded'
_octet_stream = "application/octet-stream"


class EmptyHandler(logging.Handler):
    def emit(self, message):
        pass


LOGGER_NAME = "tencentcloud_sdk_common"
logger = logging.getLogger(LOGGER_NAME)
logger.addHandler(EmptyHandler())


class AbstractClient(object):
    _requestPath = '/'
    _params = {}
    _apiVersion = ''
    _endpoint = ''
    _service = ''
    _sdkVersion = 'SDK_PYTHON_%s' % tencentcloud.__version__
    _default_content_type = _form_urlencoded_content
    FMT = '%(asctime)s %(process)d %(filename)s L%(lineno)s %(levelname)s %(message)s'

    def __init__(self, credential, region, profile=None):
        self.credential = credential
        self.region = region
        self.profile = ClientProfile() if profile is None else profile
        is_http = True if self.profile.httpProfile.scheme == "http" else False
        self.request = ApiRequest(self._get_endpoint(),
                                  req_timeout=self.profile.httpProfile.reqTimeout,
                                  proxy=self.profile.httpProfile.proxy,
                                  is_http=is_http,
                                  certification=self.profile.httpProfile.certification,
                                  pre_conn_pool_size=self.profile.httpProfile.pre_conn_pool_size)
        if self.profile.httpProfile.keepAlive:
            self.request.set_keep_alive()
        self.circuit_breaker = None
        if not self.profile.disable_region_breaker:
            if self.profile.region_breaker_profile is None:
                self.profile.region_breaker_profile = RegionBreakerProfile()
            self.circuit_breaker = CircuitBreaker(self.profile.region_breaker_profile)
        if self.profile.request_client:
            self.request_client = self._sdkVersion + "; " + self.profile.request_client
        else:
            self.request_client = self._sdkVersion

    def _fix_params(self, params):
        if not isinstance(params, (dict,)):
            return params
        return self._format_params(None, params)

    def _format_params(self, prefix, params):
        d = {}
        if params is None:
            return d

        if not isinstance(params, (tuple, list, dict)):
            d[prefix] = params
            return d

        if isinstance(params, (list, tuple)):
            for idx, item in enumerate(params):
                if prefix:
                    key = "{0}.{1}".format(prefix, idx)
                else:
                    key = "{0}".format(idx)
                d.update(self._format_params(key, item))
            return d

        if isinstance(params, dict):
            for k, v in params.items():
                if prefix:
                    key = '{0}.{1}'.format(prefix, k)
                else:
                    key = '{0}'.format(k)
                d.update(self._format_params(key, v))
            return d

        raise TencentCloudSDKException("ClientParamsError", "some params type error")

    def _build_req_inter(self, action, params, req_inter, options=None):
        options = options or {}
        if options.get('SkipSign'):
            self._build_req_without_signature(action, params, req_inter, options)
        elif self.profile.signMethod == "TC3-HMAC-SHA256" or options.get("IsMultipart") is True:
            self._build_req_with_tc3_signature(action, params, req_inter, options)
        elif self.profile.signMethod in ("HmacSHA1", "HmacSHA256"):
            self._build_req_with_old_signature(action, params, req_inter, options)
        else:
            raise TencentCloudSDKException("ClientError", "Invalid signature method.")

    def _build_req_with_old_signature(self, action, params, req, options):
        params = copy.deepcopy(self._fix_params(params))
        params['Action'] = action[0].upper() + action[1:]
        params['RequestClient'] = self.request_client
        params['Nonce'] = random.randint(1, sys.maxsize)
        params['Timestamp'] = int(time.time())
        params['Version'] = self._apiVersion

        if self.region:
            params['Region'] = self.region

        if self.credential.token:
            params['Token'] = self.credential.token

        if self.credential.secret_id:
            params['SecretId'] = self.credential.secret_id

        if self.profile.signMethod:
            params['SignatureMethod'] = self.profile.signMethod

        if self.profile.language:
            params['Language'] = self.profile.language

        signInParam = self._format_sign_string(params, options)
        params['Signature'] = Sign.sign(str(self.credential.secret_key),
                                        str(signInParam),
                                        str(self.profile.signMethod))

        req.data = urlencode(params)
        req.header["Content-Type"] = "application/x-www-form-urlencoded"

    def _build_req_with_tc3_signature(self, action, params, req, options=None):
        content_type = self._default_content_type
        if req.method == 'GET':
            content_type = _form_urlencoded_content
        elif req.method == 'POST':
            content_type = _json_content
        options = options or {}
        if options.get("IsMultipart"):
            content_type = _multipart_content
        if options.get("IsOctetStream"):
            content_type = _octet_stream
        req.header["Content-Type"] = content_type

        if req.method == "GET" and content_type == _multipart_content:
            raise SDKError("ClientError",
                           "Invalid request method GET for multipart.")

        endpoint = self._get_endpoint(options=options)
        timestamp = int(time.time())
        req.header["Host"] = endpoint
        req.header["X-TC-Action"] = action[0].upper() + action[1:]
        req.header["X-TC-RequestClient"] = self.request_client
        req.header["X-TC-Timestamp"] = str(timestamp)
        req.header["X-TC-Version"] = self._apiVersion
        if self.profile.unsignedPayload is True:
            req.header["X-TC-Content-SHA256"] = "UNSIGNED-PAYLOAD"
        if self.region:
            req.header['X-TC-Region'] = self.region
        if self.credential.token:
            req.header['X-TC-Token'] = self.credential.token
        if self.profile.language:
            req.header['X-TC-Language'] = self.profile.language

        if req.method == 'GET':
            params = copy.deepcopy(self._fix_params(params))
            req.data = urlencode(params)
        elif content_type == _json_content:
            req.data = json.dumps(params)
        elif content_type == _multipart_content:
            boundary = uuid.uuid4().hex
            req.header["Content-Type"] = content_type + "; boundary=" + boundary
            req.data = self._get_multipart_body(params, boundary, options)

        service = self._service
        date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')
        signature = self._get_tc3_signature(params, req, date, service, options)

        auth = "TC3-HMAC-SHA256 Credential=%s/%s/%s/tc3_request, SignedHeaders=content-type;host, Signature=%s" % (
            self.credential.secret_id, date, service, signature)
        req.header["Authorization"] = auth

    def _get_tc3_signature(self, params, req, date, service, options=None):
        options = options or {}
        canonical_uri = req.uri
        canonical_querystring = ""
        payload = req.data

        if req.method == 'GET':
            canonical_querystring = req.data
            payload = ""

        if req.header.get("X-TC-Content-SHA256") == "UNSIGNED-PAYLOAD":
            payload = "UNSIGNED-PAYLOAD"

        if sys.version_info[0] == 3 and isinstance(payload, type("")):
            payload = payload.encode("utf8")

        payload_hash = hashlib.sha256(payload).hexdigest()

        canonical_headers = 'content-type:%s\nhost:%s\n' % (
            req.header["Content-Type"], req.header["Host"])
        signed_headers = 'content-type;host'
        canonical_request = '%s\n%s\n%s\n%s\n%s\n%s' % (req.method,
                                                        canonical_uri,
                                                        canonical_querystring,
                                                        canonical_headers,
                                                        signed_headers,
                                                        payload_hash)

        algorithm = 'TC3-HMAC-SHA256'
        credential_scope = date + '/' + service + '/tc3_request'
        if sys.version_info[0] == 3:
            canonical_request = canonical_request.encode("utf8")
        digest = hashlib.sha256(canonical_request).hexdigest()
        string2sign = '%s\n%s\n%s\n%s' % (algorithm,
                                          req.header["X-TC-Timestamp"],
                                          credential_scope,
                                          digest)

        return Sign.sign_tc3(self.credential.secret_key, date, service, string2sign)

    def _build_req_without_signature(self, action, params, req, options=None):
        content_type = self._default_content_type
        if req.method == 'GET':
            content_type = _form_urlencoded_content
        elif req.method == 'POST':
            content_type = _json_content
        options = options or {}
        if options.get("IsMultipart"):
            content_type = _multipart_content
        if options.get("IsOctetStream"):
            content_type = _octet_stream
        req.header["Content-Type"] = content_type

        if req.method == "GET" and content_type == _multipart_content:
            raise SDKError("ClientError",
                           "Invalid request method GET for multipart.")

        endpoint = self._get_endpoint(options=options)
        timestamp = int(time.time())
        req.header["Host"] = endpoint
        req.header["X-TC-Action"] = action[0].upper() + action[1:]
        req.header["X-TC-RequestClient"] = self.request_client
        req.header["X-TC-Timestamp"] = str(timestamp)
        req.header["X-TC-Version"] = self._apiVersion
        if self.profile.unsignedPayload is True:
            req.header["X-TC-Content-SHA256"] = "UNSIGNED-PAYLOAD"
        if self.region:
            req.header['X-TC-Region'] = self.region
        if self.profile.language:
            req.header['X-TC-Language'] = self.profile.language

        if req.method == 'GET':
            params = copy.deepcopy(self._fix_params(params))
            req.data = urlencode(params)
        elif content_type == _json_content:
            req.data = json.dumps(params)
        elif content_type == _multipart_content:
            boundary = uuid.uuid4().hex
            req.header["Content-Type"] = content_type + "; boundary=" + boundary
            req.data = self._get_multipart_body(params, boundary, options)

        req.header["Authorization"] = "SKIP"

    # it must return bytes instead of string
    def _get_multipart_body(self, params, boundary, options=None):
        if options is None:
            options = {}
        # boundary and params key will never contain unicode characters
        boundary = boundary.encode()
        binparas = options.get("BinaryParams", [])
        body = b''
        for k, v in params.items():
            kbytes = k.encode()
            body += b'--%s\r\n' % boundary
            body += b'Content-Disposition: form-data; name="%s"' % kbytes
            if k in binparas:
                body += b'; filename="%s"\r\n' % kbytes
            else:
                body += b"\r\n"
                if isinstance(v, list) or isinstance(v, dict):
                    v = json.dumps(v)
                    body += b'Content-Type: application/json\r\n'
            if sys.version_info[0] == 3 and isinstance(v, type("")):
                v = v.encode()
            body += b'\r\n%s\r\n' % v
        if body != b'':
            body += b'--%s--\r\n' % boundary
        return body

    def _check_status(self, resp_inter):
        if resp_inter.status_code != 200:
            logger.debug("GetResponse: %s", ResponsePrettyFormatter(resp_inter))
            raise TencentCloudSDKException("ServerNetworkError", resp_inter.content)

    def _format_sign_string(self, params, options=None):
        formatParam = {}
        for k in params:
            formatParam[k.replace('_', '.')] = params[k]
        strParam = '&'.join('%s=%s' % (k, formatParam[k]) for k in sorted(formatParam))
        msg = '%s%s%s?%s' % (
            self.profile.httpProfile.reqMethod, self._get_endpoint(options=options), self._requestPath, strParam)
        return msg

    def _get_service_domain(self):
        rootDomain = self.profile.httpProfile.rootDomain
        return self._service + "." + rootDomain

    def _get_endpoint(self, options=None):
        endpoint = self.profile.httpProfile.endpoint
        if not endpoint and options:
            endpoint = urlparse(options.get("Endpoint", "")).hostname
        if endpoint is None:
            endpoint = self._get_service_domain()
        return endpoint

    def _check_error(self, resp):
        ct = resp.headers.get('Content-Type')
        if ct not in ('text/plain', _json_content):
            return

        data = json.loads(resp.content)
        if "Error" in data["Response"]:
            code = data["Response"]["Error"]["Code"]
            message = data["Response"]["Error"]["Message"]
            reqid = data["Response"]["RequestId"]
            logger.debug("GetResponse: %s", ResponsePrettyFormatter(resp))
            raise TencentCloudSDKException(code, message, reqid)
        if "DeprecatedWarning" in data["Response"]:
            import warnings
            warnings.filterwarnings("default")
            warnings.warn("This action is deprecated, detail: %s" % data["Response"]["DeprecatedWarning"],
                          DeprecationWarning)

    @staticmethod
    def _process_response_sse(resp):
        logger.debug("GetResponse: %s", ResponsePrettyFormatter(resp, format_body=False))
        e = {}

        for line in resp.iter_lines():
            if not line:
                yield e
                e = {}
                continue

            logger.debug("GetResponse: %s", line)
            line = line.decode('utf-8')

            # comment
            if line[0] == ':':
                continue

            colon_idx = line.find(':')
            key = line[:colon_idx]
            val = line[colon_idx + 1:]
            # If value starts with a U+0020 SPACE character, remove it from value.
            if val and val[0] == " ":
                val = val[1:]
            if key == 'data':
                # The spec allows for multiple data fields per event, concatenated them with "\n".
                if 'data' not in e:
                    e['data'] = val
                else:
                    e['data'] += '\n' + val
            elif key in ('event', 'id'):
                e[key] = val
            elif key == 'retry':
                e[key] = int(val)

    @staticmethod
    def _process_response_json(resp, resp_type):
        resp_obj = json.loads(resp.content)["Response"]
        model = resp_type()
        model._deserialize(resp_obj)
        return model

    def _call(self, action, params, options=None, headers=None):
        if headers is None:
            headers = {}
        if not isinstance(headers, dict):
            raise TencentCloudSDKException("ClientError", "headers must be a dict.")
        if "x-tc-traceid" not in {k.lower() for k in headers.keys()}:
            headers["X-TC-TraceId"] = str(uuid.uuid4())
        if not self.profile.disable_region_breaker:
            return self._call_with_region_breaker(action, params, options, headers)
        req = RequestInternal(self._get_endpoint(options=options),
                              self.profile.httpProfile.reqMethod,
                              self._requestPath,
                              header=headers)
        self._build_req_inter(action, params, req, options)

        if self.profile.httpProfile.apigw_endpoint:
            req.host = self.profile.httpProfile.apigw_endpoint
            req.header["Host"] = req.host
        return self.request.send_request(req)

    def call(self, action, params, options=None, headers=None):

        def _call_once():
            resp = self._call(action, params, options, headers)
            self._check_status(resp)
            self._check_error(resp)
            logger.debug("GetResponse: %s", ResponsePrettyFormatter(resp))
            return resp

        retryer = self.profile.retryer or NoopRetryer()
        return retryer.send_request(_call_once).content

    def _call_with_region_breaker(self, action, params, options=None, headers=None):
        endpoint = self._get_endpoint(options=options)
        generation, need_break = self.circuit_breaker.before_requests()
        if need_break:
            endpoint = self._service + "." + self.profile.region_breaker_profile.backup_endpoint
        req = RequestInternal(endpoint,
                              self.profile.httpProfile.reqMethod,
                              self._requestPath,
                              header=headers)
        self._build_req_inter(action, params, req, options)
        resp = None
        try:
            resp = self.request.send_request(req)
            self.circuit_breaker.after_requests(generation, True)
            return resp
        except TencentCloudSDKException as e:
            if resp and "RequestId" in resp.content and e.code != "InternalError":
                self.circuit_breaker.after_requests(generation, True)
            else:
                self.circuit_breaker.after_requests(generation, False)

    def call_with_region_breaker(self, action, params, options=None, headers=None):
        resp = self._call_with_region_breaker(action, params, options, headers)
        self._check_status(resp)
        self._check_error(resp)
        return resp.content

    def call_octet_stream(self, action, headers, body, options=None):
        """Invoke API with application/ocet-stream content-type.

        Note:
        1. only specific API can be invoked in such manner.
        2. only TC3-HMAC-SHA256 signature method can be specified.
        3. only POST request method can be specified

        :param action: Specific API action name.
        :type action: str
        :param headers: Header parameters for this API.
        :type headers: dict
        :param body: Bytes of requested body
        :type body: bytes
        """
        if self.profile.signMethod != "TC3-HMAC-SHA256":
            raise SDKError("ClientError", "Invalid signature method.")
        if self.profile.httpProfile.reqMethod != "POST":
            raise SDKError("ClientError", "Invalid request method.")

        if not options:
            options = {}
        req = RequestInternal(self._get_endpoint(options=options),
                              self.profile.httpProfile.reqMethod,
                              self._requestPath,
                              header=headers)
        req.data = body
        options["IsOctetStream"] = True
        self._build_req_inter(action, None, req, options)

        resp = self.request.send_request(req)
        self._check_status(resp)
        self._check_error(resp)
        return json.loads(resp.content)

    def call_json(self, action, params, headers=None, options=None):
        """Call api with json object and return with json object.

        :param action: api name e.g. ``DescribeInstances``
        :type action: str
        :param params: Request parameters of this action
        :type params: dict
        :param headers: Request headers, like {"X-TC-TraceId": "ffe0c072-8a5d-4e17-8887-a8a60252abca"}
        :type headers: dict
        :param options: Request options, like {"SkipSign": False, "IsMultipart": False, "IsOctetStream": False, "BinaryParams": []}
        :type options: dict
        """

        def _call_once():
            resp = self._call(action, params, options, headers)
            self._check_status(resp)
            self._check_error(resp)
            logger.debug("GetResponse: %s", ResponsePrettyFormatter(resp))
            return resp

        retryer = self.profile.retryer or NoopRetryer()
        return json.loads(retryer.send_request(_call_once).content)

    def call_sse(self, action, params, headers=None, options=None):
        """Call api with json object and return with sse event.

        :param action: api name e.g. ``ChatCompletions``
        :type action: str
        :param params: Request parameters of this action
        :type params: dict
        :param headers: Request headers, like {"X-TC-TraceId": "ffe0c072-8a5d-4e17-8887-a8a60252abca"}
        :type headers: dict
        :param options: Request options, like {"SkipSign": False, "IsMultipart": False, "IsOctetStream": False, "BinaryParams": []}
        :type options: dict
        """

        def _call_once():
            resp = self._call(action, params, options, headers)
            self._check_status(resp)
            self._check_error(resp)
            return resp

        retryer = self.profile.retryer or NoopRetryer()
        return self._process_response_sse(retryer.send_request(_call_once))

    def _call_and_deserialize(self, action, params, resp_type, headers=None, options=None):
        def _call_once():
            resp = self._call(action, params, options, headers)
            self._check_status(resp)
            self._check_error(resp)
            return resp

        retryer = self.profile.retryer or NoopRetryer()
        return self._process_response(retryer.send_request(_call_once), resp_type)

    def _process_response(self, resp, resp_type):
        if resp.headers.get('Content-Type') == "text/event-stream":
            logger.debug("GetResponse: %s", ResponsePrettyFormatter(resp, format_body=False))
            return self._process_response_sse(resp)

        logger.debug("GetResponse: %s", ResponsePrettyFormatter(resp))
        return self._process_response_json(resp, resp_type)

    def set_stream_logger(self, stream=None, level=logging.DEBUG, log_format=None):
        """Add a stream handler

        :param stream: e.g. ``sys.stdout`` ``sys.stdin`` ``sys.stderr``
        :type stream: IO[str]
        :param level: Logging level, e.g. ``logging.INFO``
        :type level: int
        :param log_format: Log message format
        :type log_format: str
        """
        log = logging.getLogger(LOGGER_NAME)
        log.setLevel(level)
        sh = logging.StreamHandler(stream)
        sh.setLevel(level)
        if log_format is None:
            log_format = self.FMT
        formatter = logging.Formatter(log_format)
        sh.setFormatter(formatter)
        log.addHandler(sh)

    def set_file_logger(self, file_path, level=logging.DEBUG, log_format=None):
        """Add a file handler

        :param file_path: path of log file
        :type file_path: str
        :param level: Logging level, e.g. ``logging.INFO``
        :type level: int
        :param log_format: Log message format
        :type log_format: str
        """
        log = logging.getLogger(LOGGER_NAME)
        log.setLevel(level)
        mb = 1024 * 1024
        fh = logging.handlers.RotatingFileHandler(file_path, maxBytes=512 * mb, backupCount=10)
        fh.setLevel(level)
        if log_format is None:
            log_format = self.FMT
        formatter = logging.Formatter(log_format)
        fh.setFormatter(formatter)
        log.addHandler(fh)

    def set_default_logger(self):
        """Set default log handler"""
        log = logging.getLogger(LOGGER_NAME)
        log.handlers = []
        logger.addHandler(EmptyHandler())
