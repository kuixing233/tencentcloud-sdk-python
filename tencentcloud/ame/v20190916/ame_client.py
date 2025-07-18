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
from tencentcloud.ame.v20190916 import models


class AmeClient(AbstractClient):
    _apiVersion = '2019-09-16'
    _endpoint = 'ame.tencentcloudapi.com'
    _service = 'ame'


    def BatchDescribeKTVMusicDetails(self, request):
        """根据 Id 列表查询歌曲的详细信息，包含基础信息及播放信息。

        :param request: Request instance for BatchDescribeKTVMusicDetails.
        :type request: :class:`tencentcloud.ame.v20190916.models.BatchDescribeKTVMusicDetailsRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.BatchDescribeKTVMusicDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDescribeKTVMusicDetails", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDescribeKTVMusicDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateKTVRobot(self, request):
        """创建机器人，支持进入 RTC 房间，播放直播互动曲库歌曲。

        :param request: Request instance for CreateKTVRobot.
        :type request: :class:`tencentcloud.ame.v20190916.models.CreateKTVRobotRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.CreateKTVRobotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateKTVRobot", params, headers=headers)
            response = json.loads(body)
            model = models.CreateKTVRobotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuthInfo(self, request):
        """获取授权项目信息列表

        :param request: Request instance for DescribeAuthInfo.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeAuthInfoRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeAuthInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuthInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuthInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudMusic(self, request):
        """获取云音乐播放信息接口

        :param request: Request instance for DescribeCloudMusic.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeCloudMusicRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeCloudMusicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudMusic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudMusicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudMusicPurchased(self, request):
        """获取授权项目下已购云音乐列表

        :param request: Request instance for DescribeCloudMusicPurchased.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeCloudMusicPurchasedRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeCloudMusicPurchasedResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudMusicPurchased", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudMusicPurchasedResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeItemById(self, request):
        """根据歌曲ID查询歌曲信息

        :param request: Request instance for DescribeItemById.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeItemByIdRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeItemByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeItemById", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeItemByIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeItems(self, request):
        """该服务后续会停用，不再建议使用

        :param request: Request instance for DescribeItems.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeItemsRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeItemsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeItems", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeItemsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKTVMusicDetail(self, request):
        """根据 Id 查询歌曲的详细信息，包含基础信息及播放信息。

        :param request: Request instance for DescribeKTVMusicDetail.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeKTVMusicDetailRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeKTVMusicDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKTVMusicDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKTVMusicDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKTVMusicTags(self, request):
        """获取直播互动曲库标签分组信息和标签信息

        :param request: Request instance for DescribeKTVMusicTags.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeKTVMusicTagsRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeKTVMusicTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKTVMusicTags", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKTVMusicTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKTVPlaylistDetail(self, request):
        """根据歌单 Id 获取歌单详情，包括歌单的基础信息以及歌曲列表。

        :param request: Request instance for DescribeKTVPlaylistDetail.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeKTVPlaylistDetailRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeKTVPlaylistDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKTVPlaylistDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKTVPlaylistDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKTVPlaylists(self, request):
        """获取直播互动曲库推荐歌单列表。

        :param request: Request instance for DescribeKTVPlaylists.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeKTVPlaylistsRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeKTVPlaylistsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKTVPlaylists", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKTVPlaylistsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKTVRobots(self, request):
        """获取机器人列表，支持 Id、状态等过滤条件。

        :param request: Request instance for DescribeKTVRobots.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeKTVRobotsRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeKTVRobotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKTVRobots", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKTVRobotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKTVSingerCategories(self, request):
        """获取直播互动曲库歌手分类信息

        :param request: Request instance for DescribeKTVSingerCategories.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeKTVSingerCategoriesRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeKTVSingerCategoriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKTVSingerCategories", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKTVSingerCategoriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKTVSingerMusics(self, request):
        """根据歌手id，返回该歌手下歌曲列表。



        :param request: Request instance for DescribeKTVSingerMusics.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeKTVSingerMusicsRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeKTVSingerMusicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKTVSingerMusics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKTVSingerMusicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKTVSingers(self, request):
        """根据过滤条件，返回匹配的歌手列表。

        :param request: Request instance for DescribeKTVSingers.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeKTVSingersRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeKTVSingersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKTVSingers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKTVSingersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKTVSuggestions(self, request):
        """获取直播互动曲库联想词

        :param request: Request instance for DescribeKTVSuggestions.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeKTVSuggestionsRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeKTVSuggestionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKTVSuggestions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKTVSuggestionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKTVTopList(self, request):
        """获取直播互动曲库歌曲的周榜和月榜

        :param request: Request instance for DescribeKTVTopList.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeKTVTopListRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeKTVTopListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKTVTopList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKTVTopListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLyric(self, request):
        """根据接口的模式及歌曲ID来取得歌词信息或者波形图信息。

        :param request: Request instance for DescribeLyric.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeLyricRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeLyricResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLyric", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLyricResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMusic(self, request):
        """获取曲库包歌曲播放信息接口

        :param request: Request instance for DescribeMusic.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeMusicRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeMusicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMusic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMusicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMusicSaleStatus(self, request):
        """根据音乐信息查询音乐是否在售

        :param request: Request instance for DescribeMusicSaleStatus.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeMusicSaleStatusRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeMusicSaleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMusicSaleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMusicSaleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePackageItems(self, request):
        """获取曲库包下已核销歌曲列表接口

        :param request: Request instance for DescribePackageItems.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribePackageItemsRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribePackageItemsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePackageItems", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePackageItemsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePackages(self, request):
        """获取已购曲库包列表接口

        :param request: Request instance for DescribePackages.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribePackagesRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribePackagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePackages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePackagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePkgOfflineMusic(self, request):
        """根据购买曲库包用户可查询已回退的歌曲信息

        :param request: Request instance for DescribePkgOfflineMusic.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribePkgOfflineMusicRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribePkgOfflineMusicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePkgOfflineMusic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePkgOfflineMusicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStations(self, request):
        """该服务后续会停用，不再建议使用

        :param request: Request instance for DescribeStations.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeStationsRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeStationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyKTVRobot(self, request):
        """销毁机器人，机器人退出 RTC 房间。

        :param request: Request instance for DestroyKTVRobot.
        :type request: :class:`tencentcloud.ame.v20190916.models.DestroyKTVRobotRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DestroyKTVRobotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyKTVRobot", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyKTVRobotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMusicOnShelves(self, request):
        """根据资源方，需要变更的参数，请求该接口进行变更，为空的参数默认为无变更

        :param request: Request instance for ModifyMusicOnShelves.
        :type request: :class:`tencentcloud.ame.v20190916.models.ModifyMusicOnShelvesRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.ModifyMusicOnShelvesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMusicOnShelves", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMusicOnShelvesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PutMusicOnTheShelves(self, request):
        """根据资源方所传歌曲信息，进行歌曲上架，多个歌曲同时请求时，需构造复合结构进行请求

        :param request: Request instance for PutMusicOnTheShelves.
        :type request: :class:`tencentcloud.ame.v20190916.models.PutMusicOnTheShelvesRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.PutMusicOnTheShelvesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PutMusicOnTheShelves", params, headers=headers)
            response = json.loads(body)
            model = models.PutMusicOnTheShelvesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReportData(self, request):
        """客户上报用户数据功能，为了更好地为用户提供优质服务

        :param request: Request instance for ReportData.
        :type request: :class:`tencentcloud.ame.v20190916.models.ReportDataRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.ReportDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReportData", params, headers=headers)
            response = json.loads(body)
            model = models.ReportDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchKTVMusics(self, request):
        """根据搜索条件，返回匹配的歌曲列表。

        :param request: Request instance for SearchKTVMusics.
        :type request: :class:`tencentcloud.ame.v20190916.models.SearchKTVMusicsRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.SearchKTVMusicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchKTVMusics", params, headers=headers)
            response = json.loads(body)
            model = models.SearchKTVMusicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncKTVRobotCommand(self, request):
        """下发操作机器人指令，支持播放、暂停、恢复、歌单设置等操作指令，实现对机器人行为的控制。

        :param request: Request instance for SyncKTVRobotCommand.
        :type request: :class:`tencentcloud.ame.v20190916.models.SyncKTVRobotCommandRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.SyncKTVRobotCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncKTVRobotCommand", params, headers=headers)
            response = json.loads(body)
            model = models.SyncKTVRobotCommandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TakeMusicOffShelves(self, request):
        """根据资源方所传MusicId进行将歌曲进行下架，多个MusicId使用逗号隔开

        :param request: Request instance for TakeMusicOffShelves.
        :type request: :class:`tencentcloud.ame.v20190916.models.TakeMusicOffShelvesRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.TakeMusicOffShelvesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TakeMusicOffShelves", params, headers=headers)
            response = json.loads(body)
            model = models.TakeMusicOffShelvesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))