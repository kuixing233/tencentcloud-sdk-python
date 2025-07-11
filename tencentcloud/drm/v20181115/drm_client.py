# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.drm.v20181115 import models


class DrmClient(AbstractClient):
    _apiVersion = '2018-11-15'
    _endpoint = 'drm.tencentcloudapi.com'
    _service = 'drm'


    def AddFairPlayPem(self, request):
        """本接口用来设置fairplay方案所需的私钥、私钥密钥、ask等信息。
        如需使用fairplay方案，请务必先设置私钥。

        :param request: Request instance for AddFairPlayPem.
        :type request: :class:`tencentcloud.drm.v20181115.models.AddFairPlayPemRequest`
        :rtype: :class:`tencentcloud.drm.v20181115.models.AddFairPlayPemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddFairPlayPem", params, headers=headers)
            response = json.loads(body)
            model = models.AddFairPlayPemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEncryptKeys(self, request):
        """该接口用来设置加密的密钥。注意，同一个content id，只能设置一次！

        :param request: Request instance for CreateEncryptKeys.
        :type request: :class:`tencentcloud.drm.v20181115.models.CreateEncryptKeysRequest`
        :rtype: :class:`tencentcloud.drm.v20181115.models.CreateEncryptKeysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEncryptKeys", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEncryptKeysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLicense(self, request):
        """本接口用来生成DRM方案对应的播放许可证，开发者需提供DRM方案类型、内容类型参数，后台将生成许可证后返回许可证数据
        开发者需要转发终端设备发出的许可证请求信息。

        :param request: Request instance for CreateLicense.
        :type request: :class:`tencentcloud.drm.v20181115.models.CreateLicenseRequest`
        :rtype: :class:`tencentcloud.drm.v20181115.models.CreateLicenseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLicense", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLicenseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFairPlayPem(self, request):
        """本接口用来删除fairplay方案的私钥、ask等信息
        注：高风险操作，删除后，您将无法使用腾讯云DRM提供的fairplay服务。
        由于缓存，删除操作需要约半小时生效

        :param request: Request instance for DeleteFairPlayPem.
        :type request: :class:`tencentcloud.drm.v20181115.models.DeleteFairPlayPemRequest`
        :rtype: :class:`tencentcloud.drm.v20181115.models.DeleteFairPlayPemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFairPlayPem", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFairPlayPemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllKeys(self, request):
        """本接口用来查询指定DRM类型、ContentType的所有加密密钥

        :param request: Request instance for DescribeAllKeys.
        :type request: :class:`tencentcloud.drm.v20181115.models.DescribeAllKeysRequest`
        :rtype: :class:`tencentcloud.drm.v20181115.models.DescribeAllKeysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllKeys", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllKeysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDRMLicense(self, request):
        """开发者需要指定使用的DRM类型取值 NORMALAES、和需要加密的Track类型取值 SD,ContentType取值 LiveVideo

        :param request: Request instance for DescribeDRMLicense.
        :type request: :class:`tencentcloud.drm.v20181115.models.DescribeDRMLicenseRequest`
        :rtype: :class:`tencentcloud.drm.v20181115.models.DescribeDRMLicenseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDRMLicense", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDRMLicenseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFairPlayPem(self, request):
        """该接口用来查询设置的FairPlay私钥校验信息。可用该接口校验设置的私钥与本身的私钥是否一致。

        :param request: Request instance for DescribeFairPlayPem.
        :type request: :class:`tencentcloud.drm.v20181115.models.DescribeFairPlayPemRequest`
        :rtype: :class:`tencentcloud.drm.v20181115.models.DescribeFairPlayPemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFairPlayPem", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFairPlayPemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKeys(self, request):
        """开发者需要指定使用的DRM类型、和需要加密的Track类型，后台返回加密使用的密钥
        如果加密使用的ContentID没有关联的密钥信息，后台会自动生成新的密钥返回

        :param request: Request instance for DescribeKeys.
        :type request: :class:`tencentcloud.drm.v20181115.models.DescribeKeysRequest`
        :rtype: :class:`tencentcloud.drm.v20181115.models.DescribeKeysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKeys", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKeysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GenerateTDRMKey(self, request):
        """开发者需要指定使用的DRM类型取值 NORMALAES、和需要加密的Track类型取值 SD,ContentType取值 LiveVideo

        :param request: Request instance for GenerateTDRMKey.
        :type request: :class:`tencentcloud.drm.v20181115.models.GenerateTDRMKeyRequest`
        :rtype: :class:`tencentcloud.drm.v20181115.models.GenerateTDRMKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateTDRMKey", params, headers=headers)
            response = json.loads(body)
            model = models.GenerateTDRMKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFairPlayPem(self, request):
        """本接口用来设置fairplay方案所需的私钥、私钥密钥、ask等信息。
        如需使用fairplay方案，请务必先设置私钥。

        :param request: Request instance for ModifyFairPlayPem.
        :type request: :class:`tencentcloud.drm.v20181115.models.ModifyFairPlayPemRequest`
        :rtype: :class:`tencentcloud.drm.v20181115.models.ModifyFairPlayPemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFairPlayPem", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFairPlayPemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartEncryption(self, request):
        """开发者调用该接口，启动一次内容文件的DRM加密工作流。
        注意：该接口已下线。

        :param request: Request instance for StartEncryption.
        :type request: :class:`tencentcloud.drm.v20181115.models.StartEncryptionRequest`
        :rtype: :class:`tencentcloud.drm.v20181115.models.StartEncryptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartEncryption", params, headers=headers)
            response = json.loads(body)
            model = models.StartEncryptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))