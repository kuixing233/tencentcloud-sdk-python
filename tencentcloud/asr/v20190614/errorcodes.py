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


# CAM签名/鉴权错误。
AUTHFAILURE = 'AuthFailure'

# 用户没有权限进行此查询操作。
AUTHFAILURE_CHECKRESOURCERESPONSECODEERROR = 'AuthFailure.CheckResourceResponseCodeError'

# 鉴权错误。
AUTHFAILURE_INVALIDAUTHORIZATION = 'AuthFailure.InvalidAuthorization'

# 未授权操作。
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnauthorizedOperation'

# 操作失败。
FAILEDOPERATION = 'FailedOperation'

# 鉴权错误。
FAILEDOPERATION_CHECKAUTHINFOFAILED = 'FailedOperation.CheckAuthInfoFailed'

# 下载音频文件失败。
FAILEDOPERATION_ERRORDOWNFILE = 'FailedOperation.ErrorDownFile'

# 识别失败。
FAILEDOPERATION_ERRORRECOGNIZE = 'FailedOperation.ErrorRecognize'

# 错误的TaskId。
FAILEDOPERATION_NOSUCHTASK = 'FailedOperation.NoSuchTask'

# 不存在的说话人id
FAILEDOPERATION_NOTEXISTENTVOICEPRINTID = 'FailedOperation.NotExistentVoicePrintId'

# 账号因为欠费停止服务，请在腾讯云账户充值。
FAILEDOPERATION_SERVICEISOLATE = 'FailedOperation.ServiceIsolate'

# 资源包耗尽，请购买资源包或开通后付费
FAILEDOPERATION_USERHASNOAMOUNT = 'FailedOperation.UserHasNoAmount'

# 资源包耗尽，请开通后付费或者购买资源包
FAILEDOPERATION_USERHASNOFREEAMOUNT = 'FailedOperation.UserHasNoFreeAmount'

# 服务未开通，请在腾讯云官网语音识别控制台开通服务。
FAILEDOPERATION_USERNOTREGISTERED = 'FailedOperation.UserNotRegistered'

# 内部错误。
INTERNALERROR = 'InternalError'

# 初始化配置失败。
INTERNALERROR_ERRORCONFIGURE = 'InternalError.ErrorConfigure'

# 创建日志失败。
INTERNALERROR_ERRORCREATELOG = 'InternalError.ErrorCreateLog'

# 下载音频文件失败。
INTERNALERROR_ERRORDOWNFILE = 'InternalError.ErrorDownFile'

# 新建数组失败。
INTERNALERROR_ERRORFAILNEWPREQUEST = 'InternalError.ErrorFailNewprequest'

# 写入数据库失败。
INTERNALERROR_ERRORFAILWRITETODB = 'InternalError.ErrorFailWritetodb'

# 文件无法打开。
INTERNALERROR_ERRORFILECANNOTOPEN = 'InternalError.ErrorFileCannotopen'

# 获取路由失败。
INTERNALERROR_ERRORGETROUTE = 'InternalError.ErrorGetRoute'

# 创建日志路径失败。
INTERNALERROR_ERRORMAKELOGPATH = 'InternalError.ErrorMakeLogpath'

# 识别失败。
INTERNALERROR_ERRORRECOGNIZE = 'InternalError.ErrorRecognize'

# 访问数据库失败。
INTERNALERROR_FAILACCESSDATABASE = 'InternalError.FailAccessDatabase'

# 访问Redis失败。
INTERNALERROR_FAILACCESSREDIS = 'InternalError.FailAccessRedis'

# 说话人音频解码失败
INTERNALERROR_FAILEDVOICEPRINTDECODE = 'InternalError.FailedVoicePrintDecode'

# 说话人注册接口失败
INTERNALERROR_FAILEDVOICEPRINTENROLL = 'InternalError.FailedVoicePrintEnroll'

# 说话人验证接口失败
INTERNALERROR_FAILEDVOICEPRINTVERIFY = 'InternalError.FailedVoicePrintVerify'

# 请求标签接口出错
INTERNALERROR_TAGREQUESTERROR = 'InternalError.TagRequestError'

# 说话人音频处理失败
INTERNALERROR_VOICEPRINTAUDIOFAILED = 'InternalError.VoicePrintAudioFailed'

# 传入音频解码失败
INTERNALERROR_VOICEPRINTDECODEFAILED = 'InternalError.VoicePrintDecodeFailed'

# 说话人ID注册失败
INTERNALERROR_VOICEPRINTENROLLFAILED = 'InternalError.VoicePrintEnrollFailed'

# 说话人验证失败
INTERNALERROR_VOICEPRINTVERIFYFAILED = 'InternalError.VoicePrintVerifyFailed'

# 参数错误。
INVALIDPARAMETER = 'InvalidParameter'

# 请求数据长度无效。
INVALIDPARAMETER_ERRORCONTENTLENGTH = 'InvalidParameter.ErrorContentlength'

# 参数不全。
INVALIDPARAMETER_ERRORPARAMSMISSING = 'InvalidParameter.ErrorParamsMissing'

# 解析请求数据失败。
INVALIDPARAMETER_ERRORPARSEQUEST = 'InvalidParameter.ErrorParsequest'

