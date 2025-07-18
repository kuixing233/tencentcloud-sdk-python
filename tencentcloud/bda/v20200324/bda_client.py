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
from tencentcloud.bda.v20200324 import models


class BdaClient(AbstractClient):
    _apiVersion = '2020-03-24'
    _endpoint = 'bda.tencentcloudapi.com'
    _service = 'bda'


    def CreateGroup(self, request):
        """用于创建一个空的人体库，如果人体库已存在返回错误。

        1个APPID下最多有2000W个人体动作轨迹（Trace），最多1W个人体库（Group）。

        单个人体库（Group）最多10W个人体动作轨迹（Trace）。

        单个人员（Person）最多添加 5 个人体动作轨迹（Trace）。

        :param request: Request instance for CreateGroup.
        :type request: :class:`tencentcloud.bda.v20200324.models.CreateGroupRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.CreateGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePerson(self, request):
        """创建人员，添加对应人员的人体动作轨迹信息。

        请注意：
        - 我们希望您的输入为 严格符合动作轨迹图片 要求的图片。如果您输入的图片不符合动作轨迹图片要求，会对最终效果产生较大负面影响。请您尽量保证一个Trace中的图片人体清晰、无遮挡、连贯；
        - 一个人体动作轨迹（Trace）可以包含1-5张人体图片。提供越多质量高的人体图片有助于提升最终识别结果；
        - 无论您在单个Trace中提供了多少张人体图片，我们都将生成一个对应的动作轨迹（Trace）信息。即，Trace仅和本次输入的图片序列相关，和图片的个数无关；
        - 输入的图片组中，若有部分图片输入不合法（如图片大小过大、分辨率过大、无法解码等），我们将舍弃这部分图片，确保合法图片被正确搜索。即，我们将尽可能保证请求成功，去除不合法的输入；
        - 构成人体动作轨迹单张图片大小不得超过2M，分辨率不得超过1920*1080。

        :param request: Request instance for CreatePerson.
        :type request: :class:`tencentcloud.bda.v20200324.models.CreatePersonRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.CreatePersonResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePerson", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePersonResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSegmentationTask(self, request):
        """本接口为人像分割在线处理接口组中的提交任务接口，可以对提交的资源进行处理视频流/图片流识别视频作品中的人像区域，进行一键抠像、背景替换、人像虚化等后期处理。

        :param request: Request instance for CreateSegmentationTask.
        :type request: :class:`tencentcloud.bda.v20200324.models.CreateSegmentationTaskRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.CreateSegmentationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSegmentationTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSegmentationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTrace(self, request):
        """将一个人体动作轨迹添加到一个人员中。一个人员最多允许包含 5 个人体动作轨迹。同一人的人体动作轨迹越多，搜索识别效果越好。

        >请注意：
        - 我们希望您的输入为 严格符合动作轨迹图片 要求的图片。如果您输入的图片不符合动作轨迹图片要求，会对最终效果产生较大负面影响。请您尽量保证一个Trace中的图片人体清晰、无遮挡、连贯。
        - 一个人体动作轨迹（Trace）可以包含1-5张人体图片。提供越多质量高的人体图片有助于提升最终识别结果。
        - 无论您在单个Trace中提供了多少张人体图片，我们都将生成一个对应的动作轨迹（Trace）信息。即，Trace仅和本次输入的图片序列相关，和图片的个数无关。
        - 输入的图片组中，若有部分图片输入不合法（如图片大小过大、分辨率过大、无法解码等），我们将舍弃这部分图片，确保合法图片被正确搜索。即，我们将尽可能保证请求成功，去除不合法的输入；
        - 构成人体动作轨迹单张图片大小限制为2M，分辨率限制为1920*1080。

        :param request: Request instance for CreateTrace.
        :type request: :class:`tencentcloud.bda.v20200324.models.CreateTraceRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.CreateTraceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTrace", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTraceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGroup(self, request):
        """删除该人体库及包含的所有的人员。

        :param request: Request instance for DeleteGroup.
        :type request: :class:`tencentcloud.bda.v20200324.models.DeleteGroupRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.DeleteGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePerson(self, request):
        """删除人员。

        :param request: Request instance for DeletePerson.
        :type request: :class:`tencentcloud.bda.v20200324.models.DeletePersonRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.DeletePersonResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePerson", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePersonResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSegmentationTask(self, request):
        """可以查看单条任务的处理情况，包括处理状态，处理结果。

        :param request: Request instance for DescribeSegmentationTask.
        :type request: :class:`tencentcloud.bda.v20200324.models.DescribeSegmentationTaskRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.DescribeSegmentationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSegmentationTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSegmentationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetectBody(self, request):
        """检测给定图片中的人体（Body）的位置信息及属性信息。

        :param request: Request instance for DetectBody.
        :type request: :class:`tencentcloud.bda.v20200324.models.DetectBodyRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.DetectBodyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetectBody", params, headers=headers)
            response = json.loads(body)
            model = models.DetectBodyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetectBodyJoints(self, request):
        """检测图片中人体的14个关键点。建议用于人体图像清晰、无遮挡的场景。支持一张图片中存在多个人体的识别。

        :param request: Request instance for DetectBodyJoints.
        :type request: :class:`tencentcloud.bda.v20200324.models.DetectBodyJointsRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.DetectBodyJointsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetectBodyJoints", params, headers=headers)
            response = json.loads(body)
            model = models.DetectBodyJointsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetGroupList(self, request):
        """获取人体库列表。

        :param request: Request instance for GetGroupList.
        :type request: :class:`tencentcloud.bda.v20200324.models.GetGroupListRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.GetGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.GetGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetPersonList(self, request):
        """获取指定人体库中的人员列表。

        :param request: Request instance for GetPersonList.
        :type request: :class:`tencentcloud.bda.v20200324.models.GetPersonListRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.GetPersonListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPersonList", params, headers=headers)
            response = json.loads(body)
            model = models.GetPersonListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetSummaryInfo(self, request):
        """获取人体库汇总信息。

        :param request: Request instance for GetSummaryInfo.
        :type request: :class:`tencentcloud.bda.v20200324.models.GetSummaryInfoRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.GetSummaryInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetSummaryInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetSummaryInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGroup(self, request):
        """修改人体库名称、备注。

        :param request: Request instance for ModifyGroup.
        :type request: :class:`tencentcloud.bda.v20200324.models.ModifyGroupRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.ModifyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPersonInfo(self, request):
        """修改人员信息。

        :param request: Request instance for ModifyPersonInfo.
        :type request: :class:`tencentcloud.bda.v20200324.models.ModifyPersonInfoRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.ModifyPersonInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPersonInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPersonInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchTrace(self, request):
        """本接口用于对一组待识别的人体动作轨迹（Trace）图片，在人体库中识别出最相似的 TopK 人体，按照相似度从大到小排列。

        人体动作轨迹（Trace）图片要求：图片中当且仅包含一个人体。人体完整、无遮挡。

        > 请注意：
        - 我们希望您的输入为严格符合动作轨迹图片要求的图片。如果您输入的图片不符合动作轨迹图片要求，会对最终效果产生较大负面影响；
        - 人体动作轨迹，是一个包含1-5张图片的图片序列。您可以输入1张图片作为动作轨迹，也可以输入多张。单个动作轨迹中包含越多符合质量的图片，搜索效果越好。
        - 构成人体动作轨迹单张图片大小不得超过2M，分辨率不得超过1920*1080。

        :param request: Request instance for SearchTrace.
        :type request: :class:`tencentcloud.bda.v20200324.models.SearchTraceRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.SearchTraceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchTrace", params, headers=headers)
            response = json.loads(body)
            model = models.SearchTraceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SegmentCustomizedPortraitPic(self, request):
        """在前后景分割的基础上优化多分类分割，支持对头发、五官等的分割，既作为换发型、挂件等底层技术，也可用于抠人头、抠人脸等玩法

        :param request: Request instance for SegmentCustomizedPortraitPic.
        :type request: :class:`tencentcloud.bda.v20200324.models.SegmentCustomizedPortraitPicRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.SegmentCustomizedPortraitPicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SegmentCustomizedPortraitPic", params, headers=headers)
            response = json.loads(body)
            model = models.SegmentCustomizedPortraitPicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SegmentPortraitPic(self, request):
        """即二分类人像分割，识别传入图片中人体的完整轮廓，进行抠像。

        :param request: Request instance for SegmentPortraitPic.
        :type request: :class:`tencentcloud.bda.v20200324.models.SegmentPortraitPicRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.SegmentPortraitPicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SegmentPortraitPic", params, headers=headers)
            response = json.loads(body)
            model = models.SegmentPortraitPicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateSegmentationTask(self, request):
        """终止指定视频人像分割处理任务

        :param request: Request instance for TerminateSegmentationTask.
        :type request: :class:`tencentcloud.bda.v20200324.models.TerminateSegmentationTaskRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.TerminateSegmentationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateSegmentationTask", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateSegmentationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))