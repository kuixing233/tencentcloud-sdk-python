# -*- coding: utf-8 -*-
from contextlib import contextmanager
from urllib.parse import urlparse

import requests

from tencentcloud.common.exception import TencentCloudSDKException
from tencentcloud.common.credential import OIDCRoleArnCredential, STSAssumeRoleCredential


@contextmanager
def mock_requests():
    real_request = requests.Session.request
    req_args = {}

    def interceptor(self, method, url, **kwargs):
        req_args["method"] = method
        req_args["url"] = url
        return real_request(self, method, url, **kwargs)

    requests.Session.request = interceptor

    yield req_args
    
    requests.Session.request = real_request


def parse_host(url):
    return urlparse(url).hostname


def test_sts_endpoint_override():
    """测试 STSAssumeRoleCredential 指定 endpoint 是否生效"""

    expected_host = "sts.tencentcloudapi.com"

    cred =STSAssumeRoleCredential(
        "xx",
        "yy",
        "zz",
        "test",
        7000,
        "sts.tencentcloudapi.com"
    )

    with mock_requests() as req_args:
        try:
            cred._need_refresh()
        except TencentCloudSDKException:
            pass

        assert parse_host(req_args["url"]) == expected_host


def test_oidc_endpoint_override():
    """测试 OIDCRoleArnCredential 指定 endpoint 是否生效"""

    expected_host = "sts.tencentcloudapi.com"

    cred = OIDCRoleArnCredential(
        region="ap-guangzhou",
        provider_id="dummy-provider",
        web_identity_token="dummy-token",
        role_arn="dummy-arn",
        role_session_name="dummy-session",
        endpoint="sts.tencentcloudapi.com" 
    )

    with mock_requests() as req_args:
        try:
            cred._keep_fresh()
        except TencentCloudSDKException:
            pass

        assert parse_host(req_args["url"]) == expected_host