# 音频解码失败，请检查音频格式是否正确
INVALIDPARAMETER_FAILEDVOICEPRINTDECODE = 'InvalidParameter.FailedVoicePrintDecode'

# 文件编码错误。
INVALIDPARAMETER_FILEENCODE = 'InvalidParameter.FileEncode'

# 参数错误。
INVALIDPARAMETER_INVALIDPARAMETER = 'InvalidParameter.InvalidParameter'

# 非法的词表状态。
INVALIDPARAMETER_INVALIDVOCABSTATE = 'InvalidParameter.InvalidVocabState'

# 关键词库名字已存在
INVALIDPARAMETER_KEYWORDLIBNAMEEXIST = 'InvalidParameter.KeyWordLibNameExist'

# 该模型状态不允许删除。
INVALIDPARAMETER_MODELSTATE = 'InvalidParameter.ModelState'

# 参数取值错误。
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# AppId无效。
INVALIDPARAMETERVALUE_ERRORINVALIDAPPID = 'InvalidParameterValue.ErrorInvalidAppid'

# ClientIp无效。
INVALIDPARAMETERVALUE_ERRORINVALIDCLIENTIP = 'InvalidParameterValue.ErrorInvalidClientip'

# EngSerViceType无效。
INVALIDPARAMETERVALUE_ERRORINVALIDENGSERVICE = 'InvalidParameterValue.ErrorInvalidEngservice'

# ProjectId无效。
INVALIDPARAMETERVALUE_ERRORINVALIDPROJECTID = 'InvalidParameterValue.ErrorInvalidProjectid'

# RequestId无效。
INVALIDPARAMETERVALUE_ERRORINVALIDREQUESTID = 'InvalidParameterValue.ErrorInvalidRequestid'

# SourceType无效。
INVALIDPARAMETERVALUE_ERRORINVALIDSOURCETYPE = 'InvalidParameterValue.ErrorInvalidSourcetype'

# SubserviceType无效。
INVALIDPARAMETERVALUE_ERRORINVALIDSUBSERVICETYPE = 'InvalidParameterValue.ErrorInvalidSubservicetype'

# Url无效。
INVALIDPARAMETERVALUE_ERRORINVALIDURL = 'InvalidParameterValue.ErrorInvalidUrl'

# UsrAudioKey无效。
INVALIDPARAMETERVALUE_ERRORINVALIDUSERAUDIOKEY = 'InvalidParameterValue.ErrorInvalidUseraudiokey'

# 音频编码格式不支持。
INVALIDPARAMETERVALUE_ERRORINVALIDVOICEFORMAT = 'InvalidParameterValue.ErrorInvalidVoiceFormat'

# 音频数据无效。
INVALIDPARAMETERVALUE_ERRORINVALIDVOICEDATA = 'InvalidParameterValue.ErrorInvalidVoicedata'

# 音频时长超过限制。
INVALIDPARAMETERVALUE_ERRORVOICEDATATOOLONG = 'InvalidParameterValue.ErrorVoicedataTooLong'

# 非法的参数长度。
INVALIDPARAMETERVALUE_INVALIDPARAMETERLENGTH = 'InvalidParameterValue.InvalidParameterLength'

# 非法的VocabId。
INVALIDPARAMETERVALUE_INVALIDVOCABID = 'InvalidParameterValue.InvalidVocabId'

# 非法的词表状态。
INVALIDPARAMETERVALUE_INVALIDVOCABSTATE = 'InvalidParameterValue.InvalidVocabState'

# 词权重不合法。
INVALIDPARAMETERVALUE_INVALIDWORDWEIGHT = 'InvalidParameterValue.InvalidWordWeight'

# 非法的WordWeightStr。
INVALIDPARAMETERVALUE_INVALIDWORDWEIGHTSTR = 'InvalidParameterValue.InvalidWordWeightStr'

# 模型不存在。
INVALIDPARAMETERVALUE_MODELID = 'InvalidParameterValue.ModelId'

# 音频内容没有人声或有效人声小于1秒
INVALIDPARAMETERVALUE_NOHUMANVOICE = 'InvalidParameterValue.NoHumanVoice'

# 非法的模型状态。
INVALIDPARAMETERVALUE_TOSTATE = 'InvalidParameterValue.ToState'

# 超过配额限制。
LIMITEXCEEDED = 'LimitExceeded'

# 自学习模型创建个数已到限制。
LIMITEXCEEDED_CUSTOMIZATIONFULL = 'LimitExceeded.CustomizationFull'

# 上线模型个数已到限制。
LIMITEXCEEDED_ONLINEFULL = 'LimitExceeded.OnlineFull'

# 热词表数量已到账号限制。
LIMITEXCEEDED_VOCABFULL = 'LimitExceeded.VocabFull'

# 说话人ID创建数量达到上限
LIMITEXCEEDED_VOICEPRINTFULL = 'LimitExceeded.VoicePrintFull'

# 缺少参数错误。
MISSINGPARAMETER = 'MissingParameter'

# 请求的次数超过了频率限制。
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# 超出请求频率。
REQUESTLIMITEXCEEDED_UINLIMITEXCEEDED = 'RequestLimitExceeded.UinLimitExceeded'

# 未知参数错误。
UNKNOWNPARAMETER = 'UnknownParameter'
