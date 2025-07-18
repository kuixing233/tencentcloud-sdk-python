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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class Account(AbstractModel):
    """数据库账号信息

    """

    def __init__(self):
        r"""
        :param _User: 账户的名称
        :type User: str
        :param _Host: 账户的域名
        :type Host: str
        """
        self._User = None
        self._Host = None

    @property
    def User(self):
        """账户的名称
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Host(self):
        """账户的域名
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._User = params.get("User")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActiveHourDCDBInstanceRequest(AbstractModel):
    """ActiveHourDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 待升级的实例ID列表。形如：["dcdbt-ow728lmc"]，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        """待升级的实例ID列表。形如：["dcdbt-ow728lmc"]，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActiveHourDCDBInstanceResponse(AbstractModel):
    """ActiveHourDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuccessInstanceIds: 解隔离成功的实例id列表
        :type SuccessInstanceIds: list of str
        :param _FailedInstanceIds: 解隔离失败的实例id列表
        :type FailedInstanceIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessInstanceIds = None
        self._FailedInstanceIds = None
        self._RequestId = None

    @property
    def SuccessInstanceIds(self):
        """解隔离成功的实例id列表
        :rtype: list of str
        """
        return self._SuccessInstanceIds

    @SuccessInstanceIds.setter
    def SuccessInstanceIds(self, SuccessInstanceIds):
        self._SuccessInstanceIds = SuccessInstanceIds

    @property
    def FailedInstanceIds(self):
        """解隔离失败的实例id列表
        :rtype: list of str
        """
        return self._FailedInstanceIds

    @FailedInstanceIds.setter
    def FailedInstanceIds(self, FailedInstanceIds):
        self._FailedInstanceIds = FailedInstanceIds

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessInstanceIds = params.get("SuccessInstanceIds")
        self._FailedInstanceIds = params.get("FailedInstanceIds")
        self._RequestId = params.get("RequestId")


class AddShardConfig(AbstractModel):
    """升级实例 -- 新增分片类型

    """

    def __init__(self):
        r"""
        :param _ShardCount: 新增分片的数量
        :type ShardCount: int
        :param _ShardMemory: 分片内存大小，单位 GB
        :type ShardMemory: int
        :param _ShardStorage: 分片存储大小，单位 GB
        :type ShardStorage: int
        """
        self._ShardCount = None
        self._ShardMemory = None
        self._ShardStorage = None

    @property
    def ShardCount(self):
        """新增分片的数量
        :rtype: int
        """
        return self._ShardCount

    @ShardCount.setter
    def ShardCount(self, ShardCount):
        self._ShardCount = ShardCount

    @property
    def ShardMemory(self):
        """分片内存大小，单位 GB
        :rtype: int
        """
        return self._ShardMemory

    @ShardMemory.setter
    def ShardMemory(self, ShardMemory):
        self._ShardMemory = ShardMemory

    @property
    def ShardStorage(self):
        """分片存储大小，单位 GB
        :rtype: int
        """
        return self._ShardStorage

    @ShardStorage.setter
    def ShardStorage(self, ShardStorage):
        self._ShardStorage = ShardStorage


    def _deserialize(self, params):
        self._ShardCount = params.get("ShardCount")
        self._ShardMemory = params.get("ShardMemory")
        self._ShardStorage = params.get("ShardStorage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 数据库引擎名称，本接口取值：dcdb。
        :type Product: str
        :param _SecurityGroupId: 要绑定的安全组ID，类似sg-efil73jd。
        :type SecurityGroupId: str
        :param _InstanceIds: 被绑定的实例ID，类似tdsqlshard-lesecurk，支持指定多个实例。
        :type InstanceIds: list of str
        """
        self._Product = None
        self._SecurityGroupId = None
        self._InstanceIds = None

    @property
    def Product(self):
        """数据库引擎名称，本接口取值：dcdb。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def SecurityGroupId(self):
        """要绑定的安全组ID，类似sg-efil73jd。
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def InstanceIds(self):
        """被绑定的实例ID，类似tdsqlshard-lesecurk，支持指定多个实例。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class BackupConfig(AbstractModel):
    """数据库超期备份配置

    """

    def __init__(self):
        r"""
        :param _EnableBackupPolicy: 备份策略是否启用。
        :type EnableBackupPolicy: bool
        :param _BeginDate: 超期保留开始日期，早于开始日期的超期备份不保留，格式：yyyy-mm-dd。
        :type BeginDate: str
        :param _MaxRetentionDays: 超期备份保留时长，超出保留时间的超期备份将被删除，可填写1-3650整数。
        :type MaxRetentionDays: int
        :param _Frequency: 备份模式，可选择按年月周模式保存
* 按年：annually
* 按月：monthly
* 按周：weekly
        :type Frequency: str
        :param _WeekDays: Frequency等于weekly时生效。
表示保留特定工作日备份。可选择周一到周日，支持多选，取星期英文：
* 星期一 ：Monday
* 星期二 ：Tuesday
* 星期三：Wednesday
* 星期四：Thursday
* 星期五：Friday
* 星期六：Saturday
* 星期日：Sunday
        :type WeekDays: list of str
        :param _BackupCount: 保留备份个数，Frequency等于monthly或weekly时生效。
备份模式选择按月时，可填写1-28整数；
备份模式选择年时，可填写1-336整数。
        :type BackupCount: int
        """
        self._EnableBackupPolicy = None
        self._BeginDate = None
        self._MaxRetentionDays = None
        self._Frequency = None
        self._WeekDays = None
        self._BackupCount = None

    @property
    def EnableBackupPolicy(self):
        """备份策略是否启用。
        :rtype: bool
        """
        return self._EnableBackupPolicy

    @EnableBackupPolicy.setter
    def EnableBackupPolicy(self, EnableBackupPolicy):
        self._EnableBackupPolicy = EnableBackupPolicy

    @property
    def BeginDate(self):
        """超期保留开始日期，早于开始日期的超期备份不保留，格式：yyyy-mm-dd。
        :rtype: str
        """
        return self._BeginDate

    @BeginDate.setter
    def BeginDate(self, BeginDate):
        self._BeginDate = BeginDate

    @property
    def MaxRetentionDays(self):
        """超期备份保留时长，超出保留时间的超期备份将被删除，可填写1-3650整数。
        :rtype: int
        """
        return self._MaxRetentionDays

    @MaxRetentionDays.setter
    def MaxRetentionDays(self, MaxRetentionDays):
        self._MaxRetentionDays = MaxRetentionDays

    @property
    def Frequency(self):
        """备份模式，可选择按年月周模式保存
* 按年：annually
* 按月：monthly
* 按周：weekly
        :rtype: str
        """
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def WeekDays(self):
        """Frequency等于weekly时生效。
表示保留特定工作日备份。可选择周一到周日，支持多选，取星期英文：
* 星期一 ：Monday
* 星期二 ：Tuesday
* 星期三：Wednesday
* 星期四：Thursday
* 星期五：Friday
* 星期六：Saturday
* 星期日：Sunday
        :rtype: list of str
        """
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays

    @property
    def BackupCount(self):
        """保留备份个数，Frequency等于monthly或weekly时生效。
备份模式选择按月时，可填写1-28整数；
备份模式选择年时，可填写1-336整数。
        :rtype: int
        """
        return self._BackupCount

    @BackupCount.setter
    def BackupCount(self, BackupCount):
        self._BackupCount = BackupCount


    def _deserialize(self, params):
        self._EnableBackupPolicy = params.get("EnableBackupPolicy")
        self._BeginDate = params.get("BeginDate")
        self._MaxRetentionDays = params.get("MaxRetentionDays")
        self._Frequency = params.get("Frequency")
        self._WeekDays = params.get("WeekDays")
        self._BackupCount = params.get("BackupCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BriefNodeInfo(AbstractModel):
    """描述分片DB节点信息

    """

    def __init__(self):
        r"""
        :param _NodeId: DB节点ID
        :type NodeId: str
        :param _Role: DB节点角色，取值为master或者slave
        :type Role: str
        :param _ShardId: 节点所属分片的分片ID
        :type ShardId: str
        :param _Zone: 节点所在可用区
        :type Zone: str
        """
        self._NodeId = None
        self._Role = None
        self._ShardId = None
        self._Zone = None

    @property
    def NodeId(self):
        """DB节点ID
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Role(self):
        """DB节点角色，取值为master或者slave
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def ShardId(self):
        """节点所属分片的分片ID
        :rtype: str
        """
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def Zone(self):
        """节点所在可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._Role = params.get("Role")
        self._ShardId = params.get("ShardId")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelDcnJobRequest(AbstractModel):
    """CancelDcnJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 灾备实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """灾备实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelDcnJobResponse(AbstractModel):
    """CancelDcnJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """流程ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CancelOnlineDDLJobRequest(AbstractModel):
    """CancelOnlineDDLJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _FlowId: 要暂停的 Online DDL 任务对应的流程Id。创建任务时，CreateOnlineDDLJob 会返回此流程Id
        :type FlowId: int
        """
        self._InstanceId = None
        self._FlowId = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FlowId(self):
        """要暂停的 Online DDL 任务对应的流程Id。创建任务时，CreateOnlineDDLJob 会返回此流程Id
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelOnlineDDLJobResponse(AbstractModel):
    """CancelOnlineDDLJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CloneAccountRequest(AbstractModel):
    """CloneAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _SrcUser: 源用户账户名
        :type SrcUser: str
        :param _SrcHost: 源用户HOST
        :type SrcHost: str
        :param _DstUser: 目的用户账户名
        :type DstUser: str
        :param _DstHost: 目的用户HOST
        :type DstHost: str
        :param _DstDesc: 目的用户账户描述
        :type DstDesc: str
        """
        self._InstanceId = None
        self._SrcUser = None
        self._SrcHost = None
        self._DstUser = None
        self._DstHost = None
        self._DstDesc = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SrcUser(self):
        """源用户账户名
        :rtype: str
        """
        return self._SrcUser

    @SrcUser.setter
    def SrcUser(self, SrcUser):
        self._SrcUser = SrcUser

    @property
    def SrcHost(self):
        """源用户HOST
        :rtype: str
        """
        return self._SrcHost

    @SrcHost.setter
    def SrcHost(self, SrcHost):
        self._SrcHost = SrcHost

    @property
    def DstUser(self):
        """目的用户账户名
        :rtype: str
        """
        return self._DstUser

    @DstUser.setter
    def DstUser(self, DstUser):
        self._DstUser = DstUser

    @property
    def DstHost(self):
        """目的用户HOST
        :rtype: str
        """
        return self._DstHost

    @DstHost.setter
    def DstHost(self, DstHost):
        self._DstHost = DstHost

    @property
    def DstDesc(self):
        """目的用户账户描述
        :rtype: str
        """
        return self._DstDesc

    @DstDesc.setter
    def DstDesc(self, DstDesc):
        self._DstDesc = DstDesc


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SrcUser = params.get("SrcUser")
        self._SrcHost = params.get("SrcHost")
        self._DstUser = params.get("DstUser")
        self._DstHost = params.get("DstHost")
        self._DstDesc = params.get("DstDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneAccountResponse(AbstractModel):
    """CloneAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步任务流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """异步任务流程ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CloseDBExtranetAccessRequest(AbstractModel):
    """CloseDBExtranetAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 待关闭外网访问的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param _Ipv6Flag: 是否IPv6，默认0
        :type Ipv6Flag: int
        """
        self._InstanceId = None
        self._Ipv6Flag = None

    @property
    def InstanceId(self):
        """待关闭外网访问的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ipv6Flag(self):
        """是否IPv6，默认0
        :rtype: int
        """
        return self._Ipv6Flag

    @Ipv6Flag.setter
    def Ipv6Flag(self, Ipv6Flag):
        self._Ipv6Flag = Ipv6Flag


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Ipv6Flag = params.get("Ipv6Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseDBExtranetAccessResponse(AbstractModel):
    """CloseDBExtranetAccess返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步任务ID，可通过 DescribeFlow 查询任务状态。
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """异步任务ID，可通过 DescribeFlow 查询任务状态。
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ColumnPrivilege(AbstractModel):
    """列权限信息

    """

    def __init__(self):
        r"""
        :param _Database: 数据库名
        :type Database: str
        :param _Table: 数据库表名
        :type Table: str
        :param _Column: 数据库列名
        :type Column: str
        :param _Privileges: 权限信息
        :type Privileges: list of str
        """
        self._Database = None
        self._Table = None
        self._Column = None
        self._Privileges = None

    @property
    def Database(self):
        """数据库名
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        """数据库表名
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Column(self):
        """数据库列名
        :rtype: str
        """
        return self._Column

    @Column.setter
    def Column(self, Column):
        self._Column = Column

    @property
    def Privileges(self):
        """权限信息
        :rtype: list of str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._Column = params.get("Column")
        self._Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigValue(AbstractModel):
    """配置信息。包含配置项Config，配置值Value

    """

    def __init__(self):
        r"""
        :param _Config: 配置项的名称，支持填写max_user_connections
        :type Config: str
        :param _Value: 配置值
        :type Value: str
        """
        self._Config = None
        self._Value = None

    @property
    def Config(self):
        """配置项的名称，支持填写max_user_connections
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Value(self):
        """配置值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Config = params.get("Config")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConstraintRange(AbstractModel):
    """约束类型值的范围

    """

    def __init__(self):
        r"""
        :param _Min: 约束类型为section时的最小值
        :type Min: str
        :param _Max: 约束类型为section时的最大值
        :type Max: str
        """
        self._Min = None
        self._Max = None

    @property
    def Min(self):
        """约束类型为section时的最小值
        :rtype: str
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def Max(self):
        """约束类型为section时的最大值
        :rtype: str
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max


    def _deserialize(self, params):
        self._Min = params.get("Min")
        self._Max = params.get("Max")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyAccountPrivilegesRequest(AbstractModel):
    """CopyAccountPrivileges请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param _SrcUserName: 源用户名
        :type SrcUserName: str
        :param _SrcHost: 源用户允许的访问 host
        :type SrcHost: str
        :param _DstUserName: 目的用户名
        :type DstUserName: str
        :param _DstHost: 目的用户允许的访问 host
        :type DstHost: str
        :param _SrcReadOnly: 源账号的 ReadOnly 属性
        :type SrcReadOnly: str
        :param _DstReadOnly: 目的账号的 ReadOnly 属性
        :type DstReadOnly: str
        """
        self._InstanceId = None
        self._SrcUserName = None
        self._SrcHost = None
        self._DstUserName = None
        self._DstHost = None
        self._SrcReadOnly = None
        self._DstReadOnly = None

    @property
    def InstanceId(self):
        """实例 ID，形如：dcdbt-ow728lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SrcUserName(self):
        """源用户名
        :rtype: str
        """
        return self._SrcUserName

    @SrcUserName.setter
    def SrcUserName(self, SrcUserName):
        self._SrcUserName = SrcUserName

    @property
    def SrcHost(self):
        """源用户允许的访问 host
        :rtype: str
        """
        return self._SrcHost

    @SrcHost.setter
    def SrcHost(self, SrcHost):
        self._SrcHost = SrcHost

    @property
    def DstUserName(self):
        """目的用户名
        :rtype: str
        """
        return self._DstUserName

    @DstUserName.setter
    def DstUserName(self, DstUserName):
        self._DstUserName = DstUserName

    @property
    def DstHost(self):
        """目的用户允许的访问 host
        :rtype: str
        """
        return self._DstHost

    @DstHost.setter
    def DstHost(self, DstHost):
        self._DstHost = DstHost

    @property
    def SrcReadOnly(self):
        """源账号的 ReadOnly 属性
        :rtype: str
        """
        return self._SrcReadOnly

    @SrcReadOnly.setter
    def SrcReadOnly(self, SrcReadOnly):
        self._SrcReadOnly = SrcReadOnly

    @property
    def DstReadOnly(self):
        """目的账号的 ReadOnly 属性
        :rtype: str
        """
        return self._DstReadOnly

    @DstReadOnly.setter
    def DstReadOnly(self, DstReadOnly):
        self._DstReadOnly = DstReadOnly


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SrcUserName = params.get("SrcUserName")
        self._SrcHost = params.get("SrcHost")
        self._DstUserName = params.get("DstUserName")
        self._DstHost = params.get("DstHost")
        self._SrcReadOnly = params.get("SrcReadOnly")
        self._DstReadOnly = params.get("DstReadOnly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyAccountPrivilegesResponse(AbstractModel):
    """CopyAccountPrivileges返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateAccountRequest(AbstractModel):
    """CreateAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param _UserName: AccountName
        :type UserName: str
        :param _Host: 可以登录的主机，与mysql 账号的 host 格式一致，可以支持通配符，例如 %，10.%，10.20.%。
        :type Host: str
        :param _Password: 账号密码，密码需要 8-32 个字符，不能以 '/' 开头，并且必须包含小写字母、大写字母、数字和符号()~!@#$%^&*-+=_|{}[]:<>,.?/。
        :type Password: str
        :param _ReadOnly: 是否创建为只读账号，0：否， 1：该账号的sql请求优先选择备机执行，备机不可用时选择主机执行，2：优先选择备机执行，备机不可用时操作失败，3：只从备机读取。
        :type ReadOnly: int
        :param _Description: 账号备注，可以包含中文、英文字符、常见符号和数字，长度为0~256字符
        :type Description: str
        :param _DelayThresh: 如果备机延迟超过本参数设置值，系统将认为备机发生故障
建议该参数值大于10。当ReadOnly选择1、2时该参数生效。
        :type DelayThresh: int
        :param _SlaveConst: 针对只读账号，设置策略是否固定备机，0：不固定备机，即备机不满足条件与客户端不断开连接，Proxy选择其他可用备机，1：备机不满足条件断开连接，确保一个连接固定备机。
        :type SlaveConst: int
        :param _MaxUserConnections: 用户最大连接数限制参数。不传或者传0表示为不限制，对应max_user_connections参数，目前10.1内核版本不支持设置。
        :type MaxUserConnections: int
        :param _EncryptedPassword: 使用GetPublicKey返回的RSA2048公钥加密后的密码
        :type EncryptedPassword: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Host = None
        self._Password = None
        self._ReadOnly = None
        self._Description = None
        self._DelayThresh = None
        self._SlaveConst = None
        self._MaxUserConnections = None
        self._EncryptedPassword = None

    @property
    def InstanceId(self):
        """实例 ID，形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        """AccountName
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        """可以登录的主机，与mysql 账号的 host 格式一致，可以支持通配符，例如 %，10.%，10.20.%。
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Password(self):
        """账号密码，密码需要 8-32 个字符，不能以 '/' 开头，并且必须包含小写字母、大写字母、数字和符号()~!@#$%^&*-+=_|{}[]:<>,.?/。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ReadOnly(self):
        """是否创建为只读账号，0：否， 1：该账号的sql请求优先选择备机执行，备机不可用时选择主机执行，2：优先选择备机执行，备机不可用时操作失败，3：只从备机读取。
        :rtype: int
        """
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def Description(self):
        """账号备注，可以包含中文、英文字符、常见符号和数字，长度为0~256字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DelayThresh(self):
        """如果备机延迟超过本参数设置值，系统将认为备机发生故障
建议该参数值大于10。当ReadOnly选择1、2时该参数生效。
        :rtype: int
        """
        return self._DelayThresh

    @DelayThresh.setter
    def DelayThresh(self, DelayThresh):
        self._DelayThresh = DelayThresh

    @property
    def SlaveConst(self):
        """针对只读账号，设置策略是否固定备机，0：不固定备机，即备机不满足条件与客户端不断开连接，Proxy选择其他可用备机，1：备机不满足条件断开连接，确保一个连接固定备机。
        :rtype: int
        """
        return self._SlaveConst

    @SlaveConst.setter
    def SlaveConst(self, SlaveConst):
        self._SlaveConst = SlaveConst

    @property
    def MaxUserConnections(self):
        """用户最大连接数限制参数。不传或者传0表示为不限制，对应max_user_connections参数，目前10.1内核版本不支持设置。
        :rtype: int
        """
        return self._MaxUserConnections

    @MaxUserConnections.setter
    def MaxUserConnections(self, MaxUserConnections):
        self._MaxUserConnections = MaxUserConnections

    @property
    def EncryptedPassword(self):
        """使用GetPublicKey返回的RSA2048公钥加密后的密码
        :rtype: str
        """
        return self._EncryptedPassword

    @EncryptedPassword.setter
    def EncryptedPassword(self, EncryptedPassword):
        self._EncryptedPassword = EncryptedPassword


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._Password = params.get("Password")
        self._ReadOnly = params.get("ReadOnly")
        self._Description = params.get("Description")
        self._DelayThresh = params.get("DelayThresh")
        self._SlaveConst = params.get("SlaveConst")
        self._MaxUserConnections = params.get("MaxUserConnections")
        self._EncryptedPassword = params.get("EncryptedPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountResponse(AbstractModel):
    """CreateAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，透传入参。
        :type InstanceId: str
        :param _UserName: 用户名，透传入参。
        :type UserName: str
        :param _Host: 允许访问的 host，透传入参。
        :type Host: str
        :param _ReadOnly: 透传入参。
        :type ReadOnly: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Host = None
        self._ReadOnly = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """实例ID，透传入参。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        """用户名，透传入参。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        """允许访问的 host，透传入参。
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def ReadOnly(self):
        """透传入参。
        :rtype: int
        """
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._ReadOnly = params.get("ReadOnly")
        self._RequestId = params.get("RequestId")


class CreateDCDBInstanceRequest(AbstractModel):
    """CreateDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zones: 分片节点可用区分布，可填写多个可用区。
注意当前可售卖的可用区需要通过DescribeDCDBSaleInfo接口拉取。
        :type Zones: list of str
        :param _Period: 欲购买的时长，单位：月。
        :type Period: int
        :param _ShardMemory: 分片内存大小，单位：GB，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardMemory: int
        :param _ShardStorage: 分片存储空间大小，单位：GB，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardStorage: int
        :param _ShardNodeCount: 单个分片节点个数，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardNodeCount: int
        :param _ShardCount: 实例分片个数，可选范围2-8，可以通过升级实例进行新增分片到最多64个分片。
        :type ShardCount: int
        :param _Count: 欲购买实例的数量
        :type Count: int
        :param _ProjectId: 项目 ID，可以通过查看项目列表获取，不传则关联到默认项目
        :type ProjectId: int
        :param _VpcId: 虚拟私有网络 ID，不传或传空表示创建为基础网络
        :type VpcId: str
        :param _SubnetId: 虚拟私有网络子网 ID，VpcId不为空时必填
        :type SubnetId: str
        :param _DbVersionId: 数据库引擎版本，当前可选：8.0，5.7，10.1，10.0。
        :type DbVersionId: str
        :param _AutoVoucher: 是否自动使用代金券进行支付，默认不使用。
        :type AutoVoucher: bool
        :param _VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。
        :type VoucherIds: list of str
        :param _SecurityGroupId: 安全组id
        :type SecurityGroupId: str
        :param _InstanceName: 实例名称， 可以通过该字段自主的设置实例的名字
        :type InstanceName: str
        :param _Ipv6Flag: 是否支持IPv6，0:不支持，1:支持
        :type Ipv6Flag: int
        :param _ResourceTags: 标签键值对数组
        :type ResourceTags: list of ResourceTag
        :param _InitParams: 参数列表。本接口的可选值为：character_set_server（字符集，必传），lower_case_table_names（表名大小写敏感，必传，0 - 敏感；1-不敏感），innodb_page_size（innodb数据页，默认16K），sync_mode（同步模式：0 - 异步； 1 - 强同步；2 - 强同步可退化。默认为强同步可退化）。
        :type InitParams: list of DBParamValue
        :param _DcnRegion: DCN源地域
        :type DcnRegion: str
        :param _DcnInstanceId: DCN源实例ID
        :type DcnInstanceId: str
        :param _AutoRenewFlag: 自动续费标记，0:默认状态(用户未设置，即初始状态即手动续费，用户开通了预付费不停服特权也会进行自动续费)， 1:自动续费，2:明确不自动续费(用户设置)。若业务无续费概念或无需自动续费，需要设置为0
        :type AutoRenewFlag: int
        :param _SecurityGroupIds: 安全组ids，安全组可以传数组形式，兼容之前SecurityGroupId参数
        :type SecurityGroupIds: list of str
        :param _DcnSyncMode: DCN同步模式，0：异步， 1：强同步 
        :type DcnSyncMode: int
        :param _CpuType: Cpu类型，如：英特尔：Intel/AMD，海光：Hygon，默认Intel/AMD
        :type CpuType: str
        """
        self._Zones = None
        self._Period = None
        self._ShardMemory = None
        self._ShardStorage = None
        self._ShardNodeCount = None
        self._ShardCount = None
        self._Count = None
        self._ProjectId = None
        self._VpcId = None
        self._SubnetId = None
        self._DbVersionId = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._SecurityGroupId = None
        self._InstanceName = None
        self._Ipv6Flag = None
        self._ResourceTags = None
        self._InitParams = None
        self._DcnRegion = None
        self._DcnInstanceId = None
        self._AutoRenewFlag = None
        self._SecurityGroupIds = None
        self._DcnSyncMode = None
        self._CpuType = None

    @property
    def Zones(self):
        """分片节点可用区分布，可填写多个可用区。
注意当前可售卖的可用区需要通过DescribeDCDBSaleInfo接口拉取。
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def Period(self):
        """欲购买的时长，单位：月。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def ShardMemory(self):
        """分片内存大小，单位：GB，可以通过 DescribeShardSpec
 查询实例规格获得。
        :rtype: int
        """
        return self._ShardMemory

    @ShardMemory.setter
    def ShardMemory(self, ShardMemory):
        self._ShardMemory = ShardMemory

    @property
    def ShardStorage(self):
        """分片存储空间大小，单位：GB，可以通过 DescribeShardSpec
 查询实例规格获得。
        :rtype: int
        """
        return self._ShardStorage

    @ShardStorage.setter
    def ShardStorage(self, ShardStorage):
        self._ShardStorage = ShardStorage

    @property
    def ShardNodeCount(self):
        """单个分片节点个数，可以通过 DescribeShardSpec
 查询实例规格获得。
        :rtype: int
        """
        return self._ShardNodeCount

    @ShardNodeCount.setter
    def ShardNodeCount(self, ShardNodeCount):
        self._ShardNodeCount = ShardNodeCount

    @property
    def ShardCount(self):
        """实例分片个数，可选范围2-8，可以通过升级实例进行新增分片到最多64个分片。
        :rtype: int
        """
        return self._ShardCount

    @ShardCount.setter
    def ShardCount(self, ShardCount):
        self._ShardCount = ShardCount

    @property
    def Count(self):
        """欲购买实例的数量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def ProjectId(self):
        """项目 ID，可以通过查看项目列表获取，不传则关联到默认项目
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def VpcId(self):
        """虚拟私有网络 ID，不传或传空表示创建为基础网络
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """虚拟私有网络子网 ID，VpcId不为空时必填
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def DbVersionId(self):
        """数据库引擎版本，当前可选：8.0，5.7，10.1，10.0。
        :rtype: str
        """
        return self._DbVersionId

    @DbVersionId.setter
    def DbVersionId(self, DbVersionId):
        self._DbVersionId = DbVersionId

    @property
    def AutoVoucher(self):
        """是否自动使用代金券进行支付，默认不使用。
        :rtype: bool
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        """代金券ID列表，目前仅支持指定一张代金券。
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def SecurityGroupId(self):
        """安全组id
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def InstanceName(self):
        """实例名称， 可以通过该字段自主的设置实例的名字
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Ipv6Flag(self):
        """是否支持IPv6，0:不支持，1:支持
        :rtype: int
        """
        return self._Ipv6Flag

    @Ipv6Flag.setter
    def Ipv6Flag(self, Ipv6Flag):
        self._Ipv6Flag = Ipv6Flag

    @property
    def ResourceTags(self):
        """标签键值对数组
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def InitParams(self):
        """参数列表。本接口的可选值为：character_set_server（字符集，必传），lower_case_table_names（表名大小写敏感，必传，0 - 敏感；1-不敏感），innodb_page_size（innodb数据页，默认16K），sync_mode（同步模式：0 - 异步； 1 - 强同步；2 - 强同步可退化。默认为强同步可退化）。
        :rtype: list of DBParamValue
        """
        return self._InitParams

    @InitParams.setter
    def InitParams(self, InitParams):
        self._InitParams = InitParams

    @property
    def DcnRegion(self):
        """DCN源地域
        :rtype: str
        """
        return self._DcnRegion

    @DcnRegion.setter
    def DcnRegion(self, DcnRegion):
        self._DcnRegion = DcnRegion

    @property
    def DcnInstanceId(self):
        """DCN源实例ID
        :rtype: str
        """
        return self._DcnInstanceId

    @DcnInstanceId.setter
    def DcnInstanceId(self, DcnInstanceId):
        self._DcnInstanceId = DcnInstanceId

    @property
    def AutoRenewFlag(self):
        """自动续费标记，0:默认状态(用户未设置，即初始状态即手动续费，用户开通了预付费不停服特权也会进行自动续费)， 1:自动续费，2:明确不自动续费(用户设置)。若业务无续费概念或无需自动续费，需要设置为0
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def SecurityGroupIds(self):
        """安全组ids，安全组可以传数组形式，兼容之前SecurityGroupId参数
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def DcnSyncMode(self):
        """DCN同步模式，0：异步， 1：强同步 
        :rtype: int
        """
        return self._DcnSyncMode

    @DcnSyncMode.setter
    def DcnSyncMode(self, DcnSyncMode):
        self._DcnSyncMode = DcnSyncMode

    @property
    def CpuType(self):
        """Cpu类型，如：英特尔：Intel/AMD，海光：Hygon，默认Intel/AMD
        :rtype: str
        """
        return self._CpuType

    @CpuType.setter
    def CpuType(self, CpuType):
        self._CpuType = CpuType


    def _deserialize(self, params):
        self._Zones = params.get("Zones")
        self._Period = params.get("Period")
        self._ShardMemory = params.get("ShardMemory")
        self._ShardStorage = params.get("ShardStorage")
        self._ShardNodeCount = params.get("ShardNodeCount")
        self._ShardCount = params.get("ShardCount")
        self._Count = params.get("Count")
        self._ProjectId = params.get("ProjectId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._DbVersionId = params.get("DbVersionId")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._InstanceName = params.get("InstanceName")
        self._Ipv6Flag = params.get("Ipv6Flag")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        if params.get("InitParams") is not None:
            self._InitParams = []
            for item in params.get("InitParams"):
                obj = DBParamValue()
                obj._deserialize(item)
                self._InitParams.append(obj)
        self._DcnRegion = params.get("DcnRegion")
        self._DcnInstanceId = params.get("DcnInstanceId")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._DcnSyncMode = params.get("DcnSyncMode")
        self._CpuType = params.get("CpuType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDCDBInstanceResponse(AbstractModel):
    """CreateDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealName: 长订单号。可以据此调用 DescribeOrders
 查询订单详细信息，或在支付失败时调用用户账号相关接口进行支付。
        :type DealName: str
        :param _InstanceIds: 订单对应的实例 ID 列表，如果此处没有返回实例 ID，可以通过订单查询接口获取。还可通过实例查询接口查询实例是否创建完成。
        :type InstanceIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealName = None
        self._InstanceIds = None
        self._RequestId = None

    @property
    def DealName(self):
        """长订单号。可以据此调用 DescribeOrders
 查询订单详细信息，或在支付失败时调用用户账号相关接口进行支付。
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def InstanceIds(self):
        """订单对应的实例 ID 列表，如果此处没有返回实例 ID，可以通过订单查询接口获取。还可通过实例查询接口查询实例是否创建完成。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._InstanceIds = params.get("InstanceIds")
        self._RequestId = params.get("RequestId")


class CreateDedicatedClusterDCDBInstanceRequest(AbstractModel):
    """CreateDedicatedClusterDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GoodsNum: 分配实例个数
        :type GoodsNum: int
        :param _ShardNum: 分片数量
        :type ShardNum: int
        :param _ShardMemory: 分片內存大小, 单位GB
        :type ShardMemory: int
        :param _ShardStorage: 分片磁盘大小, 单位GB
        :type ShardStorage: int
        :param _ClusterId: 独享集群集群uuid
        :type ClusterId: str
        :param _Zone: （废弃）可用区
        :type Zone: str
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _Cpu: （废弃）cpu大小，单位：核
        :type Cpu: int
        :param _VpcId: 网络ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _ShardMachine: （废弃）分片机型
        :type ShardMachine: str
        :param _ShardNodeNum: 分片的节点个数
        :type ShardNodeNum: int
        :param _ShardNodeCpu: （废弃）节点cpu核数，单位：1/100核
        :type ShardNodeCpu: int
        :param _ShardNodeMemory: （废弃）节点內存大小，单位：GB
        :type ShardNodeMemory: int
        :param _ShardNodeStorage: （废弃）节点磁盘大小，单位：GB
        :type ShardNodeStorage: int
        :param _DbVersionId: db版本
        :type DbVersionId: str
        :param _SecurityGroupId: 安全组ID
        :type SecurityGroupId: str
        :param _SecurityGroupIds: 安全组ID列表
        :type SecurityGroupIds: list of str
        :param _DcnInstanceId: DCN源实例ID
        :type DcnInstanceId: str
        :param _DcnRegion: DCN源实例地域名
        :type DcnRegion: str
        :param _InstanceName: 自定义实例名称
        :type InstanceName: str
        :param _ResourceTags: 标签
        :type ResourceTags: list of ResourceTag
        :param _Ipv6Flag: 支持IPv6标志：1 支持， 0 不支持
        :type Ipv6Flag: int
        :param _Pid: （废弃）Pid，可通过获取独享集群售卖配置接口得到
        :type Pid: int
        :param _InitParams: 参数列表。本接口的可选值为：character_set_server（字符集，必传），lower_case_table_names（表名大小写敏感，必传，0 - 敏感；1-不敏感），innodb_page_size（innodb数据页，默认16K），sync_mode（同步模式：0 - 异步； 1 - 强同步；2 - 强同步可退化。默认为强同步可退化）。
        :type InitParams: list of DBParamValue
        :param _MasterHostId: 指定主节点uuid，不填随机分配
        :type MasterHostId: str
        :param _SlaveHostIds: 指定从节点uuid，不填随机分配
        :type SlaveHostIds: list of str
        :param _RollbackInstanceId: 需要回档的源实例ID
        :type RollbackInstanceId: str
        :param _RollbackTime: 回档时间
        :type RollbackTime: str
        :param _DcnSyncMode: DCN同步模式，0：异步， 1：强同步
        :type DcnSyncMode: int
        """
        self._GoodsNum = None
        self._ShardNum = None
        self._ShardMemory = None
        self._ShardStorage = None
        self._ClusterId = None
        self._Zone = None
        self._ProjectId = None
        self._Cpu = None
        self._VpcId = None
        self._SubnetId = None
        self._ShardMachine = None
        self._ShardNodeNum = None
        self._ShardNodeCpu = None
        self._ShardNodeMemory = None
        self._ShardNodeStorage = None
        self._DbVersionId = None
        self._SecurityGroupId = None
        self._SecurityGroupIds = None
        self._DcnInstanceId = None
        self._DcnRegion = None
        self._InstanceName = None
        self._ResourceTags = None
        self._Ipv6Flag = None
        self._Pid = None
        self._InitParams = None
        self._MasterHostId = None
        self._SlaveHostIds = None
        self._RollbackInstanceId = None
        self._RollbackTime = None
        self._DcnSyncMode = None

    @property
    def GoodsNum(self):
        """分配实例个数
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def ShardNum(self):
        """分片数量
        :rtype: int
        """
        return self._ShardNum

    @ShardNum.setter
    def ShardNum(self, ShardNum):
        self._ShardNum = ShardNum

    @property
    def ShardMemory(self):
        """分片內存大小, 单位GB
        :rtype: int
        """
        return self._ShardMemory

    @ShardMemory.setter
    def ShardMemory(self, ShardMemory):
        self._ShardMemory = ShardMemory

    @property
    def ShardStorage(self):
        """分片磁盘大小, 单位GB
        :rtype: int
        """
        return self._ShardStorage

    @ShardStorage.setter
    def ShardStorage(self, ShardStorage):
        self._ShardStorage = ShardStorage

    @property
    def ClusterId(self):
        """独享集群集群uuid
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Zone(self):
        """（废弃）可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ProjectId(self):
        """项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Cpu(self):
        """（废弃）cpu大小，单位：核
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def VpcId(self):
        """网络ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ShardMachine(self):
        """（废弃）分片机型
        :rtype: str
        """
        return self._ShardMachine

    @ShardMachine.setter
    def ShardMachine(self, ShardMachine):
        self._ShardMachine = ShardMachine

    @property
    def ShardNodeNum(self):
        """分片的节点个数
        :rtype: int
        """
        return self._ShardNodeNum

    @ShardNodeNum.setter
    def ShardNodeNum(self, ShardNodeNum):
        self._ShardNodeNum = ShardNodeNum

    @property
    def ShardNodeCpu(self):
        """（废弃）节点cpu核数，单位：1/100核
        :rtype: int
        """
        return self._ShardNodeCpu

    @ShardNodeCpu.setter
    def ShardNodeCpu(self, ShardNodeCpu):
        self._ShardNodeCpu = ShardNodeCpu

    @property
    def ShardNodeMemory(self):
        """（废弃）节点內存大小，单位：GB
        :rtype: int
        """
        return self._ShardNodeMemory

    @ShardNodeMemory.setter
    def ShardNodeMemory(self, ShardNodeMemory):
        self._ShardNodeMemory = ShardNodeMemory

    @property
    def ShardNodeStorage(self):
        """（废弃）节点磁盘大小，单位：GB
        :rtype: int
        """
        return self._ShardNodeStorage

    @ShardNodeStorage.setter
    def ShardNodeStorage(self, ShardNodeStorage):
        self._ShardNodeStorage = ShardNodeStorage

    @property
    def DbVersionId(self):
        """db版本
        :rtype: str
        """
        return self._DbVersionId

    @DbVersionId.setter
    def DbVersionId(self, DbVersionId):
        self._DbVersionId = DbVersionId

    @property
    def SecurityGroupId(self):
        """安全组ID
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupIds(self):
        """安全组ID列表
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def DcnInstanceId(self):
        """DCN源实例ID
        :rtype: str
        """
        return self._DcnInstanceId

    @DcnInstanceId.setter
    def DcnInstanceId(self, DcnInstanceId):
        self._DcnInstanceId = DcnInstanceId

    @property
    def DcnRegion(self):
        """DCN源实例地域名
        :rtype: str
        """
        return self._DcnRegion

    @DcnRegion.setter
    def DcnRegion(self, DcnRegion):
        self._DcnRegion = DcnRegion

    @property
    def InstanceName(self):
        """自定义实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ResourceTags(self):
        """标签
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def Ipv6Flag(self):
        """支持IPv6标志：1 支持， 0 不支持
        :rtype: int
        """
        return self._Ipv6Flag

    @Ipv6Flag.setter
    def Ipv6Flag(self, Ipv6Flag):
        self._Ipv6Flag = Ipv6Flag

    @property
    def Pid(self):
        """（废弃）Pid，可通过获取独享集群售卖配置接口得到
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def InitParams(self):
        """参数列表。本接口的可选值为：character_set_server（字符集，必传），lower_case_table_names（表名大小写敏感，必传，0 - 敏感；1-不敏感），innodb_page_size（innodb数据页，默认16K），sync_mode（同步模式：0 - 异步； 1 - 强同步；2 - 强同步可退化。默认为强同步可退化）。
        :rtype: list of DBParamValue
        """
        return self._InitParams

    @InitParams.setter
    def InitParams(self, InitParams):
        self._InitParams = InitParams

    @property
    def MasterHostId(self):
        """指定主节点uuid，不填随机分配
        :rtype: str
        """
        return self._MasterHostId

    @MasterHostId.setter
    def MasterHostId(self, MasterHostId):
        self._MasterHostId = MasterHostId

    @property
    def SlaveHostIds(self):
        """指定从节点uuid，不填随机分配
        :rtype: list of str
        """
        return self._SlaveHostIds

    @SlaveHostIds.setter
    def SlaveHostIds(self, SlaveHostIds):
        self._SlaveHostIds = SlaveHostIds

    @property
    def RollbackInstanceId(self):
        """需要回档的源实例ID
        :rtype: str
        """
        return self._RollbackInstanceId

    @RollbackInstanceId.setter
    def RollbackInstanceId(self, RollbackInstanceId):
        self._RollbackInstanceId = RollbackInstanceId

    @property
    def RollbackTime(self):
        """回档时间
        :rtype: str
        """
        return self._RollbackTime

    @RollbackTime.setter
    def RollbackTime(self, RollbackTime):
        self._RollbackTime = RollbackTime

    @property
    def DcnSyncMode(self):
        """DCN同步模式，0：异步， 1：强同步
        :rtype: int
        """
        return self._DcnSyncMode

    @DcnSyncMode.setter
    def DcnSyncMode(self, DcnSyncMode):
        self._DcnSyncMode = DcnSyncMode


    def _deserialize(self, params):
        self._GoodsNum = params.get("GoodsNum")
        self._ShardNum = params.get("ShardNum")
        self._ShardMemory = params.get("ShardMemory")
        self._ShardStorage = params.get("ShardStorage")
        self._ClusterId = params.get("ClusterId")
        self._Zone = params.get("Zone")
        self._ProjectId = params.get("ProjectId")
        self._Cpu = params.get("Cpu")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ShardMachine = params.get("ShardMachine")
        self._ShardNodeNum = params.get("ShardNodeNum")
        self._ShardNodeCpu = params.get("ShardNodeCpu")
        self._ShardNodeMemory = params.get("ShardNodeMemory")
        self._ShardNodeStorage = params.get("ShardNodeStorage")
        self._DbVersionId = params.get("DbVersionId")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._DcnInstanceId = params.get("DcnInstanceId")
        self._DcnRegion = params.get("DcnRegion")
        self._InstanceName = params.get("InstanceName")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._Ipv6Flag = params.get("Ipv6Flag")
        self._Pid = params.get("Pid")
        if params.get("InitParams") is not None:
            self._InitParams = []
            for item in params.get("InitParams"):
                obj = DBParamValue()
                obj._deserialize(item)
                self._InitParams.append(obj)
        self._MasterHostId = params.get("MasterHostId")
        self._SlaveHostIds = params.get("SlaveHostIds")
        self._RollbackInstanceId = params.get("RollbackInstanceId")
        self._RollbackTime = params.get("RollbackTime")
        self._DcnSyncMode = params.get("DcnSyncMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDedicatedClusterDCDBInstanceResponse(AbstractModel):
    """CreateDedicatedClusterDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 分配资源ID数组
        :type InstanceIds: list of str
        :param _FlowId: 流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceIds = None
        self._FlowId = None
        self._RequestId = None

    @property
    def InstanceIds(self):
        """分配资源ID数组
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def FlowId(self):
        """流程ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CreateHourDCDBInstanceRequest(AbstractModel):
    """CreateHourDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ShardMemory: 分片内存大小，单位：GB，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardMemory: int
        :param _ShardStorage: 分片存储空间大小，单位：GB，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardStorage: int
        :param _ShardNodeCount: 单个分片节点个数，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardNodeCount: int
        :param _ShardCount: 实例分片个数，可选范围2-8，可以通过升级实例进行新增分片到最多64个分片。
        :type ShardCount: int
        :param _Count: 欲购买实例的数量
        :type Count: int
        :param _ProjectId: 项目 ID，可以通过查看项目列表获取，不传则关联到默认项目
        :type ProjectId: int
        :param _VpcId: 虚拟私有网络 ID，不传或传空表示创建为基础网络
        :type VpcId: str
        :param _SubnetId: 虚拟私有网络子网 ID，VpcId不为空时必填
        :type SubnetId: str
        :param _ShardCpu: 分片cpu大小，单位：核，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardCpu: int
        :param _DbVersionId: 数据库引擎版本，当前可选：8.0，5.7，10.1，10.0。
        :type DbVersionId: str
        :param _Zones: 分片节点可用区分布，可填写多个可用区。
        :type Zones: list of str
        :param _SecurityGroupId: 安全组id
        :type SecurityGroupId: str
        :param _InstanceName: 实例名称， 可以通过该字段自主的设置实例的名字
        :type InstanceName: str
        :param _Ipv6Flag: 是否支持IPv6，0:不支持，1:支持
        :type Ipv6Flag: int
        :param _ResourceTags: 标签键值对数组
        :type ResourceTags: list of ResourceTag
        :param _DcnRegion: DCN源地域
        :type DcnRegion: str
        :param _DcnInstanceId: DCN源实例ID
        :type DcnInstanceId: str
        :param _InitParams: 参数列表。本接口的可选值为：character_set_server（字符集，必传），lower_case_table_names（表名大小写敏感，必传，0 - 敏感；1-不敏感），innodb_page_size（innodb数据页，默认16K），sync_mode（同步模式：0 - 异步； 1 - 强同步；2 - 强同步可退化。默认为强同步可退化）。
        :type InitParams: list of DBParamValue
        :param _RollbackInstanceId: 需要回档的源实例ID
        :type RollbackInstanceId: str
        :param _RollbackTime: 回档时间，例如“2021-11-22 00:00:00”
        :type RollbackTime: str
        :param _SecurityGroupIds: 安全组ids，安全组可以传数组形式，兼容之前SecurityGroupId参数
        :type SecurityGroupIds: list of str
        :param _DcnSyncMode: DCN同步模式，0：异步， 1：强同步
        :type DcnSyncMode: int
        :param _CpuType: Cpu类型，如：英特尔：Intel/AMD，海光：Hygon，默认Intel/AMD
        :type CpuType: str
        """
        self._ShardMemory = None
        self._ShardStorage = None
        self._ShardNodeCount = None
        self._ShardCount = None
        self._Count = None
        self._ProjectId = None
        self._VpcId = None
        self._SubnetId = None
        self._ShardCpu = None
        self._DbVersionId = None
        self._Zones = None
        self._SecurityGroupId = None
        self._InstanceName = None
        self._Ipv6Flag = None
        self._ResourceTags = None
        self._DcnRegion = None
        self._DcnInstanceId = None
        self._InitParams = None
        self._RollbackInstanceId = None
        self._RollbackTime = None
        self._SecurityGroupIds = None
        self._DcnSyncMode = None
        self._CpuType = None

    @property
    def ShardMemory(self):
        """分片内存大小，单位：GB，可以通过 DescribeShardSpec
 查询实例规格获得。
        :rtype: int
        """
        return self._ShardMemory

    @ShardMemory.setter
    def ShardMemory(self, ShardMemory):
        self._ShardMemory = ShardMemory

    @property
    def ShardStorage(self):
        """分片存储空间大小，单位：GB，可以通过 DescribeShardSpec
 查询实例规格获得。
        :rtype: int
        """
        return self._ShardStorage

    @ShardStorage.setter
    def ShardStorage(self, ShardStorage):
        self._ShardStorage = ShardStorage

    @property
    def ShardNodeCount(self):
        """单个分片节点个数，可以通过 DescribeShardSpec
 查询实例规格获得。
        :rtype: int
        """
        return self._ShardNodeCount

    @ShardNodeCount.setter
    def ShardNodeCount(self, ShardNodeCount):
        self._ShardNodeCount = ShardNodeCount

    @property
    def ShardCount(self):
        """实例分片个数，可选范围2-8，可以通过升级实例进行新增分片到最多64个分片。
        :rtype: int
        """
        return self._ShardCount

    @ShardCount.setter
    def ShardCount(self, ShardCount):
        self._ShardCount = ShardCount

    @property
    def Count(self):
        """欲购买实例的数量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def ProjectId(self):
        """项目 ID，可以通过查看项目列表获取，不传则关联到默认项目
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def VpcId(self):
        """虚拟私有网络 ID，不传或传空表示创建为基础网络
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """虚拟私有网络子网 ID，VpcId不为空时必填
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ShardCpu(self):
        """分片cpu大小，单位：核，可以通过 DescribeShardSpec
 查询实例规格获得。
        :rtype: int
        """
        return self._ShardCpu

    @ShardCpu.setter
    def ShardCpu(self, ShardCpu):
        self._ShardCpu = ShardCpu

    @property
    def DbVersionId(self):
        """数据库引擎版本，当前可选：8.0，5.7，10.1，10.0。
        :rtype: str
        """
        return self._DbVersionId

    @DbVersionId.setter
    def DbVersionId(self, DbVersionId):
        self._DbVersionId = DbVersionId

    @property
    def Zones(self):
        """分片节点可用区分布，可填写多个可用区。
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def SecurityGroupId(self):
        """安全组id
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def InstanceName(self):
        """实例名称， 可以通过该字段自主的设置实例的名字
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Ipv6Flag(self):
        """是否支持IPv6，0:不支持，1:支持
        :rtype: int
        """
        return self._Ipv6Flag

    @Ipv6Flag.setter
    def Ipv6Flag(self, Ipv6Flag):
        self._Ipv6Flag = Ipv6Flag

    @property
    def ResourceTags(self):
        """标签键值对数组
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def DcnRegion(self):
        """DCN源地域
        :rtype: str
        """
        return self._DcnRegion

    @DcnRegion.setter
    def DcnRegion(self, DcnRegion):
        self._DcnRegion = DcnRegion

    @property
    def DcnInstanceId(self):
        """DCN源实例ID
        :rtype: str
        """
        return self._DcnInstanceId

    @DcnInstanceId.setter
    def DcnInstanceId(self, DcnInstanceId):
        self._DcnInstanceId = DcnInstanceId

    @property
    def InitParams(self):
        """参数列表。本接口的可选值为：character_set_server（字符集，必传），lower_case_table_names（表名大小写敏感，必传，0 - 敏感；1-不敏感），innodb_page_size（innodb数据页，默认16K），sync_mode（同步模式：0 - 异步； 1 - 强同步；2 - 强同步可退化。默认为强同步可退化）。
        :rtype: list of DBParamValue
        """
        return self._InitParams

    @InitParams.setter
    def InitParams(self, InitParams):
        self._InitParams = InitParams

    @property
    def RollbackInstanceId(self):
        """需要回档的源实例ID
        :rtype: str
        """
        return self._RollbackInstanceId

    @RollbackInstanceId.setter
    def RollbackInstanceId(self, RollbackInstanceId):
        self._RollbackInstanceId = RollbackInstanceId

    @property
    def RollbackTime(self):
        """回档时间，例如“2021-11-22 00:00:00”
        :rtype: str
        """
        return self._RollbackTime

    @RollbackTime.setter
    def RollbackTime(self, RollbackTime):
        self._RollbackTime = RollbackTime

    @property
    def SecurityGroupIds(self):
        """安全组ids，安全组可以传数组形式，兼容之前SecurityGroupId参数
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def DcnSyncMode(self):
        """DCN同步模式，0：异步， 1：强同步
        :rtype: int
        """
        return self._DcnSyncMode

    @DcnSyncMode.setter
    def DcnSyncMode(self, DcnSyncMode):
        self._DcnSyncMode = DcnSyncMode

    @property
    def CpuType(self):
        """Cpu类型，如：英特尔：Intel/AMD，海光：Hygon，默认Intel/AMD
        :rtype: str
        """
        return self._CpuType

    @CpuType.setter
    def CpuType(self, CpuType):
        self._CpuType = CpuType


    def _deserialize(self, params):
        self._ShardMemory = params.get("ShardMemory")
        self._ShardStorage = params.get("ShardStorage")
        self._ShardNodeCount = params.get("ShardNodeCount")
        self._ShardCount = params.get("ShardCount")
        self._Count = params.get("Count")
        self._ProjectId = params.get("ProjectId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ShardCpu = params.get("ShardCpu")
        self._DbVersionId = params.get("DbVersionId")
        self._Zones = params.get("Zones")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._InstanceName = params.get("InstanceName")
        self._Ipv6Flag = params.get("Ipv6Flag")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._DcnRegion = params.get("DcnRegion")
        self._DcnInstanceId = params.get("DcnInstanceId")
        if params.get("InitParams") is not None:
            self._InitParams = []
            for item in params.get("InitParams"):
                obj = DBParamValue()
                obj._deserialize(item)
                self._InitParams.append(obj)
        self._RollbackInstanceId = params.get("RollbackInstanceId")
        self._RollbackTime = params.get("RollbackTime")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._DcnSyncMode = params.get("DcnSyncMode")
        self._CpuType = params.get("CpuType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHourDCDBInstanceResponse(AbstractModel):
    """CreateHourDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 订单对应的实例 ID 列表，如果此处没有返回实例 ID，可以通过订单查询接口获取。还可通过实例查询接口查询实例是否创建完成。
        :type InstanceIds: list of str
        :param _FlowId: 流程id，可以根据流程id查询创建进度
        :type FlowId: int
        :param _DealName: 订单号。可以据此调用 DescribeOrders
 查询订单详细信息，或在支付失败时调用用户账号相关接口进行支付。
        :type DealName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceIds = None
        self._FlowId = None
        self._DealName = None
        self._RequestId = None

    @property
    def InstanceIds(self):
        """订单对应的实例 ID 列表，如果此处没有返回实例 ID，可以通过订单查询接口获取。还可通过实例查询接口查询实例是否创建完成。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def FlowId(self):
        """流程id，可以根据流程id查询创建进度
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def DealName(self):
        """订单号。可以据此调用 DescribeOrders
 查询订单详细信息，或在支付失败时调用用户账号相关接口进行支付。
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._FlowId = params.get("FlowId")
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class CreateOnlineDDLJobRequest(AbstractModel):
    """CreateOnlineDDLJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Alter: 要执行的 DDL 语句。常用的在线DDL参考此API文档示例部分
        :type Alter: str
        :param _DbName: 要修改的数据库	
        :type DbName: str
        :param _Table: 要修改的表
        :type Table: str
        :param _User: 指定账号执行DDL，需确保账号有 ALTER, CREATE, INSERT, UPDATE, DROP, DELETE, INDEX, CREATE TEMPORARY TABLES, LOCK TABLES, TRIGGER, REPLICATION CLIENT, REPLICATION SLAVE 等相关权限 （若不填写将默认使用系统账号）
        :type User: str
        :param _Password: 指定账号的密码
        :type Password: str
        :param _CriticalLoad: 运行线程数大于此值时，将终止DDL。不填则默认58
        :type CriticalLoad: int
        :param _CheckAutoInc: 是否检查自增字段。为1则不允许修改自增字段，0或不填写则不检查
        :type CheckAutoInc: int
        :param _MaxDelay: 允许的主备延迟时间(单位s)，0或不填写则不检查延迟
        :type MaxDelay: int
        :param _UsePt: 是否使用pt-osc工具做DDL
        :type UsePt: int
        :param _StartTime: 开始执行时间
        :type StartTime: str
        """
        self._InstanceId = None
        self._Alter = None
        self._DbName = None
        self._Table = None
        self._User = None
        self._Password = None
        self._CriticalLoad = None
        self._CheckAutoInc = None
        self._MaxDelay = None
        self._UsePt = None
        self._StartTime = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Alter(self):
        """要执行的 DDL 语句。常用的在线DDL参考此API文档示例部分
        :rtype: str
        """
        return self._Alter

    @Alter.setter
    def Alter(self, Alter):
        self._Alter = Alter

    @property
    def DbName(self):
        """要修改的数据库	
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Table(self):
        """要修改的表
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def User(self):
        """指定账号执行DDL，需确保账号有 ALTER, CREATE, INSERT, UPDATE, DROP, DELETE, INDEX, CREATE TEMPORARY TABLES, LOCK TABLES, TRIGGER, REPLICATION CLIENT, REPLICATION SLAVE 等相关权限 （若不填写将默认使用系统账号）
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        """指定账号的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def CriticalLoad(self):
        """运行线程数大于此值时，将终止DDL。不填则默认58
        :rtype: int
        """
        return self._CriticalLoad

    @CriticalLoad.setter
    def CriticalLoad(self, CriticalLoad):
        self._CriticalLoad = CriticalLoad

    @property
    def CheckAutoInc(self):
        """是否检查自增字段。为1则不允许修改自增字段，0或不填写则不检查
        :rtype: int
        """
        return self._CheckAutoInc

    @CheckAutoInc.setter
    def CheckAutoInc(self, CheckAutoInc):
        self._CheckAutoInc = CheckAutoInc

    @property
    def MaxDelay(self):
        """允许的主备延迟时间(单位s)，0或不填写则不检查延迟
        :rtype: int
        """
        return self._MaxDelay

    @MaxDelay.setter
    def MaxDelay(self, MaxDelay):
        self._MaxDelay = MaxDelay

    @property
    def UsePt(self):
        """是否使用pt-osc工具做DDL
        :rtype: int
        """
        return self._UsePt

    @UsePt.setter
    def UsePt(self, UsePt):
        self._UsePt = UsePt

    @property
    def StartTime(self):
        """开始执行时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Alter = params.get("Alter")
        self._DbName = params.get("DbName")
        self._Table = params.get("Table")
        self._User = params.get("User")
        self._Password = params.get("Password")
        self._CriticalLoad = params.get("CriticalLoad")
        self._CheckAutoInc = params.get("CheckAutoInc")
        self._MaxDelay = params.get("MaxDelay")
        self._UsePt = params.get("UsePt")
        self._StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOnlineDDLJobResponse(AbstractModel):
    """CreateOnlineDDLJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 在线DDL任务Id
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """在线DDL任务Id
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CreateTmpDCDBInstanceRequest(AbstractModel):
    """CreateTmpDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 回档实例的ID
        :type InstanceId: str
        :param _RollbackTime: 回档时间点
        :type RollbackTime: str
        """
        self._InstanceId = None
        self._RollbackTime = None

    @property
    def InstanceId(self):
        """回档实例的ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RollbackTime(self):
        """回档时间点
        :rtype: str
        """
        return self._RollbackTime

    @RollbackTime.setter
    def RollbackTime(self, RollbackTime):
        self._RollbackTime = RollbackTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RollbackTime = params.get("RollbackTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTmpDCDBInstanceResponse(AbstractModel):
    """CreateTmpDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务流ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """任务流ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class DBAccount(AbstractModel):
    """云数据库账号信息

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名
        :type UserName: str
        :param _Host: 用户可以从哪台主机登录（对应 MySQL 用户的 host 字段，UserName + Host 唯一标识一个用户，IP形式，IP段以%结尾；支持填入%；为空默认等于%）
        :type Host: str
        :param _Description: 用户备注信息
        :type Description: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 最后更新时间
        :type UpdateTime: str
        :param _ReadOnly: 只读标记，0：否， 1：该账号的sql请求优先选择备机执行，备机不可用时选择主机执行，2：优先选择备机执行，备机不可用时操作失败。
        :type ReadOnly: int
        :param _DelayThresh: 如果备机延迟超过本参数设置值，系统将认为备机发生故障
建议该参数值大于10。当ReadOnly选择1、2时该参数生效。
        :type DelayThresh: int
        :param _SlaveConst: 针对只读账号，设置策略是否固定备机，0：不固定备机，即备机不满足条件与客户端不断开连接，Proxy选择其他可用备机，1：备机不满足条件断开连接，确保一个连接固定备机。
        :type SlaveConst: int
        :param _MaxUserConnections: 用户最大连接数，0代表无限制	
        :type MaxUserConnections: int
        """
        self._UserName = None
        self._Host = None
        self._Description = None
        self._CreateTime = None
        self._UpdateTime = None
        self._ReadOnly = None
        self._DelayThresh = None
        self._SlaveConst = None
        self._MaxUserConnections = None

    @property
    def UserName(self):
        """用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        """用户可以从哪台主机登录（对应 MySQL 用户的 host 字段，UserName + Host 唯一标识一个用户，IP形式，IP段以%结尾；支持填入%；为空默认等于%）
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Description(self):
        """用户备注信息
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """最后更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ReadOnly(self):
        """只读标记，0：否， 1：该账号的sql请求优先选择备机执行，备机不可用时选择主机执行，2：优先选择备机执行，备机不可用时操作失败。
        :rtype: int
        """
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def DelayThresh(self):
        """如果备机延迟超过本参数设置值，系统将认为备机发生故障
建议该参数值大于10。当ReadOnly选择1、2时该参数生效。
        :rtype: int
        """
        return self._DelayThresh

    @DelayThresh.setter
    def DelayThresh(self, DelayThresh):
        self._DelayThresh = DelayThresh

    @property
    def SlaveConst(self):
        """针对只读账号，设置策略是否固定备机，0：不固定备机，即备机不满足条件与客户端不断开连接，Proxy选择其他可用备机，1：备机不满足条件断开连接，确保一个连接固定备机。
        :rtype: int
        """
        return self._SlaveConst

    @SlaveConst.setter
    def SlaveConst(self, SlaveConst):
        self._SlaveConst = SlaveConst

    @property
    def MaxUserConnections(self):
        """用户最大连接数，0代表无限制	
        :rtype: int
        """
        return self._MaxUserConnections

    @MaxUserConnections.setter
    def MaxUserConnections(self, MaxUserConnections):
        self._MaxUserConnections = MaxUserConnections


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._ReadOnly = params.get("ReadOnly")
        self._DelayThresh = params.get("DelayThresh")
        self._SlaveConst = params.get("SlaveConst")
        self._MaxUserConnections = params.get("MaxUserConnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBParamValue(AbstractModel):
    """云数据库参数信息。

    """

    def __init__(self):
        r"""
        :param _Param: 参数名称
        :type Param: str
        :param _Value: 参数值
        :type Value: str
        """
        self._Param = None
        self._Value = None

    @property
    def Param(self):
        """参数名称
        :rtype: str
        """
        return self._Param

    @Param.setter
    def Param(self, Param):
        self._Param = Param

    @property
    def Value(self):
        """参数值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Param = params.get("Param")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DCDBInstanceInfo(AbstractModel):
    """分布式数据库实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _AppId: 应用ID
        :type AppId: int
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _Region: 地域
        :type Region: str
        :param _Zone: 可用区
        :type Zone: str
        :param _VpcId: VPC数字ID
        :type VpcId: int
        :param _SubnetId: Subnet数字ID
        :type SubnetId: int
        :param _StatusDesc: 状态中文描述
        :type StatusDesc: str
        :param _Status: 实例状态：0 创建中，1 流程处理中， 2 运行中，3 实例未初始化，-1 实例已隔离，4 实例初始化中，5 实例删除中，6 实例重启中，7 数据迁移中
        :type Status: int
        :param _Vip: 内网IP
        :type Vip: str
        :param _Vport: 内网端口
        :type Vport: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _AutoRenewFlag: 自动续费标志
        :type AutoRenewFlag: int
        :param _Memory: 内存大小，单位 GB
        :type Memory: int
        :param _Storage: 存储大小，单位 GB
        :type Storage: int
        :param _ShardCount: 分片个数
        :type ShardCount: int
        :param _PeriodEndTime: 到期时间
        :type PeriodEndTime: str
        :param _IsolatedTimestamp: 隔离时间
        :type IsolatedTimestamp: str
        :param _Uin: 账号ID
        :type Uin: str
        :param _ShardDetail: 分片详情
        :type ShardDetail: list of ShardInfo
        :param _NodeCount: 节点数，2 为一主一从， 3 为一主二从
        :type NodeCount: int
        :param _IsTmp: 临时实例标记，0 为非临时实例
        :type IsTmp: int
        :param _ExclusterId: 独享集群ID，为空表示非独享集群实例
        :type ExclusterId: str
        :param _UniqueVpcId: 字符串型的私有网络ID
        :type UniqueVpcId: str
        :param _UniqueSubnetId: 字符串型的私有网络子网ID
        :type UniqueSubnetId: str
        :param _Id: 数字实例ID（过时字段，请勿依赖该值）
        :type Id: int
        :param _WanDomain: 外网访问的域名，公网可解析
        :type WanDomain: str
        :param _WanVip: 外网 IP 地址，公网可访问
        :type WanVip: str
        :param _WanPort: 外网端口
        :type WanPort: int
        :param _Pid: 产品类型 ID（过时字段，请勿依赖该值）
        :type Pid: int
        :param _UpdateTime: 实例最后更新时间，格式为 2006-01-02 15:04:05
        :type UpdateTime: str
        :param _DbEngine: 数据库引擎
        :type DbEngine: str
        :param _DbVersion: 数据库引擎版本
        :type DbVersion: str
        :param _Paymode: 付费模式
        :type Paymode: str
        :param _Locker: 实例处于异步任务状态时，表示异步任务流程ID
        :type Locker: int
        :param _WanStatus: 外网状态，0-未开通；1-已开通；2-关闭；3-开通中
        :type WanStatus: int
        :param _IsAuditSupported: 该实例是否支持审计。1-支持；0-不支持
        :type IsAuditSupported: int
        :param _Cpu: Cpu核数
        :type Cpu: int
        :param _Ipv6Flag: 实例IPv6标志
        :type Ipv6Flag: int
        :param _Vipv6: 内网IPv6
        :type Vipv6: str
        :param _WanVipv6: 外网IPv6
        :type WanVipv6: str
        :param _WanPortIpv6: 外网IPv6端口
        :type WanPortIpv6: int
        :param _WanStatusIpv6: 外网IPv6状态
        :type WanStatusIpv6: int
        :param _DcnFlag: DCN标志，0-无，1-主实例，2-灾备实例
        :type DcnFlag: int
        :param _DcnStatus: DCN状态，0-无，1-创建中，2-同步中，3-已断开
        :type DcnStatus: int
        :param _DcnDstNum: DCN灾备实例数
        :type DcnDstNum: int
        :param _InstanceType: 1： 主实例（独享型）, 2: 主实例, 3： 灾备实例, 4： 灾备实例（独享型）
        :type InstanceType: int
        :param _ResourceTags: 实例标签信息
        :type ResourceTags: list of ResourceTag
        :param _DbVersionId: 数据库引擎版本
        :type DbVersionId: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._AppId = None
        self._ProjectId = None
        self._Region = None
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._StatusDesc = None
        self._Status = None
        self._Vip = None
        self._Vport = None
        self._CreateTime = None
        self._AutoRenewFlag = None
        self._Memory = None
        self._Storage = None
        self._ShardCount = None
        self._PeriodEndTime = None
        self._IsolatedTimestamp = None
        self._Uin = None
        self._ShardDetail = None
        self._NodeCount = None
        self._IsTmp = None
        self._ExclusterId = None
        self._UniqueVpcId = None
        self._UniqueSubnetId = None
        self._Id = None
        self._WanDomain = None
        self._WanVip = None
        self._WanPort = None
        self._Pid = None
        self._UpdateTime = None
        self._DbEngine = None
        self._DbVersion = None
        self._Paymode = None
        self._Locker = None
        self._WanStatus = None
        self._IsAuditSupported = None
        self._Cpu = None
        self._Ipv6Flag = None
        self._Vipv6 = None
        self._WanVipv6 = None
        self._WanPortIpv6 = None
        self._WanStatusIpv6 = None
        self._DcnFlag = None
        self._DcnStatus = None
        self._DcnDstNum = None
        self._InstanceType = None
        self._ResourceTags = None
        self._DbVersionId = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AppId(self):
        """应用ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ProjectId(self):
        """项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Region(self):
        """地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        """VPC数字ID
        :rtype: int
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Subnet数字ID
        :rtype: int
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def StatusDesc(self):
        """状态中文描述
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def Status(self):
        """实例状态：0 创建中，1 流程处理中， 2 运行中，3 实例未初始化，-1 实例已隔离，4 实例初始化中，5 实例删除中，6 实例重启中，7 数据迁移中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Vip(self):
        """内网IP
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """内网端口
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AutoRenewFlag(self):
        """自动续费标志
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def Memory(self):
        """内存大小，单位 GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        """存储大小，单位 GB
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def ShardCount(self):
        """分片个数
        :rtype: int
        """
        return self._ShardCount

    @ShardCount.setter
    def ShardCount(self, ShardCount):
        self._ShardCount = ShardCount

    @property
    def PeriodEndTime(self):
        """到期时间
        :rtype: str
        """
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def IsolatedTimestamp(self):
        """隔离时间
        :rtype: str
        """
        return self._IsolatedTimestamp

    @IsolatedTimestamp.setter
    def IsolatedTimestamp(self, IsolatedTimestamp):
        self._IsolatedTimestamp = IsolatedTimestamp

    @property
    def Uin(self):
        """账号ID
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ShardDetail(self):
        """分片详情
        :rtype: list of ShardInfo
        """
        return self._ShardDetail

    @ShardDetail.setter
    def ShardDetail(self, ShardDetail):
        self._ShardDetail = ShardDetail

    @property
    def NodeCount(self):
        """节点数，2 为一主一从， 3 为一主二从
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def IsTmp(self):
        """临时实例标记，0 为非临时实例
        :rtype: int
        """
        return self._IsTmp

    @IsTmp.setter
    def IsTmp(self, IsTmp):
        self._IsTmp = IsTmp

    @property
    def ExclusterId(self):
        """独享集群ID，为空表示非独享集群实例
        :rtype: str
        """
        return self._ExclusterId

    @ExclusterId.setter
    def ExclusterId(self, ExclusterId):
        self._ExclusterId = ExclusterId

    @property
    def UniqueVpcId(self):
        """字符串型的私有网络ID
        :rtype: str
        """
        return self._UniqueVpcId

    @UniqueVpcId.setter
    def UniqueVpcId(self, UniqueVpcId):
        self._UniqueVpcId = UniqueVpcId

    @property
    def UniqueSubnetId(self):
        """字符串型的私有网络子网ID
        :rtype: str
        """
        return self._UniqueSubnetId

    @UniqueSubnetId.setter
    def UniqueSubnetId(self, UniqueSubnetId):
        self._UniqueSubnetId = UniqueSubnetId

    @property
    def Id(self):
        """数字实例ID（过时字段，请勿依赖该值）
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def WanDomain(self):
        """外网访问的域名，公网可解析
        :rtype: str
        """
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain

    @property
    def WanVip(self):
        """外网 IP 地址，公网可访问
        :rtype: str
        """
        return self._WanVip

    @WanVip.setter
    def WanVip(self, WanVip):
        self._WanVip = WanVip

    @property
    def WanPort(self):
        """外网端口
        :rtype: int
        """
        return self._WanPort

    @WanPort.setter
    def WanPort(self, WanPort):
        self._WanPort = WanPort

    @property
    def Pid(self):
        """产品类型 ID（过时字段，请勿依赖该值）
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def UpdateTime(self):
        """实例最后更新时间，格式为 2006-01-02 15:04:05
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def DbEngine(self):
        """数据库引擎
        :rtype: str
        """
        return self._DbEngine

    @DbEngine.setter
    def DbEngine(self, DbEngine):
        self._DbEngine = DbEngine

    @property
    def DbVersion(self):
        """数据库引擎版本
        :rtype: str
        """
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def Paymode(self):
        """付费模式
        :rtype: str
        """
        return self._Paymode

    @Paymode.setter
    def Paymode(self, Paymode):
        self._Paymode = Paymode

    @property
    def Locker(self):
        """实例处于异步任务状态时，表示异步任务流程ID
        :rtype: int
        """
        return self._Locker

    @Locker.setter
    def Locker(self, Locker):
        self._Locker = Locker

    @property
    def WanStatus(self):
        """外网状态，0-未开通；1-已开通；2-关闭；3-开通中
        :rtype: int
        """
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

    @property
    def IsAuditSupported(self):
        """该实例是否支持审计。1-支持；0-不支持
        :rtype: int
        """
        return self._IsAuditSupported

    @IsAuditSupported.setter
    def IsAuditSupported(self, IsAuditSupported):
        self._IsAuditSupported = IsAuditSupported

    @property
    def Cpu(self):
        """Cpu核数
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Ipv6Flag(self):
        """实例IPv6标志
        :rtype: int
        """
        return self._Ipv6Flag

    @Ipv6Flag.setter
    def Ipv6Flag(self, Ipv6Flag):
        self._Ipv6Flag = Ipv6Flag

    @property
    def Vipv6(self):
        """内网IPv6
        :rtype: str
        """
        return self._Vipv6

    @Vipv6.setter
    def Vipv6(self, Vipv6):
        self._Vipv6 = Vipv6

    @property
    def WanVipv6(self):
        """外网IPv6
        :rtype: str
        """
        return self._WanVipv6

    @WanVipv6.setter
    def WanVipv6(self, WanVipv6):
        self._WanVipv6 = WanVipv6

    @property
    def WanPortIpv6(self):
        """外网IPv6端口
        :rtype: int
        """
        return self._WanPortIpv6

    @WanPortIpv6.setter
    def WanPortIpv6(self, WanPortIpv6):
        self._WanPortIpv6 = WanPortIpv6

    @property
    def WanStatusIpv6(self):
        """外网IPv6状态
        :rtype: int
        """
        return self._WanStatusIpv6

    @WanStatusIpv6.setter
    def WanStatusIpv6(self, WanStatusIpv6):
        self._WanStatusIpv6 = WanStatusIpv6

    @property
    def DcnFlag(self):
        """DCN标志，0-无，1-主实例，2-灾备实例
        :rtype: int
        """
        return self._DcnFlag

    @DcnFlag.setter
    def DcnFlag(self, DcnFlag):
        self._DcnFlag = DcnFlag

    @property
    def DcnStatus(self):
        """DCN状态，0-无，1-创建中，2-同步中，3-已断开
        :rtype: int
        """
        return self._DcnStatus

    @DcnStatus.setter
    def DcnStatus(self, DcnStatus):
        self._DcnStatus = DcnStatus

    @property
    def DcnDstNum(self):
        """DCN灾备实例数
        :rtype: int
        """
        return self._DcnDstNum

    @DcnDstNum.setter
    def DcnDstNum(self, DcnDstNum):
        self._DcnDstNum = DcnDstNum

    @property
    def InstanceType(self):
        """1： 主实例（独享型）, 2: 主实例, 3： 灾备实例, 4： 灾备实例（独享型）
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ResourceTags(self):
        """实例标签信息
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def DbVersionId(self):
        """数据库引擎版本
        :rtype: str
        """
        return self._DbVersionId

    @DbVersionId.setter
    def DbVersionId(self, DbVersionId):
        self._DbVersionId = DbVersionId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AppId = params.get("AppId")
        self._ProjectId = params.get("ProjectId")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._StatusDesc = params.get("StatusDesc")
        self._Status = params.get("Status")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._CreateTime = params.get("CreateTime")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._ShardCount = params.get("ShardCount")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._IsolatedTimestamp = params.get("IsolatedTimestamp")
        self._Uin = params.get("Uin")
        if params.get("ShardDetail") is not None:
            self._ShardDetail = []
            for item in params.get("ShardDetail"):
                obj = ShardInfo()
                obj._deserialize(item)
                self._ShardDetail.append(obj)
        self._NodeCount = params.get("NodeCount")
        self._IsTmp = params.get("IsTmp")
        self._ExclusterId = params.get("ExclusterId")
        self._UniqueVpcId = params.get("UniqueVpcId")
        self._UniqueSubnetId = params.get("UniqueSubnetId")
        self._Id = params.get("Id")
        self._WanDomain = params.get("WanDomain")
        self._WanVip = params.get("WanVip")
        self._WanPort = params.get("WanPort")
        self._Pid = params.get("Pid")
        self._UpdateTime = params.get("UpdateTime")
        self._DbEngine = params.get("DbEngine")
        self._DbVersion = params.get("DbVersion")
        self._Paymode = params.get("Paymode")
        self._Locker = params.get("Locker")
        self._WanStatus = params.get("WanStatus")
        self._IsAuditSupported = params.get("IsAuditSupported")
        self._Cpu = params.get("Cpu")
        self._Ipv6Flag = params.get("Ipv6Flag")
        self._Vipv6 = params.get("Vipv6")
        self._WanVipv6 = params.get("WanVipv6")
        self._WanPortIpv6 = params.get("WanPortIpv6")
        self._WanStatusIpv6 = params.get("WanStatusIpv6")
        self._DcnFlag = params.get("DcnFlag")
        self._DcnStatus = params.get("DcnStatus")
        self._DcnDstNum = params.get("DcnDstNum")
        self._InstanceType = params.get("InstanceType")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._DbVersionId = params.get("DbVersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DCDBShardInfo(AbstractModel):
    """描述分布式数据库分片信息。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 所属实例Id
        :type InstanceId: str
        :param _ShardSerialId: 分片SQL透传Id，用于将sql透传到指定分片执行
        :type ShardSerialId: str
        :param _ShardInstanceId: 全局唯一的分片Id
        :type ShardInstanceId: str
        :param _Status: 状态：0 创建中，1 流程处理中， 2 运行中，3 分片未初始化
        :type Status: int
        :param _StatusDesc: 状态中文描述
        :type StatusDesc: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _VpcId: 字符串格式的私有网络Id
        :type VpcId: str
        :param _SubnetId: 字符串格式的私有网络子网Id
        :type SubnetId: str
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _Region: 地域
        :type Region: str
        :param _Zone: 可用区
        :type Zone: str
        :param _Memory: 内存大小，单位 GB
        :type Memory: int
        :param _Storage: 存储大小，单位 GB
        :type Storage: int
        :param _PeriodEndTime: 到期时间
        :type PeriodEndTime: str
        :param _NodeCount: 节点数，2 为一主一从， 3 为一主二从
        :type NodeCount: int
        :param _StorageUsage: 存储使用率，单位为 %
        :type StorageUsage: float
        :param _MemoryUsage: 内存使用率，单位为 %
        :type MemoryUsage: float
        :param _ShardId: 数字分片Id（过时字段，请勿依赖该值）
        :type ShardId: int
        :param _Pid: 产品ProductID
        :type Pid: int
        :param _ProxyVersion: Proxy版本
        :type ProxyVersion: str
        :param _Paymode: 付费模型
        :type Paymode: str
        :param _ShardMasterZone: 分片的主可用区
        :type ShardMasterZone: str
        :param _ShardSlaveZones: 分片的从可用区列表
        :type ShardSlaveZones: list of str
        :param _Cpu: CPU核数
        :type Cpu: int
        :param _Range: 分片ShardKey的范围（总共64个哈希值），例如： 0-31，32-63
        :type Range: str
        """
        self._InstanceId = None
        self._ShardSerialId = None
        self._ShardInstanceId = None
        self._Status = None
        self._StatusDesc = None
        self._CreateTime = None
        self._VpcId = None
        self._SubnetId = None
        self._ProjectId = None
        self._Region = None
        self._Zone = None
        self._Memory = None
        self._Storage = None
        self._PeriodEndTime = None
        self._NodeCount = None
        self._StorageUsage = None
        self._MemoryUsage = None
        self._ShardId = None
        self._Pid = None
        self._ProxyVersion = None
        self._Paymode = None
        self._ShardMasterZone = None
        self._ShardSlaveZones = None
        self._Cpu = None
        self._Range = None

    @property
    def InstanceId(self):
        """所属实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ShardSerialId(self):
        """分片SQL透传Id，用于将sql透传到指定分片执行
        :rtype: str
        """
        return self._ShardSerialId

    @ShardSerialId.setter
    def ShardSerialId(self, ShardSerialId):
        self._ShardSerialId = ShardSerialId

    @property
    def ShardInstanceId(self):
        """全局唯一的分片Id
        :rtype: str
        """
        return self._ShardInstanceId

    @ShardInstanceId.setter
    def ShardInstanceId(self, ShardInstanceId):
        self._ShardInstanceId = ShardInstanceId

    @property
    def Status(self):
        """状态：0 创建中，1 流程处理中， 2 运行中，3 分片未初始化
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        """状态中文描述
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def VpcId(self):
        """字符串格式的私有网络Id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """字符串格式的私有网络子网Id
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ProjectId(self):
        """项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Region(self):
        """地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Memory(self):
        """内存大小，单位 GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        """存储大小，单位 GB
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def PeriodEndTime(self):
        """到期时间
        :rtype: str
        """
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def NodeCount(self):
        """节点数，2 为一主一从， 3 为一主二从
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def StorageUsage(self):
        """存储使用率，单位为 %
        :rtype: float
        """
        return self._StorageUsage

    @StorageUsage.setter
    def StorageUsage(self, StorageUsage):
        self._StorageUsage = StorageUsage

    @property
    def MemoryUsage(self):
        """内存使用率，单位为 %
        :rtype: float
        """
        return self._MemoryUsage

    @MemoryUsage.setter
    def MemoryUsage(self, MemoryUsage):
        self._MemoryUsage = MemoryUsage

    @property
    def ShardId(self):
        """数字分片Id（过时字段，请勿依赖该值）
        :rtype: int
        """
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def Pid(self):
        """产品ProductID
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def ProxyVersion(self):
        """Proxy版本
        :rtype: str
        """
        return self._ProxyVersion

    @ProxyVersion.setter
    def ProxyVersion(self, ProxyVersion):
        self._ProxyVersion = ProxyVersion

    @property
    def Paymode(self):
        """付费模型
        :rtype: str
        """
        return self._Paymode

    @Paymode.setter
    def Paymode(self, Paymode):
        self._Paymode = Paymode

    @property
    def ShardMasterZone(self):
        """分片的主可用区
        :rtype: str
        """
        return self._ShardMasterZone

    @ShardMasterZone.setter
    def ShardMasterZone(self, ShardMasterZone):
        self._ShardMasterZone = ShardMasterZone

    @property
    def ShardSlaveZones(self):
        """分片的从可用区列表
        :rtype: list of str
        """
        return self._ShardSlaveZones

    @ShardSlaveZones.setter
    def ShardSlaveZones(self, ShardSlaveZones):
        self._ShardSlaveZones = ShardSlaveZones

    @property
    def Cpu(self):
        """CPU核数
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Range(self):
        """分片ShardKey的范围（总共64个哈希值），例如： 0-31，32-63
        :rtype: str
        """
        return self._Range

    @Range.setter
    def Range(self, Range):
        self._Range = Range


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ShardSerialId = params.get("ShardSerialId")
        self._ShardInstanceId = params.get("ShardInstanceId")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._CreateTime = params.get("CreateTime")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ProjectId = params.get("ProjectId")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._NodeCount = params.get("NodeCount")
        self._StorageUsage = params.get("StorageUsage")
        self._MemoryUsage = params.get("MemoryUsage")
        self._ShardId = params.get("ShardId")
        self._Pid = params.get("Pid")
        self._ProxyVersion = params.get("ProxyVersion")
        self._Paymode = params.get("Paymode")
        self._ShardMasterZone = params.get("ShardMasterZone")
        self._ShardSlaveZones = params.get("ShardSlaveZones")
        self._Cpu = params.get("Cpu")
        self._Range = params.get("Range")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDLDetail(AbstractModel):
    """DDL任务执行详情

    """

    def __init__(self):
        r"""
        :param _ShardSerialId: 分片Id
        :type ShardSerialId: str
        :param _DbName: 数据库
        :type DbName: str
        :param _Table: 表
        :type Table: str
        :param _Alter: 执行的DDL任务内容
        :type Alter: str
        :param _BeginTime: 开始执行时间
        :type BeginTime: str
        :param _Status: 当前任务状态。0 成功； 1失败；  2进行中
        :type Status: int
        :param _Desc: 任务详细描述信息
        :type Desc: str
        :param _Stage: 任务当前所处阶段
        :type Stage: str
        :param _SwitchStatus: 切换状态：1: 未到切换阶段；2：正在等待进行表切换；3: 正在进行切换；4: 切换成功；5: 切换失败
        :type SwitchStatus: int
        """
        self._ShardSerialId = None
        self._DbName = None
        self._Table = None
        self._Alter = None
        self._BeginTime = None
        self._Status = None
        self._Desc = None
        self._Stage = None
        self._SwitchStatus = None

    @property
    def ShardSerialId(self):
        """分片Id
        :rtype: str
        """
        return self._ShardSerialId

    @ShardSerialId.setter
    def ShardSerialId(self, ShardSerialId):
        self._ShardSerialId = ShardSerialId

    @property
    def DbName(self):
        """数据库
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Table(self):
        """表
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Alter(self):
        """执行的DDL任务内容
        :rtype: str
        """
        return self._Alter

    @Alter.setter
    def Alter(self, Alter):
        self._Alter = Alter

    @property
    def BeginTime(self):
        """开始执行时间
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def Status(self):
        """当前任务状态。0 成功； 1失败；  2进行中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Desc(self):
        """任务详细描述信息
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Stage(self):
        """任务当前所处阶段
        :rtype: str
        """
        return self._Stage

    @Stage.setter
    def Stage(self, Stage):
        self._Stage = Stage

    @property
    def SwitchStatus(self):
        """切换状态：1: 未到切换阶段；2：正在等待进行表切换；3: 正在进行切换；4: 切换成功；5: 切换失败
        :rtype: int
        """
        return self._SwitchStatus

    @SwitchStatus.setter
    def SwitchStatus(self, SwitchStatus):
        self._SwitchStatus = SwitchStatus


    def _deserialize(self, params):
        self._ShardSerialId = params.get("ShardSerialId")
        self._DbName = params.get("DbName")
        self._Table = params.get("Table")
        self._Alter = params.get("Alter")
        self._BeginTime = params.get("BeginTime")
        self._Status = params.get("Status")
        self._Desc = params.get("Desc")
        self._Stage = params.get("Stage")
        self._SwitchStatus = params.get("SwitchStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Database(AbstractModel):
    """数据库信息

    """

    def __init__(self):
        r"""
        :param _DbName: 数据库名称
        :type DbName: str
        """
        self._DbName = None

    @property
    def DbName(self):
        """数据库名称
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseFunction(AbstractModel):
    """数据库函数信息

    """

    def __init__(self):
        r"""
        :param _Func: 函数名称
        :type Func: str
        """
        self._Func = None

    @property
    def Func(self):
        """函数名称
        :rtype: str
        """
        return self._Func

    @Func.setter
    def Func(self, Func):
        self._Func = Func


    def _deserialize(self, params):
        self._Func = params.get("Func")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabasePrivilege(AbstractModel):
    """数据库权限

    """

    def __init__(self):
        r"""
        :param _Privileges: 权限信息
        :type Privileges: list of str
        :param _Database: 数据库名
        :type Database: str
        """
        self._Privileges = None
        self._Database = None

    @property
    def Privileges(self):
        """权限信息
        :rtype: list of str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges

    @property
    def Database(self):
        """数据库名
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database


    def _deserialize(self, params):
        self._Privileges = params.get("Privileges")
        self._Database = params.get("Database")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseProcedure(AbstractModel):
    """数据库存储过程信息

    """

    def __init__(self):
        r"""
        :param _Proc: 存储过程名称
        :type Proc: str
        """
        self._Proc = None

    @property
    def Proc(self):
        """存储过程名称
        :rtype: str
        """
        return self._Proc

    @Proc.setter
    def Proc(self, Proc):
        self._Proc = Proc


    def _deserialize(self, params):
        self._Proc = params.get("Proc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseTable(AbstractModel):
    """数据库表信息

    """

    def __init__(self):
        r"""
        :param _Table: 表名
        :type Table: str
        """
        self._Table = None

    @property
    def Table(self):
        """表名
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table


    def _deserialize(self, params):
        self._Table = params.get("Table")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseView(AbstractModel):
    """数据库视图信息

    """

    def __init__(self):
        r"""
        :param _View: 视图名称
        :type View: str
        """
        self._View = None

    @property
    def View(self):
        """视图名称
        :rtype: str
        """
        return self._View

    @View.setter
    def View(self, View):
        self._View = View


    def _deserialize(self, params):
        self._View = params.get("View")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DcnDetailItem(AbstractModel):
    """DCN详情条目

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _Region: 实例地域
        :type Region: str
        :param _Zone: 实例可用区
        :type Zone: str
        :param _Vip: 实例IP地址
        :type Vip: str
        :param _Vipv6: 实例IPv6地址
        :type Vipv6: str
        :param _Vport: 实例端口
        :type Vport: int
        :param _Status: 实例状态
        :type Status: int
        :param _StatusDesc: 实例状态描述
        :type StatusDesc: str
        :param _DcnFlag: 实例DCN标志，1-主，2-备
        :type DcnFlag: int
        :param _DcnStatus: 实例DCN状态，0-无，1-创建中，2-同步中，3-已断开
        :type DcnStatus: int
        :param _Cpu: 实例CPU核数
        :type Cpu: int
        :param _Memory: 实例内存大小，单位 GB
        :type Memory: int
        :param _Storage: 实例存储大小，单位 GB
        :type Storage: int
        :param _PayMode: 付费模式
        :type PayMode: int
        :param _CreateTime: 实例创建时间，格式为 2006-01-02 15:04:05
        :type CreateTime: str
        :param _PeriodEndTime: 实例到期时间，格式为 2006-01-02 15:04:05
        :type PeriodEndTime: str
        :param _InstanceType: 1： 主实例（独享型）, 2: 主实例, 3： 灾备实例, 4： 灾备实例（独享型）
        :type InstanceType: int
        :param _EncryptStatus: 是否开启了 kms
        :type EncryptStatus: int
        :param _DcnStatusDesc: 实例DCN状态描述信息
        :type DcnStatusDesc: str
        :param _PolarisInstanceId: DCN实例绑定的北极星服务所属的北极星实例Id，若未绑定则为空
        :type PolarisInstanceId: str
        :param _PolarisInstanceName: DCN实例绑定的北极星服务所属的北极星实例名，若未绑定则为空
        :type PolarisInstanceName: str
        :param _PolarisNamespace: DCN实例绑定的北极星服务所属的北极星命名空间，若未绑定则为空
        :type PolarisNamespace: str
        :param _PolarisService: DCN实例绑定的北极星服务，若未绑定则为空
        :type PolarisService: str
        :param _PolarisServiceStatus: DCN实例在北极星服务中的状态 0:未开启; 1:已开启; 2:已隔离; 3:切换中
        :type PolarisServiceStatus: int
        :param _PolarisServiceStatusDesc: DCN实例在北极星服务中的状态的描述信息
        :type PolarisServiceStatusDesc: str
        :param _PolarisRegion: 北极星管控地域
        :type PolarisRegion: str
        :param _IsDcnSwitchSupported: 是否支持DCN切换
        :type IsDcnSwitchSupported: int
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Region = None
        self._Zone = None
        self._Vip = None
        self._Vipv6 = None
        self._Vport = None
        self._Status = None
        self._StatusDesc = None
        self._DcnFlag = None
        self._DcnStatus = None
        self._Cpu = None
        self._Memory = None
        self._Storage = None
        self._PayMode = None
        self._CreateTime = None
        self._PeriodEndTime = None
        self._InstanceType = None
        self._EncryptStatus = None
        self._DcnStatusDesc = None
        self._PolarisInstanceId = None
        self._PolarisInstanceName = None
        self._PolarisNamespace = None
        self._PolarisService = None
        self._PolarisServiceStatus = None
        self._PolarisServiceStatusDesc = None
        self._PolarisRegion = None
        self._IsDcnSwitchSupported = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Region(self):
        """实例地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """实例可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Vip(self):
        """实例IP地址
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vipv6(self):
        """实例IPv6地址
        :rtype: str
        """
        return self._Vipv6

    @Vipv6.setter
    def Vipv6(self, Vipv6):
        self._Vipv6 = Vipv6

    @property
    def Vport(self):
        """实例端口
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Status(self):
        """实例状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        """实例状态描述
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def DcnFlag(self):
        """实例DCN标志，1-主，2-备
        :rtype: int
        """
        return self._DcnFlag

    @DcnFlag.setter
    def DcnFlag(self, DcnFlag):
        self._DcnFlag = DcnFlag

    @property
    def DcnStatus(self):
        """实例DCN状态，0-无，1-创建中，2-同步中，3-已断开
        :rtype: int
        """
        return self._DcnStatus

    @DcnStatus.setter
    def DcnStatus(self, DcnStatus):
        self._DcnStatus = DcnStatus

    @property
    def Cpu(self):
        """实例CPU核数
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """实例内存大小，单位 GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        """实例存储大小，单位 GB
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def PayMode(self):
        """付费模式
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def CreateTime(self):
        """实例创建时间，格式为 2006-01-02 15:04:05
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def PeriodEndTime(self):
        """实例到期时间，格式为 2006-01-02 15:04:05
        :rtype: str
        """
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def InstanceType(self):
        """1： 主实例（独享型）, 2: 主实例, 3： 灾备实例, 4： 灾备实例（独享型）
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def EncryptStatus(self):
        """是否开启了 kms
        :rtype: int
        """
        return self._EncryptStatus

    @EncryptStatus.setter
    def EncryptStatus(self, EncryptStatus):
        self._EncryptStatus = EncryptStatus

    @property
    def DcnStatusDesc(self):
        """实例DCN状态描述信息
        :rtype: str
        """
        return self._DcnStatusDesc

    @DcnStatusDesc.setter
    def DcnStatusDesc(self, DcnStatusDesc):
        self._DcnStatusDesc = DcnStatusDesc

    @property
    def PolarisInstanceId(self):
        """DCN实例绑定的北极星服务所属的北极星实例Id，若未绑定则为空
        :rtype: str
        """
        return self._PolarisInstanceId

    @PolarisInstanceId.setter
    def PolarisInstanceId(self, PolarisInstanceId):
        self._PolarisInstanceId = PolarisInstanceId

    @property
    def PolarisInstanceName(self):
        """DCN实例绑定的北极星服务所属的北极星实例名，若未绑定则为空
        :rtype: str
        """
        return self._PolarisInstanceName

    @PolarisInstanceName.setter
    def PolarisInstanceName(self, PolarisInstanceName):
        self._PolarisInstanceName = PolarisInstanceName

    @property
    def PolarisNamespace(self):
        """DCN实例绑定的北极星服务所属的北极星命名空间，若未绑定则为空
        :rtype: str
        """
        return self._PolarisNamespace

    @PolarisNamespace.setter
    def PolarisNamespace(self, PolarisNamespace):
        self._PolarisNamespace = PolarisNamespace

    @property
    def PolarisService(self):
        """DCN实例绑定的北极星服务，若未绑定则为空
        :rtype: str
        """
        return self._PolarisService

    @PolarisService.setter
    def PolarisService(self, PolarisService):
        self._PolarisService = PolarisService

    @property
    def PolarisServiceStatus(self):
        """DCN实例在北极星服务中的状态 0:未开启; 1:已开启; 2:已隔离; 3:切换中
        :rtype: int
        """
        return self._PolarisServiceStatus

    @PolarisServiceStatus.setter
    def PolarisServiceStatus(self, PolarisServiceStatus):
        self._PolarisServiceStatus = PolarisServiceStatus

    @property
    def PolarisServiceStatusDesc(self):
        """DCN实例在北极星服务中的状态的描述信息
        :rtype: str
        """
        return self._PolarisServiceStatusDesc

    @PolarisServiceStatusDesc.setter
    def PolarisServiceStatusDesc(self, PolarisServiceStatusDesc):
        self._PolarisServiceStatusDesc = PolarisServiceStatusDesc

    @property
    def PolarisRegion(self):
        """北极星管控地域
        :rtype: str
        """
        return self._PolarisRegion

    @PolarisRegion.setter
    def PolarisRegion(self, PolarisRegion):
        self._PolarisRegion = PolarisRegion

    @property
    def IsDcnSwitchSupported(self):
        """是否支持DCN切换
        :rtype: int
        """
        return self._IsDcnSwitchSupported

    @IsDcnSwitchSupported.setter
    def IsDcnSwitchSupported(self, IsDcnSwitchSupported):
        self._IsDcnSwitchSupported = IsDcnSwitchSupported


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._Vip = params.get("Vip")
        self._Vipv6 = params.get("Vipv6")
        self._Vport = params.get("Vport")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._DcnFlag = params.get("DcnFlag")
        self._DcnStatus = params.get("DcnStatus")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._PayMode = params.get("PayMode")
        self._CreateTime = params.get("CreateTime")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._InstanceType = params.get("InstanceType")
        self._EncryptStatus = params.get("EncryptStatus")
        self._DcnStatusDesc = params.get("DcnStatusDesc")
        self._PolarisInstanceId = params.get("PolarisInstanceId")
        self._PolarisInstanceName = params.get("PolarisInstanceName")
        self._PolarisNamespace = params.get("PolarisNamespace")
        self._PolarisService = params.get("PolarisService")
        self._PolarisServiceStatus = params.get("PolarisServiceStatus")
        self._PolarisServiceStatusDesc = params.get("PolarisServiceStatusDesc")
        self._PolarisRegion = params.get("PolarisRegion")
        self._IsDcnSwitchSupported = params.get("IsDcnSwitchSupported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Deal(AbstractModel):
    """订单信息

    """

    def __init__(self):
        r"""
        :param _DealName: 订单号
        :type DealName: str
        :param _OwnerUin: 所属账号
        :type OwnerUin: str
        :param _Count: 商品数量
        :type Count: int
        :param _FlowId: 关联的流程 Id，可用于查询流程执行状态
        :type FlowId: int
        :param _InstanceIds: 只有创建实例且已完成发货的订单会填充该字段，表示该订单创建的实例的 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceIds: list of str
        :param _PayMode: 付费模式，0后付费/1预付费
        :type PayMode: int
        """
        self._DealName = None
        self._OwnerUin = None
        self._Count = None
        self._FlowId = None
        self._InstanceIds = None
        self._PayMode = None

    @property
    def DealName(self):
        """订单号
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def OwnerUin(self):
        """所属账号
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Count(self):
        """商品数量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def FlowId(self):
        """关联的流程 Id，可用于查询流程执行状态
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceIds(self):
        """只有创建实例且已完成发货的订单会填充该字段，表示该订单创建的实例的 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def PayMode(self):
        """付费模式，0后付费/1预付费
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._OwnerUin = params.get("OwnerUin")
        self._Count = params.get("Count")
        self._FlowId = params.get("FlowId")
        self._InstanceIds = params.get("InstanceIds")
        self._PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountRequest(AbstractModel):
    """DeleteAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param _UserName: 用户名
        :type UserName: str
        :param _Host: 用户允许的访问 host
        :type Host: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Host = None

    @property
    def InstanceId(self):
        """实例ID，形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        """用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        """用户允许的访问 host
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountResponse(AbstractModel):
    """DeleteAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAccountPrivilegesRequest(AbstractModel):
    """DescribeAccountPrivileges请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：dcdbt-ow7t8lmc。
        :type InstanceId: str
        :param _UserName: 登录用户名。
        :type UserName: str
        :param _Host: 用户允许的访问 host，用户名+host唯一确定一个账号。
        :type Host: str
        :param _DbName: 数据库名。如果为 \*，表示查询全局权限（即 \*.\*），此时忽略 Type 和 Object 参数
        :type DbName: str
        :param _Type: 类型,可以填入 table 、 view 、 proc 、 func 和 \*。当 DbName 为具体数据库名，Type为 \* 时，表示查询该数据库权限（即db.\*），此时忽略 Object 参数
        :type Type: str
        :param _Object: 具体的 Type 的名称，例如 Type 为 table 时就是具体的表名。DbName 和 Type 都为具体名称，则 Object 表示具体对象名，不能为 \* 或者为空
        :type Object: str
        :param _ColName: 当 Type=table 时，ColName 为 \* 表示查询表的权限，如果为具体字段名，表示查询对应字段的权限
        :type ColName: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Host = None
        self._DbName = None
        self._Type = None
        self._Object = None
        self._ColName = None

    @property
    def InstanceId(self):
        """实例 ID，形如：dcdbt-ow7t8lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        """登录用户名。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        """用户允许的访问 host，用户名+host唯一确定一个账号。
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def DbName(self):
        """数据库名。如果为 \*，表示查询全局权限（即 \*.\*），此时忽略 Type 和 Object 参数
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Type(self):
        """类型,可以填入 table 、 view 、 proc 、 func 和 \*。当 DbName 为具体数据库名，Type为 \* 时，表示查询该数据库权限（即db.\*），此时忽略 Object 参数
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Object(self):
        """具体的 Type 的名称，例如 Type 为 table 时就是具体的表名。DbName 和 Type 都为具体名称，则 Object 表示具体对象名，不能为 \* 或者为空
        :rtype: str
        """
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object

    @property
    def ColName(self):
        """当 Type=table 时，ColName 为 \* 表示查询表的权限，如果为具体字段名，表示查询对应字段的权限
        :rtype: str
        """
        return self._ColName

    @ColName.setter
    def ColName(self, ColName):
        self._ColName = ColName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._DbName = params.get("DbName")
        self._Type = params.get("Type")
        self._Object = params.get("Object")
        self._ColName = params.get("ColName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountPrivilegesResponse(AbstractModel):
    """DescribeAccountPrivileges返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Privileges: 权限列表。
        :type Privileges: list of str
        :param _UserName: 数据库账号用户名
        :type UserName: str
        :param _Host: 数据库账号Host
        :type Host: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._Privileges = None
        self._UserName = None
        self._Host = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Privileges(self):
        """权限列表。
        :rtype: list of str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges

    @property
    def UserName(self):
        """数据库账号用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        """数据库账号Host
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Privileges = params.get("Privileges")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例ID，形如：dcdbt-ow728lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，透传入参。
        :type InstanceId: str
        :param _Users: 实例用户列表。
        :type Users: list of DBAccount
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._Users = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """实例ID，透传入参。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Users(self):
        """实例用户列表。
        :rtype: list of DBAccount
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = DBAccount()
                obj._deserialize(item)
                self._Users.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupConfigsRequest(AbstractModel):
    """DescribeBackupConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：tdsqlshard-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例 ID，格式如：tdsqlshard-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupConfigsResponse(AbstractModel):
    """DescribeBackupConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _Days: 常规备份存储时长，范围[1, 3650]。
        :type Days: int
        :param _StartBackupTime: 每天备份执行的区间的开始时间，格式 mm:ss，形如 22:00。
        :type StartBackupTime: str
        :param _EndBackupTime: 每天备份执行的区间的结束时间，格式 mm:ss，形如 23:59。
        :type EndBackupTime: str
        :param _WeekDays: 执行备份周期，枚举值：Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday
        :type WeekDays: list of str
        :param _ArchiveDays: 沉降到归档存储时长，-1表示关闭归档设置。
        :type ArchiveDays: int
        :param _BackupConfigSet: 超期备份配置。
        :type BackupConfigSet: list of BackupConfig
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._Days = None
        self._StartBackupTime = None
        self._EndBackupTime = None
        self._WeekDays = None
        self._ArchiveDays = None
        self._BackupConfigSet = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Days(self):
        """常规备份存储时长，范围[1, 3650]。
        :rtype: int
        """
        return self._Days

    @Days.setter
    def Days(self, Days):
        self._Days = Days

    @property
    def StartBackupTime(self):
        """每天备份执行的区间的开始时间，格式 mm:ss，形如 22:00。
        :rtype: str
        """
        return self._StartBackupTime

    @StartBackupTime.setter
    def StartBackupTime(self, StartBackupTime):
        self._StartBackupTime = StartBackupTime

    @property
    def EndBackupTime(self):
        """每天备份执行的区间的结束时间，格式 mm:ss，形如 23:59。
        :rtype: str
        """
        return self._EndBackupTime

    @EndBackupTime.setter
    def EndBackupTime(self, EndBackupTime):
        self._EndBackupTime = EndBackupTime

    @property
    def WeekDays(self):
        """执行备份周期，枚举值：Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday
        :rtype: list of str
        """
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays

    @property
    def ArchiveDays(self):
        """沉降到归档存储时长，-1表示关闭归档设置。
        :rtype: int
        """
        return self._ArchiveDays

    @ArchiveDays.setter
    def ArchiveDays(self, ArchiveDays):
        self._ArchiveDays = ArchiveDays

    @property
    def BackupConfigSet(self):
        """超期备份配置。
        :rtype: list of BackupConfig
        """
        return self._BackupConfigSet

    @BackupConfigSet.setter
    def BackupConfigSet(self, BackupConfigSet):
        self._BackupConfigSet = BackupConfigSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Days = params.get("Days")
        self._StartBackupTime = params.get("StartBackupTime")
        self._EndBackupTime = params.get("EndBackupTime")
        self._WeekDays = params.get("WeekDays")
        self._ArchiveDays = params.get("ArchiveDays")
        if params.get("BackupConfigSet") is not None:
            self._BackupConfigSet = []
            for item in params.get("BackupConfigSet"):
                obj = BackupConfig()
                obj._deserialize(item)
                self._BackupConfigSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupFilesRequest(AbstractModel):
    """DescribeBackupFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 按实例ID查询
        :type InstanceId: str
        :param _ShardId: 按分片ID查询
        :type ShardId: str
        :param _BackupType: 备份类型，Data:数据备份，Binlog:Binlog备份，Errlog:错误日志，Slowlog:慢日志
        :type BackupType: str
        :param _StartTime: 按开始时间查询
        :type StartTime: str
        :param _EndTime: 按结束时间查询
        :type EndTime: str
        :param _Limit: 分页参数
        :type Limit: int
        :param _Offset: 分页参数
        :type Offset: int
        :param _OrderBy: 排序参数，可选值：Time,Size
        :type OrderBy: str
        :param _OrderType: 排序参数，可选值：DESC,ASC
        :type OrderType: str
        """
        self._InstanceId = None
        self._ShardId = None
        self._BackupType = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderType = None

    @property
    def InstanceId(self):
        """按实例ID查询
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ShardId(self):
        """按分片ID查询
        :rtype: str
        """
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def BackupType(self):
        """备份类型，Data:数据备份，Binlog:Binlog备份，Errlog:错误日志，Slowlog:慢日志
        :rtype: str
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def StartTime(self):
        """按开始时间查询
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """按结束时间查询
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        """分页参数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页参数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        """排序参数，可选值：Time,Size
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderType(self):
        """排序参数，可选值：DESC,ASC
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ShardId = params.get("ShardId")
        self._BackupType = params.get("BackupType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderType = params.get("OrderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupFilesResponse(AbstractModel):
    """DescribeBackupFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Files: 备份文件列表
        :type Files: list of InstanceBackupFileItem
        :param _TotalCount: 总条目数
        :type TotalCount: int
        :param _UrlPrefix: 下载链接前缀
        :type UrlPrefix: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Files = None
        self._TotalCount = None
        self._UrlPrefix = None
        self._RequestId = None

    @property
    def Files(self):
        """备份文件列表
        :rtype: list of InstanceBackupFileItem
        """
        return self._Files

    @Files.setter
    def Files(self, Files):
        self._Files = Files

    @property
    def TotalCount(self):
        """总条目数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def UrlPrefix(self):
        """下载链接前缀
        :rtype: str
        """
        return self._UrlPrefix

    @UrlPrefix.setter
    def UrlPrefix(self, UrlPrefix):
        self._UrlPrefix = UrlPrefix

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Files") is not None:
            self._Files = []
            for item in params.get("Files"):
                obj = InstanceBackupFileItem()
                obj._deserialize(item)
                self._Files.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._UrlPrefix = params.get("UrlPrefix")
        self._RequestId = params.get("RequestId")


class DescribeDBEncryptAttributesRequest(AbstractModel):
    """DescribeDBEncryptAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id，形如：tdsqlshard-ow728lmc。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例Id，形如：tdsqlshard-ow728lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBEncryptAttributesResponse(AbstractModel):
    """DescribeDBEncryptAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EncryptStatus: 是否启用加密，1-已开启；0-未开启。
        :type EncryptStatus: int
        :param _CipherText: DEK密钥
        :type CipherText: str
        :param _ExpireDate: DEK密钥过期日期。
        :type ExpireDate: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EncryptStatus = None
        self._CipherText = None
        self._ExpireDate = None
        self._RequestId = None

    @property
    def EncryptStatus(self):
        """是否启用加密，1-已开启；0-未开启。
        :rtype: int
        """
        return self._EncryptStatus

    @EncryptStatus.setter
    def EncryptStatus(self, EncryptStatus):
        self._EncryptStatus = EncryptStatus

    @property
    def CipherText(self):
        """DEK密钥
        :rtype: str
        """
        return self._CipherText

    @CipherText.setter
    def CipherText(self, CipherText):
        self._CipherText = CipherText

    @property
    def ExpireDate(self):
        """DEK密钥过期日期。
        :rtype: str
        """
        return self._ExpireDate

    @ExpireDate.setter
    def ExpireDate(self, ExpireDate):
        self._ExpireDate = ExpireDate

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EncryptStatus = params.get("EncryptStatus")
        self._CipherText = params.get("CipherText")
        self._ExpireDate = params.get("ExpireDate")
        self._RequestId = params.get("RequestId")


class DescribeDBLogFilesRequest(AbstractModel):
    """DescribeDBLogFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：dcdbt-ow7t8lmc。
        :type InstanceId: str
        :param _ShardId: 分片 ID，形如：shard-7noic7tv
        :type ShardId: str
        :param _Type: 请求日志类型，取值只能为1、2、3或者4。1-binlog，2-冷备，3-errlog，4-slowlog。
        :type Type: int
        """
        self._InstanceId = None
        self._ShardId = None
        self._Type = None

    @property
    def InstanceId(self):
        """实例 ID，形如：dcdbt-ow7t8lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ShardId(self):
        """分片 ID，形如：shard-7noic7tv
        :rtype: str
        """
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def Type(self):
        """请求日志类型，取值只能为1、2、3或者4。1-binlog，2-冷备，3-errlog，4-slowlog。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ShardId = params.get("ShardId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBLogFilesResponse(AbstractModel):
    """DescribeDBLogFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param _Type: 请求日志类型。1-binlog，2-冷备，3-errlog，4-slowlog。
        :type Type: int
        :param _Total: 请求日志总数
        :type Total: int
        :param _Files: 日志文件列表
        :type Files: list of LogFileInfo
        :param _VpcPrefix: 如果是VPC网络的实例，做用本前缀加上URI为下载地址
        :type VpcPrefix: str
        :param _NormalPrefix: 如果是普通网络的实例，做用本前缀加上URI为下载地址
        :type NormalPrefix: str
        :param _ShardId: 分片 ID，形如：shard-7noic7tv
        :type ShardId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._Type = None
        self._Total = None
        self._Files = None
        self._VpcPrefix = None
        self._NormalPrefix = None
        self._ShardId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """实例 ID，形如：dcdbt-ow728lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        """请求日志类型。1-binlog，2-冷备，3-errlog，4-slowlog。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Total(self):
        """请求日志总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Files(self):
        """日志文件列表
        :rtype: list of LogFileInfo
        """
        return self._Files

    @Files.setter
    def Files(self, Files):
        self._Files = Files

    @property
    def VpcPrefix(self):
        """如果是VPC网络的实例，做用本前缀加上URI为下载地址
        :rtype: str
        """
        return self._VpcPrefix

    @VpcPrefix.setter
    def VpcPrefix(self, VpcPrefix):
        self._VpcPrefix = VpcPrefix

    @property
    def NormalPrefix(self):
        """如果是普通网络的实例，做用本前缀加上URI为下载地址
        :rtype: str
        """
        return self._NormalPrefix

    @NormalPrefix.setter
    def NormalPrefix(self, NormalPrefix):
        self._NormalPrefix = NormalPrefix

    @property
    def ShardId(self):
        """分片 ID，形如：shard-7noic7tv
        :rtype: str
        """
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
        self._Total = params.get("Total")
        if params.get("Files") is not None:
            self._Files = []
            for item in params.get("Files"):
                obj = LogFileInfo()
                obj._deserialize(item)
                self._Files.append(obj)
        self._VpcPrefix = params.get("VpcPrefix")
        self._NormalPrefix = params.get("NormalPrefix")
        self._ShardId = params.get("ShardId")
        self._RequestId = params.get("RequestId")


class DescribeDBParametersRequest(AbstractModel):
    """DescribeDBParameters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：dcdbt-ow7t8lmc。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例 ID，形如：dcdbt-ow7t8lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBParametersResponse(AbstractModel):
    """DescribeDBParameters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：dcdbt-ow7t8lmc。
        :type InstanceId: str
        :param _Params: 请求DB的当前参数值
        :type Params: list of ParamDesc
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._Params = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """实例 ID，形如：dcdbt-ow7t8lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Params(self):
        """请求DB的当前参数值
        :rtype: list of ParamDesc
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Params") is not None:
            self._Params = []
            for item in params.get("Params"):
                obj = ParamDesc()
                obj._deserialize(item)
                self._Params.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 数据库引擎名称，本接口取值：dcdb。
        :type Product: str
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        """
        self._Product = None
        self._InstanceId = None

    @property
    def Product(self):
        """数据库引擎名称，本接口取值：dcdb。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSecurityGroupsResponse(AbstractModel):
    """DescribeDBSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Groups: 安全组详情。
        :type Groups: list of SecurityGroup
        :param _VIP: 实例VIP
        :type VIP: str
        :param _VPort: 实例端口
        :type VPort: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Groups = None
        self._VIP = None
        self._VPort = None
        self._RequestId = None

    @property
    def Groups(self):
        """安全组详情。
        :rtype: list of SecurityGroup
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def VIP(self):
        """实例VIP
        :rtype: str
        """
        return self._VIP

    @VIP.setter
    def VIP(self, VIP):
        self._VIP = VIP

    @property
    def VPort(self):
        """实例端口
        :rtype: str
        """
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._VIP = params.get("VIP")
        self._VPort = params.get("VPort")
        self._RequestId = params.get("RequestId")


class DescribeDBSlowLogsRequest(AbstractModel):
    """DescribeDBSlowLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：dcdbt-hw0qj6m1
        :type InstanceId: str
        :param _Offset: 从结果的第几条数据开始返回
        :type Offset: int
        :param _Limit: 返回的结果条数
        :type Limit: int
        :param _StartTime: 查询的起始时间，形如2016-07-23 14:55:20
        :type StartTime: str
        :param _ShardId: 实例的分片ID，形如shard-53ima8ln
        :type ShardId: str
        :param _EndTime: 查询的结束时间，形如2016-08-22 14:55:20。如果不填，那么查询结束时间就是当前时间
        :type EndTime: str
        :param _Db: 要查询的具体数据库名称
        :type Db: str
        :param _OrderBy: 排序指标，取值为query_time_sum或者query_count。不填默认按照query_time_sum排序
        :type OrderBy: str
        :param _OrderByType: 排序类型，desc（降序）或者asc（升序）。不填默认desc排序
        :type OrderByType: str
        :param _Slave: 是否查询从机的慢查询，0-主机; 1-从机。不填默认查询主机慢查询
        :type Slave: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._StartTime = None
        self._ShardId = None
        self._EndTime = None
        self._Db = None
        self._OrderBy = None
        self._OrderByType = None
        self._Slave = None

    @property
    def InstanceId(self):
        """实例 ID，形如：dcdbt-hw0qj6m1
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        """从结果的第几条数据开始返回
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回的结果条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def StartTime(self):
        """查询的起始时间，形如2016-07-23 14:55:20
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ShardId(self):
        """实例的分片ID，形如shard-53ima8ln
        :rtype: str
        """
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def EndTime(self):
        """查询的结束时间，形如2016-08-22 14:55:20。如果不填，那么查询结束时间就是当前时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Db(self):
        """要查询的具体数据库名称
        :rtype: str
        """
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def OrderBy(self):
        """排序指标，取值为query_time_sum或者query_count。不填默认按照query_time_sum排序
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        """排序类型，desc（降序）或者asc（升序）。不填默认desc排序
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Slave(self):
        """是否查询从机的慢查询，0-主机; 1-从机。不填默认查询主机慢查询
        :rtype: int
        """
        return self._Slave

    @Slave.setter
    def Slave(self, Slave):
        self._Slave = Slave


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._StartTime = params.get("StartTime")
        self._ShardId = params.get("ShardId")
        self._EndTime = params.get("EndTime")
        self._Db = params.get("Db")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._Slave = params.get("Slave")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSlowLogsResponse(AbstractModel):
    """DescribeDBSlowLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LockTimeSum: 所有语句锁时间总和
        :type LockTimeSum: float
        :param _QueryCount: 所有语句查询总次数
        :type QueryCount: int
        :param _Total: 总记录数
        :type Total: int
        :param _QueryTimeSum: 所有语句查询时间总和
        :type QueryTimeSum: float
        :param _Data: 慢查询日志数据
        :type Data: list of SlowLogData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LockTimeSum = None
        self._QueryCount = None
        self._Total = None
        self._QueryTimeSum = None
        self._Data = None
        self._RequestId = None

    @property
    def LockTimeSum(self):
        """所有语句锁时间总和
        :rtype: float
        """
        return self._LockTimeSum

    @LockTimeSum.setter
    def LockTimeSum(self, LockTimeSum):
        self._LockTimeSum = LockTimeSum

    @property
    def QueryCount(self):
        """所有语句查询总次数
        :rtype: int
        """
        return self._QueryCount

    @QueryCount.setter
    def QueryCount(self, QueryCount):
        self._QueryCount = QueryCount

    @property
    def Total(self):
        """总记录数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def QueryTimeSum(self):
        """所有语句查询时间总和
        :rtype: float
        """
        return self._QueryTimeSum

    @QueryTimeSum.setter
    def QueryTimeSum(self, QueryTimeSum):
        self._QueryTimeSum = QueryTimeSum

    @property
    def Data(self):
        """慢查询日志数据
        :rtype: list of SlowLogData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LockTimeSum = params.get("LockTimeSum")
        self._QueryCount = params.get("QueryCount")
        self._Total = params.get("Total")
        self._QueryTimeSum = params.get("QueryTimeSum")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SlowLogData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBSyncModeRequest(AbstractModel):
    """DescribeDBSyncMode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 待修改同步模式的实例ID。形如：dcdbt-ow728lmc。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """待修改同步模式的实例ID。形如：dcdbt-ow728lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSyncModeResponse(AbstractModel):
    """DescribeDBSyncMode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SyncMode: 同步模式：0 异步，1 强同步， 2 强同步可退化
        :type SyncMode: int
        :param _IsModifying: 是否有修改流程在执行中：1 是， 0 否。
        :type IsModifying: int
        :param _CurrentSyncMode: 当前复制方式，0 异步，1 同步
        :type CurrentSyncMode: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SyncMode = None
        self._IsModifying = None
        self._CurrentSyncMode = None
        self._RequestId = None

    @property
    def SyncMode(self):
        """同步模式：0 异步，1 强同步， 2 强同步可退化
        :rtype: int
        """
        return self._SyncMode

    @SyncMode.setter
    def SyncMode(self, SyncMode):
        self._SyncMode = SyncMode

    @property
    def IsModifying(self):
        """是否有修改流程在执行中：1 是， 0 否。
        :rtype: int
        """
        return self._IsModifying

    @IsModifying.setter
    def IsModifying(self, IsModifying):
        self._IsModifying = IsModifying

    @property
    def CurrentSyncMode(self):
        """当前复制方式，0 异步，1 同步
        :rtype: int
        """
        return self._CurrentSyncMode

    @CurrentSyncMode.setter
    def CurrentSyncMode(self, CurrentSyncMode):
        self._CurrentSyncMode = CurrentSyncMode

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SyncMode = params.get("SyncMode")
        self._IsModifying = params.get("IsModifying")
        self._CurrentSyncMode = params.get("CurrentSyncMode")
        self._RequestId = params.get("RequestId")


class DescribeDBTmpInstancesRequest(AbstractModel):
    """DescribeDBTmpInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBTmpInstancesResponse(AbstractModel):
    """DescribeDBTmpInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TmpInstances: 临时实例列表
        :type TmpInstances: list of TmpInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TmpInstances = None
        self._RequestId = None

    @property
    def TmpInstances(self):
        """临时实例列表
        :rtype: list of TmpInstance
        """
        return self._TmpInstances

    @TmpInstances.setter
    def TmpInstances(self, TmpInstances):
        self._TmpInstances = TmpInstances

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TmpInstances") is not None:
            self._TmpInstances = []
            for item in params.get("TmpInstances"):
                obj = TmpInstance()
                obj._deserialize(item)
                self._TmpInstances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDCDBBinlogTimeRequest(AbstractModel):
    """DescribeDCDBBinlogTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 需要回档的实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """需要回档的实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDCDBBinlogTimeResponse(AbstractModel):
    """DescribeDCDBBinlogTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StartTime = None
        self._EndTime = None
        self._RequestId = None

    @property
    def StartTime(self):
        """开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RequestId = params.get("RequestId")


class DescribeDCDBInstanceDetailRequest(AbstractModel):
    """DescribeDCDBInstanceDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如dcdbt-7oaxtcb7
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例ID，形如dcdbt-7oaxtcb7
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDCDBInstanceDetailResponse(AbstractModel):
    """DescribeDCDBInstanceDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如dcdbt-7oaxtcb7
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _Status: 实例状态。0-实例创建中；1-异步任务处理中；2-运行中；3-实例未初始化；-1-实例已隔离
        :type Status: int
        :param _StatusDesc: 实例目前运行状态描述
        :type StatusDesc: str
        :param _Vip: 实例内网IP地址
        :type Vip: str
        :param _Vport: 实例内网端口
        :type Vport: int
        :param _NodeCount: 实例节点数。值为2时表示一主一从，值为3时表示一主二从
        :type NodeCount: int
        :param _Region: 实例所在地域名称，形如ap-guangzhou
        :type Region: str
        :param _VpcId: 实例私有网络ID，形如vpc-r9jr0de3
        :type VpcId: str
        :param _SubnetId: 实例私有网络子网ID，形如subnet-6rqs61o2
        :type SubnetId: str
        :param _WanStatus: 外网状态，0-未开通；1-已开通；2-关闭；3-开通中；4-关闭中
        :type WanStatus: int
        :param _WanDomain: 外网访问的域名，公网可解析
        :type WanDomain: str
        :param _WanVip: 外网IP地址，公网可访问
        :type WanVip: str
        :param _WanPort: 外网访问端口
        :type WanPort: int
        :param _ProjectId: 实例所属项目ID
        :type ProjectId: int
        :param _AutoRenewFlag: 实例自动续费标志。0-正常续费；1-自动续费；2-到期不续费
        :type AutoRenewFlag: int
        :param _ExclusterId: 独享集群ID
        :type ExclusterId: str
        :param _PayMode: 付费模式。prepaid-预付费；postpaid-按量计费
        :type PayMode: str
        :param _CreateTime: 实例创建时间，格式为 2006-01-02 15:04:05
        :type CreateTime: str
        :param _PeriodEndTime: 实例到期时间，格式为 2006-01-02 15:04:05
        :type PeriodEndTime: str
        :param _DbVersion: 数据库版本信息
        :type DbVersion: str
        :param _IsAuditSupported: 实例是否支持审计。0-不支持；1-支持
        :type IsAuditSupported: int
        :param _IsEncryptSupported: 实例是否支持数据加密。0-不支持；1-支持
        :type IsEncryptSupported: int
        :param _Machine: 实例母机机器型号
        :type Machine: str
        :param _Memory: 实例内存大小，单位 GB，各个分片的内存大小的和
        :type Memory: int
        :param _Storage: 实例磁盘存储大小，单位 GB，各个分片的磁盘大小的和
        :type Storage: int
        :param _StorageUsage: 实例存储空间使用率，计算方式为：各个分片已经使用的磁盘大小的和/各个分片的磁盘大小的和。
        :type StorageUsage: float
        :param _LogStorage: 日志存储空间大小，单位GB
        :type LogStorage: int
        :param _Pid: 产品类型ID
        :type Pid: int
        :param _MasterZone: 主DB可用区
        :type MasterZone: str
        :param _SlaveZones: 从DB可用区
        :type SlaveZones: list of str
        :param _Shards: 分片信息
        :type Shards: list of ShardBriefInfo
        :param _Vip6: 内网IPv6
        :type Vip6: str
        :param _Cpu: 实例Cpu核数
        :type Cpu: int
        :param _Qps: 实例QPS
        :type Qps: int
        :param _DbEngine: DB引擎
        :type DbEngine: str
        :param _Ipv6Flag: 是否支持IPv6
        :type Ipv6Flag: int
        :param _WanVipv6: 外网IPv6地址，公网可访问
        :type WanVipv6: str
        :param _WanStatusIpv6: 外网状态，0-未开通；1-已开通；2-关闭；3-开通中；4-关闭中
        :type WanStatusIpv6: int
        :param _WanPortIpv6: 外网IPv6端口
        :type WanPortIpv6: int
        :param _ResourceTags: 标签信息
        :type ResourceTags: list of ResourceTag
        :param _DcnFlag: DCN标志，0-无，1-主实例，2-灾备实例
        :type DcnFlag: int
        :param _DcnStatus: DCN状态，0-无，1-创建中，2-同步中，3-已断开
        :type DcnStatus: int
        :param _DcnDstNum: DCN灾备实例数
        :type DcnDstNum: int
        :param _InstanceType: 1： 主实例（独享型）, 2: 主实例, 3： 灾备实例, 4： 灾备实例（独享型）
        :type InstanceType: int
        :param _IsMaxUserConnectionsSupported: 实例是否支持设置用户连接数限制，内核为10.1暂不支持。
        :type IsMaxUserConnectionsSupported: bool
        :param _DbVersionId: 对外显示的数据库版本
        :type DbVersionId: str
        :param _EncryptStatus: 加密状态, 0-未开启，1-已开启
        :type EncryptStatus: int
        :param _ExclusterType: 独享集群类型，0:公有云, 1:金融围笼, 2:CDC集群
        :type ExclusterType: int
        :param _RsAccessStrategy: VPC就近访问
        :type RsAccessStrategy: int
        :param _ReservedNetResources: 尚未回收的网络资源
        :type ReservedNetResources: list of ReservedNetResource
        :param _IsPhysicalReplicationSupported: 是否支持物理复制
        :type IsPhysicalReplicationSupported: bool
        :param _IsDcnStrongSyncSupported: 是否支持强同步DCN
        :type IsDcnStrongSyncSupported: int
        :param _IsDcnSwitchSupported: 是否支持DCN切换
        :type IsDcnSwitchSupported: int
        :param _CpuType: cpu类型，英特尔：Intel/AMD，海光：Hygon，默认Intel/AMD	
        :type CpuType: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Status = None
        self._StatusDesc = None
        self._Vip = None
        self._Vport = None
        self._NodeCount = None
        self._Region = None
        self._VpcId = None
        self._SubnetId = None
        self._WanStatus = None
        self._WanDomain = None
        self._WanVip = None
        self._WanPort = None
        self._ProjectId = None
        self._AutoRenewFlag = None
        self._ExclusterId = None
        self._PayMode = None
        self._CreateTime = None
        self._PeriodEndTime = None
        self._DbVersion = None
        self._IsAuditSupported = None
        self._IsEncryptSupported = None
        self._Machine = None
        self._Memory = None
        self._Storage = None
        self._StorageUsage = None
        self._LogStorage = None
        self._Pid = None
        self._MasterZone = None
        self._SlaveZones = None
        self._Shards = None
        self._Vip6 = None
        self._Cpu = None
        self._Qps = None
        self._DbEngine = None
        self._Ipv6Flag = None
        self._WanVipv6 = None
        self._WanStatusIpv6 = None
        self._WanPortIpv6 = None
        self._ResourceTags = None
        self._DcnFlag = None
        self._DcnStatus = None
        self._DcnDstNum = None
        self._InstanceType = None
        self._IsMaxUserConnectionsSupported = None
        self._DbVersionId = None
        self._EncryptStatus = None
        self._ExclusterType = None
        self._RsAccessStrategy = None
        self._ReservedNetResources = None
        self._IsPhysicalReplicationSupported = None
        self._IsDcnStrongSyncSupported = None
        self._IsDcnSwitchSupported = None
        self._CpuType = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """实例ID，形如dcdbt-7oaxtcb7
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Status(self):
        """实例状态。0-实例创建中；1-异步任务处理中；2-运行中；3-实例未初始化；-1-实例已隔离
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        """实例目前运行状态描述
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def Vip(self):
        """实例内网IP地址
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """实例内网端口
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def NodeCount(self):
        """实例节点数。值为2时表示一主一从，值为3时表示一主二从
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def Region(self):
        """实例所在地域名称，形如ap-guangzhou
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        """实例私有网络ID，形如vpc-r9jr0de3
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """实例私有网络子网ID，形如subnet-6rqs61o2
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def WanStatus(self):
        """外网状态，0-未开通；1-已开通；2-关闭；3-开通中；4-关闭中
        :rtype: int
        """
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

    @property
    def WanDomain(self):
        """外网访问的域名，公网可解析
        :rtype: str
        """
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain

    @property
    def WanVip(self):
        """外网IP地址，公网可访问
        :rtype: str
        """
        return self._WanVip

    @WanVip.setter
    def WanVip(self, WanVip):
        self._WanVip = WanVip

    @property
    def WanPort(self):
        """外网访问端口
        :rtype: int
        """
        return self._WanPort

    @WanPort.setter
    def WanPort(self, WanPort):
        self._WanPort = WanPort

    @property
    def ProjectId(self):
        """实例所属项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AutoRenewFlag(self):
        """实例自动续费标志。0-正常续费；1-自动续费；2-到期不续费
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def ExclusterId(self):
        """独享集群ID
        :rtype: str
        """
        return self._ExclusterId

    @ExclusterId.setter
    def ExclusterId(self, ExclusterId):
        self._ExclusterId = ExclusterId

    @property
    def PayMode(self):
        """付费模式。prepaid-预付费；postpaid-按量计费
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def CreateTime(self):
        """实例创建时间，格式为 2006-01-02 15:04:05
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def PeriodEndTime(self):
        """实例到期时间，格式为 2006-01-02 15:04:05
        :rtype: str
        """
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def DbVersion(self):
        """数据库版本信息
        :rtype: str
        """
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def IsAuditSupported(self):
        """实例是否支持审计。0-不支持；1-支持
        :rtype: int
        """
        return self._IsAuditSupported

    @IsAuditSupported.setter
    def IsAuditSupported(self, IsAuditSupported):
        self._IsAuditSupported = IsAuditSupported

    @property
    def IsEncryptSupported(self):
        """实例是否支持数据加密。0-不支持；1-支持
        :rtype: int
        """
        return self._IsEncryptSupported

    @IsEncryptSupported.setter
    def IsEncryptSupported(self, IsEncryptSupported):
        self._IsEncryptSupported = IsEncryptSupported

    @property
    def Machine(self):
        """实例母机机器型号
        :rtype: str
        """
        return self._Machine

    @Machine.setter
    def Machine(self, Machine):
        self._Machine = Machine

    @property
    def Memory(self):
        """实例内存大小，单位 GB，各个分片的内存大小的和
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        """实例磁盘存储大小，单位 GB，各个分片的磁盘大小的和
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def StorageUsage(self):
        """实例存储空间使用率，计算方式为：各个分片已经使用的磁盘大小的和/各个分片的磁盘大小的和。
        :rtype: float
        """
        return self._StorageUsage

    @StorageUsage.setter
    def StorageUsage(self, StorageUsage):
        self._StorageUsage = StorageUsage

    @property
    def LogStorage(self):
        """日志存储空间大小，单位GB
        :rtype: int
        """
        return self._LogStorage

    @LogStorage.setter
    def LogStorage(self, LogStorage):
        self._LogStorage = LogStorage

    @property
    def Pid(self):
        """产品类型ID
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def MasterZone(self):
        """主DB可用区
        :rtype: str
        """
        return self._MasterZone

    @MasterZone.setter
    def MasterZone(self, MasterZone):
        self._MasterZone = MasterZone

    @property
    def SlaveZones(self):
        """从DB可用区
        :rtype: list of str
        """
        return self._SlaveZones

    @SlaveZones.setter
    def SlaveZones(self, SlaveZones):
        self._SlaveZones = SlaveZones

    @property
    def Shards(self):
        """分片信息
        :rtype: list of ShardBriefInfo
        """
        return self._Shards

    @Shards.setter
    def Shards(self, Shards):
        self._Shards = Shards

    @property
    def Vip6(self):
        """内网IPv6
        :rtype: str
        """
        return self._Vip6

    @Vip6.setter
    def Vip6(self, Vip6):
        self._Vip6 = Vip6

    @property
    def Cpu(self):
        """实例Cpu核数
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Qps(self):
        """实例QPS
        :rtype: int
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def DbEngine(self):
        """DB引擎
        :rtype: str
        """
        return self._DbEngine

    @DbEngine.setter
    def DbEngine(self, DbEngine):
        self._DbEngine = DbEngine

    @property
    def Ipv6Flag(self):
        """是否支持IPv6
        :rtype: int
        """
        return self._Ipv6Flag

    @Ipv6Flag.setter
    def Ipv6Flag(self, Ipv6Flag):
        self._Ipv6Flag = Ipv6Flag

    @property
    def WanVipv6(self):
        """外网IPv6地址，公网可访问
        :rtype: str
        """
        return self._WanVipv6

    @WanVipv6.setter
    def WanVipv6(self, WanVipv6):
        self._WanVipv6 = WanVipv6

    @property
    def WanStatusIpv6(self):
        """外网状态，0-未开通；1-已开通；2-关闭；3-开通中；4-关闭中
        :rtype: int
        """
        return self._WanStatusIpv6

    @WanStatusIpv6.setter
    def WanStatusIpv6(self, WanStatusIpv6):
        self._WanStatusIpv6 = WanStatusIpv6

    @property
    def WanPortIpv6(self):
        """外网IPv6端口
        :rtype: int
        """
        return self._WanPortIpv6

    @WanPortIpv6.setter
    def WanPortIpv6(self, WanPortIpv6):
        self._WanPortIpv6 = WanPortIpv6

    @property
    def ResourceTags(self):
        """标签信息
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def DcnFlag(self):
        """DCN标志，0-无，1-主实例，2-灾备实例
        :rtype: int
        """
        return self._DcnFlag

    @DcnFlag.setter
    def DcnFlag(self, DcnFlag):
        self._DcnFlag = DcnFlag

    @property
    def DcnStatus(self):
        """DCN状态，0-无，1-创建中，2-同步中，3-已断开
        :rtype: int
        """
        return self._DcnStatus

    @DcnStatus.setter
    def DcnStatus(self, DcnStatus):
        self._DcnStatus = DcnStatus

    @property
    def DcnDstNum(self):
        """DCN灾备实例数
        :rtype: int
        """
        return self._DcnDstNum

    @DcnDstNum.setter
    def DcnDstNum(self, DcnDstNum):
        self._DcnDstNum = DcnDstNum

    @property
    def InstanceType(self):
        """1： 主实例（独享型）, 2: 主实例, 3： 灾备实例, 4： 灾备实例（独享型）
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def IsMaxUserConnectionsSupported(self):
        """实例是否支持设置用户连接数限制，内核为10.1暂不支持。
        :rtype: bool
        """
        return self._IsMaxUserConnectionsSupported

    @IsMaxUserConnectionsSupported.setter
    def IsMaxUserConnectionsSupported(self, IsMaxUserConnectionsSupported):
        self._IsMaxUserConnectionsSupported = IsMaxUserConnectionsSupported

    @property
    def DbVersionId(self):
        """对外显示的数据库版本
        :rtype: str
        """
        return self._DbVersionId

    @DbVersionId.setter
    def DbVersionId(self, DbVersionId):
        self._DbVersionId = DbVersionId

    @property
    def EncryptStatus(self):
        """加密状态, 0-未开启，1-已开启
        :rtype: int
        """
        return self._EncryptStatus

    @EncryptStatus.setter
    def EncryptStatus(self, EncryptStatus):
        self._EncryptStatus = EncryptStatus

    @property
    def ExclusterType(self):
        """独享集群类型，0:公有云, 1:金融围笼, 2:CDC集群
        :rtype: int
        """
        return self._ExclusterType

    @ExclusterType.setter
    def ExclusterType(self, ExclusterType):
        self._ExclusterType = ExclusterType

    @property
    def RsAccessStrategy(self):
        """VPC就近访问
        :rtype: int
        """
        return self._RsAccessStrategy

    @RsAccessStrategy.setter
    def RsAccessStrategy(self, RsAccessStrategy):
        self._RsAccessStrategy = RsAccessStrategy

    @property
    def ReservedNetResources(self):
        """尚未回收的网络资源
        :rtype: list of ReservedNetResource
        """
        return self._ReservedNetResources

    @ReservedNetResources.setter
    def ReservedNetResources(self, ReservedNetResources):
        self._ReservedNetResources = ReservedNetResources

    @property
    def IsPhysicalReplicationSupported(self):
        """是否支持物理复制
        :rtype: bool
        """
        return self._IsPhysicalReplicationSupported

    @IsPhysicalReplicationSupported.setter
    def IsPhysicalReplicationSupported(self, IsPhysicalReplicationSupported):
        self._IsPhysicalReplicationSupported = IsPhysicalReplicationSupported

    @property
    def IsDcnStrongSyncSupported(self):
        """是否支持强同步DCN
        :rtype: int
        """
        return self._IsDcnStrongSyncSupported

    @IsDcnStrongSyncSupported.setter
    def IsDcnStrongSyncSupported(self, IsDcnStrongSyncSupported):
        self._IsDcnStrongSyncSupported = IsDcnStrongSyncSupported

    @property
    def IsDcnSwitchSupported(self):
        """是否支持DCN切换
        :rtype: int
        """
        return self._IsDcnSwitchSupported

    @IsDcnSwitchSupported.setter
    def IsDcnSwitchSupported(self, IsDcnSwitchSupported):
        self._IsDcnSwitchSupported = IsDcnSwitchSupported

    @property
    def CpuType(self):
        """cpu类型，英特尔：Intel/AMD，海光：Hygon，默认Intel/AMD	
        :rtype: str
        """
        return self._CpuType

    @CpuType.setter
    def CpuType(self, CpuType):
        self._CpuType = CpuType

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._NodeCount = params.get("NodeCount")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._WanStatus = params.get("WanStatus")
        self._WanDomain = params.get("WanDomain")
        self._WanVip = params.get("WanVip")
        self._WanPort = params.get("WanPort")
        self._ProjectId = params.get("ProjectId")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._ExclusterId = params.get("ExclusterId")
        self._PayMode = params.get("PayMode")
        self._CreateTime = params.get("CreateTime")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._DbVersion = params.get("DbVersion")
        self._IsAuditSupported = params.get("IsAuditSupported")
        self._IsEncryptSupported = params.get("IsEncryptSupported")
        self._Machine = params.get("Machine")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._StorageUsage = params.get("StorageUsage")
        self._LogStorage = params.get("LogStorage")
        self._Pid = params.get("Pid")
        self._MasterZone = params.get("MasterZone")
        self._SlaveZones = params.get("SlaveZones")
        if params.get("Shards") is not None:
            self._Shards = []
            for item in params.get("Shards"):
                obj = ShardBriefInfo()
                obj._deserialize(item)
                self._Shards.append(obj)
        self._Vip6 = params.get("Vip6")
        self._Cpu = params.get("Cpu")
        self._Qps = params.get("Qps")
        self._DbEngine = params.get("DbEngine")
        self._Ipv6Flag = params.get("Ipv6Flag")
        self._WanVipv6 = params.get("WanVipv6")
        self._WanStatusIpv6 = params.get("WanStatusIpv6")
        self._WanPortIpv6 = params.get("WanPortIpv6")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._DcnFlag = params.get("DcnFlag")
        self._DcnStatus = params.get("DcnStatus")
        self._DcnDstNum = params.get("DcnDstNum")
        self._InstanceType = params.get("InstanceType")
        self._IsMaxUserConnectionsSupported = params.get("IsMaxUserConnectionsSupported")
        self._DbVersionId = params.get("DbVersionId")
        self._EncryptStatus = params.get("EncryptStatus")
        self._ExclusterType = params.get("ExclusterType")
        self._RsAccessStrategy = params.get("RsAccessStrategy")
        if params.get("ReservedNetResources") is not None:
            self._ReservedNetResources = []
            for item in params.get("ReservedNetResources"):
                obj = ReservedNetResource()
                obj._deserialize(item)
                self._ReservedNetResources.append(obj)
        self._IsPhysicalReplicationSupported = params.get("IsPhysicalReplicationSupported")
        self._IsDcnStrongSyncSupported = params.get("IsDcnStrongSyncSupported")
        self._IsDcnSwitchSupported = params.get("IsDcnSwitchSupported")
        self._CpuType = params.get("CpuType")
        self._RequestId = params.get("RequestId")


class DescribeDCDBInstanceNodeInfoRequest(AbstractModel):
    """DescribeDCDBInstanceNodeInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Limit: 单次最多返回多少条，取值范围为(0-100]，默认为100
        :type Limit: int
        :param _Offset: 返回数据的偏移值，默认为0
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        """单次最多返回多少条，取值范围为(0-100]，默认为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """返回数据的偏移值，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDCDBInstanceNodeInfoResponse(AbstractModel):
    """DescribeDCDBInstanceNodeInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 节点总个数
        :type TotalCount: int
        :param _NodesInfo: 节点信息
        :type NodesInfo: list of BriefNodeInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._NodesInfo = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """节点总个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NodesInfo(self):
        """节点信息
        :rtype: list of BriefNodeInfo
        """
        return self._NodesInfo

    @NodesInfo.setter
    def NodesInfo(self, NodesInfo):
        self._NodesInfo = NodesInfo

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("NodesInfo") is not None:
            self._NodesInfo = []
            for item in params.get("NodesInfo"):
                obj = BriefNodeInfo()
                obj._deserialize(item)
                self._NodesInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDCDBInstancesRequest(AbstractModel):
    """DescribeDCDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 按照一个或者多个实例 ID 查询。实例 ID 形如：dcdbt-2t4cf98d
        :type InstanceIds: list of str
        :param _SearchName: 搜索的字段名，当前支持的值有：instancename、vip、all。传 instancename 表示按实例名进行搜索；传 vip 表示按内网IP进行搜索；传 all 将会按实例ID、实例名和内网IP进行搜索。
        :type SearchName: str
        :param _SearchKey: 搜索的关键字，支持模糊搜索。多个关键字使用换行符（'\n'）分割。
        :type SearchKey: str
        :param _ProjectIds: 按项目 ID 查询
        :type ProjectIds: list of int
        :param _IsFilterVpc: 是否根据 VPC 网络来搜索
        :type IsFilterVpc: bool
        :param _VpcId: 私有网络 ID， IsFilterVpc 为 1 时有效
        :type VpcId: str
        :param _SubnetId: 私有网络的子网 ID， IsFilterVpc 为 1 时有效
        :type SubnetId: str
        :param _OrderBy: 排序字段， projectId， createtime， instancename 三者之一
        :type OrderBy: str
        :param _OrderByType: 排序类型， desc 或者 asc
        :type OrderByType: str
        :param _Offset: 偏移量，默认为 0
        :type Offset: int
        :param _Limit: 返回数量，默认为 10，最大值为 100。
        :type Limit: int
        :param _ExclusterType: 1非独享集群，2独享集群， 0全部
        :type ExclusterType: int
        :param _IsFilterExcluster: 标识是否使用ExclusterType字段, false不使用，true使用
        :type IsFilterExcluster: bool
        :param _ExclusterIds: 独享集群ID
        :type ExclusterIds: list of str
        :param _TagKeys: 按标签key查询
        :type TagKeys: list of str
        :param _Tags: 标签
        :type Tags: list of Tag
        :param _FilterInstanceType: 实例类型过滤，1-独享实例，2-主实例，3-灾备实例，多个按逗号分隔
        :type FilterInstanceType: str
        :param _Status: 按实例状态筛选。状态值 -2：已删除； -1：已隔离；0：创建中；1：流程处理中；2：运行中
        :type Status: list of int
        :param _ExcludeStatus: 排除实例状态。状态值 -2：已删除； -1：已隔离；0：创建中；1：流程处理中；2：运行中
        :type ExcludeStatus: list of int
        """
        self._InstanceIds = None
        self._SearchName = None
        self._SearchKey = None
        self._ProjectIds = None
        self._IsFilterVpc = None
        self._VpcId = None
        self._SubnetId = None
        self._OrderBy = None
        self._OrderByType = None
        self._Offset = None
        self._Limit = None
        self._ExclusterType = None
        self._IsFilterExcluster = None
        self._ExclusterIds = None
        self._TagKeys = None
        self._Tags = None
        self._FilterInstanceType = None
        self._Status = None
        self._ExcludeStatus = None

    @property
    def InstanceIds(self):
        """按照一个或者多个实例 ID 查询。实例 ID 形如：dcdbt-2t4cf98d
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def SearchName(self):
        """搜索的字段名，当前支持的值有：instancename、vip、all。传 instancename 表示按实例名进行搜索；传 vip 表示按内网IP进行搜索；传 all 将会按实例ID、实例名和内网IP进行搜索。
        :rtype: str
        """
        return self._SearchName

    @SearchName.setter
    def SearchName(self, SearchName):
        self._SearchName = SearchName

    @property
    def SearchKey(self):
        """搜索的关键字，支持模糊搜索。多个关键字使用换行符（'\n'）分割。
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def ProjectIds(self):
        """按项目 ID 查询
        :rtype: list of int
        """
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def IsFilterVpc(self):
        """是否根据 VPC 网络来搜索
        :rtype: bool
        """
        return self._IsFilterVpc

    @IsFilterVpc.setter
    def IsFilterVpc(self, IsFilterVpc):
        self._IsFilterVpc = IsFilterVpc

    @property
    def VpcId(self):
        """私有网络 ID， IsFilterVpc 为 1 时有效
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """私有网络的子网 ID， IsFilterVpc 为 1 时有效
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def OrderBy(self):
        """排序字段， projectId， createtime， instancename 三者之一
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        """排序类型， desc 或者 asc
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Offset(self):
        """偏移量，默认为 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为 10，最大值为 100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ExclusterType(self):
        """1非独享集群，2独享集群， 0全部
        :rtype: int
        """
        return self._ExclusterType

    @ExclusterType.setter
    def ExclusterType(self, ExclusterType):
        self._ExclusterType = ExclusterType

    @property
    def IsFilterExcluster(self):
        """标识是否使用ExclusterType字段, false不使用，true使用
        :rtype: bool
        """
        return self._IsFilterExcluster

    @IsFilterExcluster.setter
    def IsFilterExcluster(self, IsFilterExcluster):
        self._IsFilterExcluster = IsFilterExcluster

    @property
    def ExclusterIds(self):
        """独享集群ID
        :rtype: list of str
        """
        return self._ExclusterIds

    @ExclusterIds.setter
    def ExclusterIds(self, ExclusterIds):
        self._ExclusterIds = ExclusterIds

    @property
    def TagKeys(self):
        """按标签key查询
        :rtype: list of str
        """
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def Tags(self):
        """标签
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def FilterInstanceType(self):
        """实例类型过滤，1-独享实例，2-主实例，3-灾备实例，多个按逗号分隔
        :rtype: str
        """
        return self._FilterInstanceType

    @FilterInstanceType.setter
    def FilterInstanceType(self, FilterInstanceType):
        self._FilterInstanceType = FilterInstanceType

    @property
    def Status(self):
        """按实例状态筛选。状态值 -2：已删除； -1：已隔离；0：创建中；1：流程处理中；2：运行中
        :rtype: list of int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ExcludeStatus(self):
        """排除实例状态。状态值 -2：已删除； -1：已隔离；0：创建中；1：流程处理中；2：运行中
        :rtype: list of int
        """
        return self._ExcludeStatus

    @ExcludeStatus.setter
    def ExcludeStatus(self, ExcludeStatus):
        self._ExcludeStatus = ExcludeStatus


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._SearchName = params.get("SearchName")
        self._SearchKey = params.get("SearchKey")
        self._ProjectIds = params.get("ProjectIds")
        self._IsFilterVpc = params.get("IsFilterVpc")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ExclusterType = params.get("ExclusterType")
        self._IsFilterExcluster = params.get("IsFilterExcluster")
        self._ExclusterIds = params.get("ExclusterIds")
        self._TagKeys = params.get("TagKeys")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._FilterInstanceType = params.get("FilterInstanceType")
        self._Status = params.get("Status")
        self._ExcludeStatus = params.get("ExcludeStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDCDBInstancesResponse(AbstractModel):
    """DescribeDCDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的实例数量
        :type TotalCount: int
        :param _Instances: 实例详细信息列表
        :type Instances: list of DCDBInstanceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Instances = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的实例数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Instances(self):
        """实例详细信息列表
        :rtype: list of DCDBInstanceInfo
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = DCDBInstanceInfo()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDCDBPriceRequest(AbstractModel):
    """DescribeDCDBPrice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 欲新购实例的可用区ID。
        :type Zone: str
        :param _Count: 欲购买实例的数量，目前支持购买1-10个实例
        :type Count: int
        :param _Period: 欲购买的时长，单位：月。
        :type Period: int
        :param _ShardNodeCount: 单个分片节点个数大小，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardNodeCount: int
        :param _ShardMemory: 分片内存大小，单位：GB，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardMemory: int
        :param _ShardStorage: 分片存储空间大小，单位：GB，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardStorage: int
        :param _ShardCount: 实例分片个数，可选范围2-8，可以通过升级实例进行新增分片到最多64个分片。
        :type ShardCount: int
        :param _Paymode: 付费类型。postpaid：按量付费   prepaid：预付费
        :type Paymode: str
        :param _AmountUnit: 价格金额单位，不传默认单位为分，取值：  
* pent：分
* microPent：微分
        :type AmountUnit: str
        :param _CpuType: Cpu类型，如：英特尔：Intel/AMD，海光：Hygon，默认Intel/AMD
        :type CpuType: str
        """
        self._Zone = None
        self._Count = None
        self._Period = None
        self._ShardNodeCount = None
        self._ShardMemory = None
        self._ShardStorage = None
        self._ShardCount = None
        self._Paymode = None
        self._AmountUnit = None
        self._CpuType = None

    @property
    def Zone(self):
        """欲新购实例的可用区ID。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Count(self):
        """欲购买实例的数量，目前支持购买1-10个实例
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Period(self):
        """欲购买的时长，单位：月。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def ShardNodeCount(self):
        """单个分片节点个数大小，可以通过 DescribeShardSpec
 查询实例规格获得。
        :rtype: int
        """
        return self._ShardNodeCount

    @ShardNodeCount.setter
    def ShardNodeCount(self, ShardNodeCount):
        self._ShardNodeCount = ShardNodeCount

    @property
    def ShardMemory(self):
        """分片内存大小，单位：GB，可以通过 DescribeShardSpec
 查询实例规格获得。
        :rtype: int
        """
        return self._ShardMemory

    @ShardMemory.setter
    def ShardMemory(self, ShardMemory):
        self._ShardMemory = ShardMemory

    @property
    def ShardStorage(self):
        """分片存储空间大小，单位：GB，可以通过 DescribeShardSpec
 查询实例规格获得。
        :rtype: int
        """
        return self._ShardStorage

    @ShardStorage.setter
    def ShardStorage(self, ShardStorage):
        self._ShardStorage = ShardStorage

    @property
    def ShardCount(self):
        """实例分片个数，可选范围2-8，可以通过升级实例进行新增分片到最多64个分片。
        :rtype: int
        """
        return self._ShardCount

    @ShardCount.setter
    def ShardCount(self, ShardCount):
        self._ShardCount = ShardCount

    @property
    def Paymode(self):
        """付费类型。postpaid：按量付费   prepaid：预付费
        :rtype: str
        """
        return self._Paymode

    @Paymode.setter
    def Paymode(self, Paymode):
        self._Paymode = Paymode

    @property
    def AmountUnit(self):
        """价格金额单位，不传默认单位为分，取值：  
* pent：分
* microPent：微分
        :rtype: str
        """
        return self._AmountUnit

    @AmountUnit.setter
    def AmountUnit(self, AmountUnit):
        self._AmountUnit = AmountUnit

    @property
    def CpuType(self):
        """Cpu类型，如：英特尔：Intel/AMD，海光：Hygon，默认Intel/AMD
        :rtype: str
        """
        return self._CpuType

    @CpuType.setter
    def CpuType(self, CpuType):
        self._CpuType = CpuType


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Count = params.get("Count")
        self._Period = params.get("Period")
        self._ShardNodeCount = params.get("ShardNodeCount")
        self._ShardMemory = params.get("ShardMemory")
        self._ShardStorage = params.get("ShardStorage")
        self._ShardCount = params.get("ShardCount")
        self._Paymode = params.get("Paymode")
        self._AmountUnit = params.get("AmountUnit")
        self._CpuType = params.get("CpuType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDCDBPriceResponse(AbstractModel):
    """DescribeDCDBPrice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriginalPrice: 原价  
* 单位：默认为分，若请求参数带有AmountUnit，参考AmountUnit描述
* 币种：国内站为人民币，国际站为美元
        :type OriginalPrice: int
        :param _Price: 实际价格，受折扣等影响，可能和原价不同
* 单位：默认为分，若请求参数带有AmountUnit，参考AmountUnit描述
* 币种：国内站人民币，国际站美元
        :type Price: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OriginalPrice = None
        self._Price = None
        self._RequestId = None

    @property
    def OriginalPrice(self):
        """原价  
* 单位：默认为分，若请求参数带有AmountUnit，参考AmountUnit描述
* 币种：国内站为人民币，国际站为美元
        :rtype: int
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Price(self):
        """实际价格，受折扣等影响，可能和原价不同
* 单位：默认为分，若请求参数带有AmountUnit，参考AmountUnit描述
* 币种：国内站人民币，国际站美元
        :rtype: int
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalPrice = params.get("OriginalPrice")
        self._Price = params.get("Price")
        self._RequestId = params.get("RequestId")


class DescribeDCDBRenewalPriceRequest(AbstractModel):
    """DescribeDCDBRenewalPrice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 待续费的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param _Period: 续费时长，单位：月。不传则默认为1个月。
        :type Period: int
        :param _AmountUnit: 价格金额单位，不传默认单位为分，取值：  
* pent：分
* microPent：微分
        :type AmountUnit: str
        """
        self._InstanceId = None
        self._Period = None
        self._AmountUnit = None

    @property
    def InstanceId(self):
        """待续费的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Period(self):
        """续费时长，单位：月。不传则默认为1个月。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def AmountUnit(self):
        """价格金额单位，不传默认单位为分，取值：  
* pent：分
* microPent：微分
        :rtype: str
        """
        return self._AmountUnit

    @AmountUnit.setter
    def AmountUnit(self, AmountUnit):
        self._AmountUnit = AmountUnit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Period = params.get("Period")
        self._AmountUnit = params.get("AmountUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDCDBRenewalPriceResponse(AbstractModel):
    """DescribeDCDBRenewalPrice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriginalPrice: 原价  
* 单位：默认为分，若请求参数带有AmountUnit，参考AmountUnit描述
* 币种：国内站为人民币，国际站为美元
        :type OriginalPrice: int
        :param _Price: 实际价格，受折扣等影响，可能和原价不同
* 单位：默认为分，若请求参数带有AmountUnit，参考AmountUnit描述
* 币种：国内站人民币，国际站美元
        :type Price: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OriginalPrice = None
        self._Price = None
        self._RequestId = None

    @property
    def OriginalPrice(self):
        """原价  
* 单位：默认为分，若请求参数带有AmountUnit，参考AmountUnit描述
* 币种：国内站为人民币，国际站为美元
        :rtype: int
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Price(self):
        """实际价格，受折扣等影响，可能和原价不同
* 单位：默认为分，若请求参数带有AmountUnit，参考AmountUnit描述
* 币种：国内站人民币，国际站美元
        :rtype: int
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalPrice = params.get("OriginalPrice")
        self._Price = params.get("Price")
        self._RequestId = params.get("RequestId")


class DescribeDCDBSaleInfoRequest(AbstractModel):
    """DescribeDCDBSaleInfo请求参数结构体

    """


class DescribeDCDBSaleInfoResponse(AbstractModel):
    """DescribeDCDBSaleInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegionList: 可售卖地域信息列表
        :type RegionList: list of RegionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegionList = None
        self._RequestId = None

    @property
    def RegionList(self):
        """可售卖地域信息列表
        :rtype: list of RegionInfo
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = RegionInfo()
                obj._deserialize(item)
                self._RegionList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDCDBShardsRequest(AbstractModel):
    """DescribeDCDBShards请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param _ShardInstanceIds: 分片ID列表。
        :type ShardInstanceIds: list of str
        :param _Offset: 偏移量，默认为 0
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _OrderBy: 排序字段， 目前仅支持 createtime
        :type OrderBy: str
        :param _OrderByType: 排序类型， desc 或者 asc
        :type OrderByType: str
        """
        self._InstanceId = None
        self._ShardInstanceIds = None
        self._Offset = None
        self._Limit = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def InstanceId(self):
        """实例ID，形如：dcdbt-ow728lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ShardInstanceIds(self):
        """分片ID列表。
        :rtype: list of str
        """
        return self._ShardInstanceIds

    @ShardInstanceIds.setter
    def ShardInstanceIds(self, ShardInstanceIds):
        self._ShardInstanceIds = ShardInstanceIds

    @property
    def Offset(self):
        """偏移量，默认为 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为 20，最大值为 100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderBy(self):
        """排序字段， 目前仅支持 createtime
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        """排序类型， desc 或者 asc
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ShardInstanceIds = params.get("ShardInstanceIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDCDBShardsResponse(AbstractModel):
    """DescribeDCDBShards返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的分片数量
        :type TotalCount: int
        :param _Shards: 分片信息列表
        :type Shards: list of DCDBShardInfo
        :param _DcnFlag: 灾备标志，0-无，1-主实例，2-灾备实例
        :type DcnFlag: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Shards = None
        self._DcnFlag = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的分片数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Shards(self):
        """分片信息列表
        :rtype: list of DCDBShardInfo
        """
        return self._Shards

    @Shards.setter
    def Shards(self, Shards):
        self._Shards = Shards

    @property
    def DcnFlag(self):
        """灾备标志，0-无，1-主实例，2-灾备实例
        :rtype: int
        """
        return self._DcnFlag

    @DcnFlag.setter
    def DcnFlag(self, DcnFlag):
        self._DcnFlag = DcnFlag

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Shards") is not None:
            self._Shards = []
            for item in params.get("Shards"):
                obj = DCDBShardInfo()
                obj._deserialize(item)
                self._Shards.append(obj)
        self._DcnFlag = params.get("DcnFlag")
        self._RequestId = params.get("RequestId")


class DescribeDCDBUpgradePriceRequest(AbstractModel):
    """DescribeDCDBUpgradePrice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 待升级的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param _UpgradeType: 升级类型，取值范围: 
<li> ADD: 新增分片 </li> 
 <li> EXPAND: 升级实例中的已有分片 </li> 
 <li> SPLIT: 将已有分片中的数据切分到新增分片上</li>
        :type UpgradeType: str
        :param _AddShardConfig: 新增分片配置，当UpgradeType为ADD时生效。
        :type AddShardConfig: :class:`tencentcloud.dcdb.v20180411.models.AddShardConfig`
        :param _ExpandShardConfig: 扩容分片配置，当UpgradeType为EXPAND时生效。
        :type ExpandShardConfig: :class:`tencentcloud.dcdb.v20180411.models.ExpandShardConfig`
        :param _SplitShardConfig: 切分分片配置，当UpgradeType为SPLIT时生效。
        :type SplitShardConfig: :class:`tencentcloud.dcdb.v20180411.models.SplitShardConfig`
        :param _AmountUnit: 价格金额单位，不传默认单位为分，取值：  
* pent：分
* microPent：微分
        :type AmountUnit: str
        """
        self._InstanceId = None
        self._UpgradeType = None
        self._AddShardConfig = None
        self._ExpandShardConfig = None
        self._SplitShardConfig = None
        self._AmountUnit = None

    @property
    def InstanceId(self):
        """待升级的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UpgradeType(self):
        """升级类型，取值范围: 
<li> ADD: 新增分片 </li> 
 <li> EXPAND: 升级实例中的已有分片 </li> 
 <li> SPLIT: 将已有分片中的数据切分到新增分片上</li>
        :rtype: str
        """
        return self._UpgradeType

    @UpgradeType.setter
    def UpgradeType(self, UpgradeType):
        self._UpgradeType = UpgradeType

    @property
    def AddShardConfig(self):
        """新增分片配置，当UpgradeType为ADD时生效。
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.AddShardConfig`
        """
        return self._AddShardConfig

    @AddShardConfig.setter
    def AddShardConfig(self, AddShardConfig):
        self._AddShardConfig = AddShardConfig

    @property
    def ExpandShardConfig(self):
        """扩容分片配置，当UpgradeType为EXPAND时生效。
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ExpandShardConfig`
        """
        return self._ExpandShardConfig

    @ExpandShardConfig.setter
    def ExpandShardConfig(self, ExpandShardConfig):
        self._ExpandShardConfig = ExpandShardConfig

    @property
    def SplitShardConfig(self):
        """切分分片配置，当UpgradeType为SPLIT时生效。
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.SplitShardConfig`
        """
        return self._SplitShardConfig

    @SplitShardConfig.setter
    def SplitShardConfig(self, SplitShardConfig):
        self._SplitShardConfig = SplitShardConfig

    @property
    def AmountUnit(self):
        """价格金额单位，不传默认单位为分，取值：  
* pent：分
* microPent：微分
        :rtype: str
        """
        return self._AmountUnit

    @AmountUnit.setter
    def AmountUnit(self, AmountUnit):
        self._AmountUnit = AmountUnit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UpgradeType = params.get("UpgradeType")
        if params.get("AddShardConfig") is not None:
            self._AddShardConfig = AddShardConfig()
            self._AddShardConfig._deserialize(params.get("AddShardConfig"))
        if params.get("ExpandShardConfig") is not None:
            self._ExpandShardConfig = ExpandShardConfig()
            self._ExpandShardConfig._deserialize(params.get("ExpandShardConfig"))
        if params.get("SplitShardConfig") is not None:
            self._SplitShardConfig = SplitShardConfig()
            self._SplitShardConfig._deserialize(params.get("SplitShardConfig"))
        self._AmountUnit = params.get("AmountUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDCDBUpgradePriceResponse(AbstractModel):
    """DescribeDCDBUpgradePrice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriginalPrice: 原价  
* 单位：默认为分，若请求参数带有AmountUnit，参考AmountUnit描述
* 币种：国内站为人民币，国际站为美元
        :type OriginalPrice: int
        :param _Price: 实际价格，受折扣等影响，可能和原价不同
* 单位：默认为分，若请求参数带有AmountUnit，参考AmountUnit描述
* 币种：国内站人民币，国际站美元
        :type Price: int
        :param _Formula: 变配明细计算公式
        :type Formula: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OriginalPrice = None
        self._Price = None
        self._Formula = None
        self._RequestId = None

    @property
    def OriginalPrice(self):
        """原价  
* 单位：默认为分，若请求参数带有AmountUnit，参考AmountUnit描述
* 币种：国内站为人民币，国际站为美元
        :rtype: int
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Price(self):
        """实际价格，受折扣等影响，可能和原价不同
* 单位：默认为分，若请求参数带有AmountUnit，参考AmountUnit描述
* 币种：国内站人民币，国际站美元
        :rtype: int
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Formula(self):
        """变配明细计算公式
        :rtype: str
        """
        return self._Formula

    @Formula.setter
    def Formula(self, Formula):
        self._Formula = Formula

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalPrice = params.get("OriginalPrice")
        self._Price = params.get("Price")
        self._Formula = params.get("Formula")
        self._RequestId = params.get("RequestId")


class DescribeDatabaseObjectsRequest(AbstractModel):
    """DescribeDatabaseObjects请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：dcdbt-ow7t8lmc。
        :type InstanceId: str
        :param _DbName: 数据库名称，通过 DescribeDatabases 接口获取。
        :type DbName: str
        """
        self._InstanceId = None
        self._DbName = None

    @property
    def InstanceId(self):
        """实例 ID，形如：dcdbt-ow7t8lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        """数据库名称，通过 DescribeDatabases 接口获取。
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseObjectsResponse(AbstractModel):
    """DescribeDatabaseObjects返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 透传入参。
        :type InstanceId: str
        :param _DbName: 数据库名称。
        :type DbName: str
        :param _Tables: 表列表。
        :type Tables: list of DatabaseTable
        :param _Views: 视图列表。
        :type Views: list of DatabaseView
        :param _Procs: 存储过程列表。
        :type Procs: list of DatabaseProcedure
        :param _Funcs: 函数列表。
        :type Funcs: list of DatabaseFunction
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._DbName = None
        self._Tables = None
        self._Views = None
        self._Procs = None
        self._Funcs = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """透传入参。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        """数据库名称。
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Tables(self):
        """表列表。
        :rtype: list of DatabaseTable
        """
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def Views(self):
        """视图列表。
        :rtype: list of DatabaseView
        """
        return self._Views

    @Views.setter
    def Views(self, Views):
        self._Views = Views

    @property
    def Procs(self):
        """存储过程列表。
        :rtype: list of DatabaseProcedure
        """
        return self._Procs

    @Procs.setter
    def Procs(self, Procs):
        self._Procs = Procs

    @property
    def Funcs(self):
        """函数列表。
        :rtype: list of DatabaseFunction
        """
        return self._Funcs

    @Funcs.setter
    def Funcs(self, Funcs):
        self._Funcs = Funcs

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        if params.get("Tables") is not None:
            self._Tables = []
            for item in params.get("Tables"):
                obj = DatabaseTable()
                obj._deserialize(item)
                self._Tables.append(obj)
        if params.get("Views") is not None:
            self._Views = []
            for item in params.get("Views"):
                obj = DatabaseView()
                obj._deserialize(item)
                self._Views.append(obj)
        if params.get("Procs") is not None:
            self._Procs = []
            for item in params.get("Procs"):
                obj = DatabaseProcedure()
                obj._deserialize(item)
                self._Procs.append(obj)
        if params.get("Funcs") is not None:
            self._Funcs = []
            for item in params.get("Funcs"):
                obj = DatabaseFunction()
                obj._deserialize(item)
                self._Funcs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDatabaseTableRequest(AbstractModel):
    """DescribeDatabaseTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：dcdbt-ow7t8lmc。
        :type InstanceId: str
        :param _DbName: 数据库名称，通过 DescribeDatabases 接口获取。
        :type DbName: str
        :param _Table: 表名称，通过 DescribeDatabaseObjects 接口获取。
        :type Table: str
        """
        self._InstanceId = None
        self._DbName = None
        self._Table = None

    @property
    def InstanceId(self):
        """实例 ID，形如：dcdbt-ow7t8lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        """数据库名称，通过 DescribeDatabases 接口获取。
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Table(self):
        """表名称，通过 DescribeDatabaseObjects 接口获取。
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        self._Table = params.get("Table")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseTableResponse(AbstractModel):
    """DescribeDatabaseTable返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例名称。
        :type InstanceId: str
        :param _DbName: 数据库名称。
        :type DbName: str
        :param _Table: 表名称。
        :type Table: str
        :param _Cols: 列信息。
        :type Cols: list of TableColumn
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._DbName = None
        self._Table = None
        self._Cols = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """实例名称。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        """数据库名称。
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Table(self):
        """表名称。
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Cols(self):
        """列信息。
        :rtype: list of TableColumn
        """
        return self._Cols

    @Cols.setter
    def Cols(self, Cols):
        self._Cols = Cols

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        self._Table = params.get("Table")
        if params.get("Cols") is not None:
            self._Cols = []
            for item in params.get("Cols"):
                obj = TableColumn()
                obj._deserialize(item)
                self._Cols.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：dcdbt-ow7t8lmc。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例 ID，形如：dcdbt-ow7t8lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabasesResponse(AbstractModel):
    """DescribeDatabases返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Databases: 该实例上的数据库列表。
        :type Databases: list of Database
        :param _InstanceId: 透传入参。
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Databases = None
        self._InstanceId = None
        self._RequestId = None

    @property
    def Databases(self):
        """该实例上的数据库列表。
        :rtype: list of Database
        """
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def InstanceId(self):
        """透传入参。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Databases") is not None:
            self._Databases = []
            for item in params.get("Databases"):
                obj = Database()
                obj._deserialize(item)
                self._Databases.append(obj)
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class DescribeDcnDetailRequest(AbstractModel):
    """DescribeDcnDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDcnDetailResponse(AbstractModel):
    """DescribeDcnDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DcnDetails: DCN同步详情
        :type DcnDetails: list of DcnDetailItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DcnDetails = None
        self._RequestId = None

    @property
    def DcnDetails(self):
        """DCN同步详情
        :rtype: list of DcnDetailItem
        """
        return self._DcnDetails

    @DcnDetails.setter
    def DcnDetails(self, DcnDetails):
        self._DcnDetails = DcnDetails

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DcnDetails") is not None:
            self._DcnDetails = []
            for item in params.get("DcnDetails"):
                obj = DcnDetailItem()
                obj._deserialize(item)
                self._DcnDetails.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFileDownloadUrlRequest(AbstractModel):
    """DescribeFileDownloadUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ShardId: 实例分片ID
        :type ShardId: str
        :param _FilePath: 不带签名的文件路径
        :type FilePath: str
        """
        self._InstanceId = None
        self._ShardId = None
        self._FilePath = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ShardId(self):
        """实例分片ID
        :rtype: str
        """
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def FilePath(self):
        """不带签名的文件路径
        :rtype: str
        """
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ShardId = params.get("ShardId")
        self._FilePath = params.get("FilePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileDownloadUrlResponse(AbstractModel):
    """DescribeFileDownloadUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PreSignedUrl: 带签名的下载连接
        :type PreSignedUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PreSignedUrl = None
        self._RequestId = None

    @property
    def PreSignedUrl(self):
        """带签名的下载连接
        :rtype: str
        """
        return self._PreSignedUrl

    @PreSignedUrl.setter
    def PreSignedUrl(self, PreSignedUrl):
        self._PreSignedUrl = PreSignedUrl

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PreSignedUrl = params.get("PreSignedUrl")
        self._RequestId = params.get("RequestId")


class DescribeFlowRequest(AbstractModel):
    """DescribeFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步请求接口返回的任务流程号。
        :type FlowId: int
        """
        self._FlowId = None

    @property
    def FlowId(self):
        """异步请求接口返回的任务流程号。
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowResponse(AbstractModel):
    """DescribeFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 流程状态，0：成功，1：失败，2：运行中
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """流程状态，0：成功，1：失败，2：运行中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeLogFileRetentionPeriodRequest(AbstractModel):
    """DescribeLogFileRetentionPeriod请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例 ID，形如：tdsql-ow728lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogFileRetentionPeriodResponse(AbstractModel):
    """DescribeLogFileRetentionPeriod返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param _Days: 日志备份天数
        :type Days: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._Days = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """实例 ID，形如：tdsql-ow728lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Days(self):
        """日志备份天数
        :rtype: int
        """
        return self._Days

    @Days.setter
    def Days(self, Days):
        self._Days = Days

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Days = params.get("Days")
        self._RequestId = params.get("RequestId")


class DescribeOnlineDDLJobRequest(AbstractModel):
    """DescribeOnlineDDLJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _FlowId: Online DDL 对应的流程Id。创建任务时，CreateOnlineDDLJob 会返回此流程Id
        :type FlowId: int
        """
        self._InstanceId = None
        self._FlowId = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FlowId(self):
        """Online DDL 对应的流程Id。创建任务时，CreateOnlineDDLJob 会返回此流程Id
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOnlineDDLJobResponse(AbstractModel):
    """DescribeOnlineDDLJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。0：成功；1：失败；大于1：进行中
        :type Status: int
        :param _Process: 任务进度百分比
        :type Process: int
        :param _ErrorMessage: 错误信息或提示信息
        :type ErrorMessage: str
        :param _DDLDetails: 各分片DDL执行详情
        :type DDLDetails: list of DDLDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Process = None
        self._ErrorMessage = None
        self._DDLDetails = None
        self._RequestId = None

    @property
    def Status(self):
        """任务状态。0：成功；1：失败；大于1：进行中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Process(self):
        """任务进度百分比
        :rtype: int
        """
        return self._Process

    @Process.setter
    def Process(self, Process):
        self._Process = Process

    @property
    def ErrorMessage(self):
        """错误信息或提示信息
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def DDLDetails(self):
        """各分片DDL执行详情
        :rtype: list of DDLDetail
        """
        return self._DDLDetails

    @DDLDetails.setter
    def DDLDetails(self, DDLDetails):
        self._DDLDetails = DDLDetails

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Process = params.get("Process")
        self._ErrorMessage = params.get("ErrorMessage")
        if params.get("DDLDetails") is not None:
            self._DDLDetails = []
            for item in params.get("DDLDetails"):
                obj = DDLDetail()
                obj._deserialize(item)
                self._DDLDetails.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOrdersRequest(AbstractModel):
    """DescribeOrders请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DealNames: 待查询的长订单号列表，创建实例、续费实例、扩容实例接口返回。
        :type DealNames: list of str
        """
        self._DealNames = None

    @property
    def DealNames(self):
        """待查询的长订单号列表，创建实例、续费实例、扩容实例接口返回。
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames


    def _deserialize(self, params):
        self._DealNames = params.get("DealNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrdersResponse(AbstractModel):
    """DescribeOrders返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回的订单数量。
        :type TotalCount: int
        :param _Deals: 订单信息列表。
        :type Deals: list of Deal
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Deals = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """返回的订单数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Deals(self):
        """订单信息列表。
        :rtype: list of Deal
        """
        return self._Deals

    @Deals.setter
    def Deals(self, Deals):
        self._Deals = Deals

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Deals") is not None:
            self._Deals = []
            for item in params.get("Deals"):
                obj = Deal()
                obj._deserialize(item)
                self._Deals.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 数据库引擎名称，本接口取值：dcdb。
        :type Product: str
        :param _ProjectId: 项目ID。
        :type ProjectId: int
        """
        self._Product = None
        self._ProjectId = None

    @property
    def Product(self):
        """数据库引擎名称，本接口取值：dcdb。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def ProjectId(self):
        """项目ID。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectSecurityGroupsResponse(AbstractModel):
    """DescribeProjectSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Groups: 安全组详情。
        :type Groups: list of SecurityGroup
        :param _Total: 安全组个数。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Groups = None
        self._Total = None
        self._RequestId = None

    @property
    def Groups(self):
        """安全组详情。
        :rtype: list of SecurityGroup
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def Total(self):
        """安全组个数。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeProjectsRequest(AbstractModel):
    """DescribeProjects请求参数结构体

    """


class DescribeProjectsResponse(AbstractModel):
    """DescribeProjects返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Projects: 项目列表
        :type Projects: list of Project
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Projects = None
        self._RequestId = None

    @property
    def Projects(self):
        """项目列表
        :rtype: list of Project
        """
        return self._Projects

    @Projects.setter
    def Projects(self, Projects):
        self._Projects = Projects

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Projects") is not None:
            self._Projects = []
            for item in params.get("Projects"):
                obj = Project()
                obj._deserialize(item)
                self._Projects.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeShardSpecRequest(AbstractModel):
    """DescribeShardSpec请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CpuType: Cpu类型，如：英特尔：Intel/AMD，海光：Hygon，默认Intel/AMD
        :type CpuType: str
        """
        self._CpuType = None

    @property
    def CpuType(self):
        """Cpu类型，如：英特尔：Intel/AMD，海光：Hygon，默认Intel/AMD
        :rtype: str
        """
        return self._CpuType

    @CpuType.setter
    def CpuType(self, CpuType):
        self._CpuType = CpuType


    def _deserialize(self, params):
        self._CpuType = params.get("CpuType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShardSpecResponse(AbstractModel):
    """DescribeShardSpec返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SpecConfig: 按机型分类的可售卖规格列表
        :type SpecConfig: list of SpecConfig
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SpecConfig = None
        self._RequestId = None

    @property
    def SpecConfig(self):
        """按机型分类的可售卖规格列表
        :rtype: list of SpecConfig
        """
        return self._SpecConfig

    @SpecConfig.setter
    def SpecConfig(self, SpecConfig):
        self._SpecConfig = SpecConfig

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SpecConfig") is not None:
            self._SpecConfig = []
            for item in params.get("SpecConfig"):
                obj = SpecConfig()
                obj._deserialize(item)
                self._SpecConfig.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserTasksRequest(AbstractModel):
    """DescribeUserTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Statuses: 任务的状态列表。0-任务启动中；1-任务运行中；2-任务成功；3-任务失败
        :type Statuses: list of int
        :param _InstanceIds: 实例ID列表
        :type InstanceIds: list of str
        :param _FlowTypes: 任务类型列表，当前支持的任务类型有：0-回档任务；1-创建实例任务；2-扩容任务；3-迁移任务；4-删除实例任务；5-重启任务
        :type FlowTypes: list of int
        :param _StartTime: 任务的创建时间
        :type StartTime: str
        :param _EndTime: 任务的结束时间
        :type EndTime: str
        :param _UTaskIds: 任务ID的数组
        :type UTaskIds: list of int
        :param _Limit: 每次最多返回多少条任务，取值范围为(0,100]，不传的话默认值为20
        :type Limit: int
        :param _Offset: 返回任务默认是按照创建时间降序排列，从偏移值Offset处开始返回
        :type Offset: int
        """
        self._Statuses = None
        self._InstanceIds = None
        self._FlowTypes = None
        self._StartTime = None
        self._EndTime = None
        self._UTaskIds = None
        self._Limit = None
        self._Offset = None

    @property
    def Statuses(self):
        """任务的状态列表。0-任务启动中；1-任务运行中；2-任务成功；3-任务失败
        :rtype: list of int
        """
        return self._Statuses

    @Statuses.setter
    def Statuses(self, Statuses):
        self._Statuses = Statuses

    @property
    def InstanceIds(self):
        """实例ID列表
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def FlowTypes(self):
        """任务类型列表，当前支持的任务类型有：0-回档任务；1-创建实例任务；2-扩容任务；3-迁移任务；4-删除实例任务；5-重启任务
        :rtype: list of int
        """
        return self._FlowTypes

    @FlowTypes.setter
    def FlowTypes(self, FlowTypes):
        self._FlowTypes = FlowTypes

    @property
    def StartTime(self):
        """任务的创建时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """任务的结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def UTaskIds(self):
        """任务ID的数组
        :rtype: list of int
        """
        return self._UTaskIds

    @UTaskIds.setter
    def UTaskIds(self, UTaskIds):
        self._UTaskIds = UTaskIds

    @property
    def Limit(self):
        """每次最多返回多少条任务，取值范围为(0,100]，不传的话默认值为20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """返回任务默认是按照创建时间降序排列，从偏移值Offset处开始返回
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Statuses = params.get("Statuses")
        self._InstanceIds = params.get("InstanceIds")
        self._FlowTypes = params.get("FlowTypes")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._UTaskIds = params.get("UTaskIds")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserTasksResponse(AbstractModel):
    """DescribeUserTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 任务总数
        :type TotalCount: int
        :param _FlowSet: 任务列表
        :type FlowSet: list of UserTaskInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._FlowSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """任务总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def FlowSet(self):
        """任务列表
        :rtype: list of UserTaskInfo
        """
        return self._FlowSet

    @FlowSet.setter
    def FlowSet(self, FlowSet):
        self._FlowSet = FlowSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("FlowSet") is not None:
            self._FlowSet = []
            for item in params.get("FlowSet"):
                obj = UserTaskInfo()
                obj._deserialize(item)
                self._FlowSet.append(obj)
        self._RequestId = params.get("RequestId")


class DestroyDCDBInstanceRequest(AbstractModel):
    """DestroyDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：tdsqlshard-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例 ID，格式如：tdsqlshard-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyDCDBInstanceResponse(AbstractModel):
    """DestroyDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，与入参InstanceId一致。
        :type InstanceId: str
        :param _FlowId: 异步任务的请求 ID，可使用此 ID [查询异步任务的执行结果](https://cloud.tencent.com/document/product/557/56485)。
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._FlowId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """实例 ID，与入参InstanceId一致。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FlowId(self):
        """异步任务的请求 ID，可使用此 ID [查询异步任务的执行结果](https://cloud.tencent.com/document/product/557/56485)。
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class DestroyHourDCDBInstanceRequest(AbstractModel):
    """DestroyHourDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：tdsqlshard-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例 ID，格式如：tdsqlshard-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyHourDCDBInstanceResponse(AbstractModel):
    """DestroyHourDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步任务的请求 ID，可使用此 ID [查询异步任务的执行结果](https://cloud.tencent.com/document/product/557/56485)。
        :type FlowId: int
        :param _InstanceId: 实例 ID，与入参InstanceId一致。
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._InstanceId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """异步任务的请求 ID，可使用此 ID [查询异步任务的执行结果](https://cloud.tencent.com/document/product/557/56485)。
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceId(self):
        """实例 ID，与入参InstanceId一致。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 数据库引擎名称，本接口取值：dcdb。
        :type Product: str
        :param _SecurityGroupId: 安全组Id。
        :type SecurityGroupId: str
        :param _InstanceIds: 实例ID列表，一个或者多个实例Id组成的数组。
        :type InstanceIds: list of str
        """
        self._Product = None
        self._SecurityGroupId = None
        self._InstanceIds = None

    @property
    def Product(self):
        """数据库引擎名称，本接口取值：dcdb。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def SecurityGroupId(self):
        """安全组Id。
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def InstanceIds(self):
        """实例ID列表，一个或者多个实例Id组成的数组。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ExpandShardConfig(AbstractModel):
    """升级实例 -- 扩容分片类型

    """

    def __init__(self):
        r"""
        :param _ShardInstanceIds: 分片ID数组
        :type ShardInstanceIds: list of str
        :param _ShardMemory: 分片内存大小，单位 GB
        :type ShardMemory: int
        :param _ShardStorage: 分片存储大小，单位 GB
        :type ShardStorage: int
        :param _ShardNodeCount: 分片节点数
        :type ShardNodeCount: int
        """
        self._ShardInstanceIds = None
        self._ShardMemory = None
        self._ShardStorage = None
        self._ShardNodeCount = None

    @property
    def ShardInstanceIds(self):
        """分片ID数组
        :rtype: list of str
        """
        return self._ShardInstanceIds

    @ShardInstanceIds.setter
    def ShardInstanceIds(self, ShardInstanceIds):
        self._ShardInstanceIds = ShardInstanceIds

    @property
    def ShardMemory(self):
        """分片内存大小，单位 GB
        :rtype: int
        """
        return self._ShardMemory

    @ShardMemory.setter
    def ShardMemory(self, ShardMemory):
        self._ShardMemory = ShardMemory

    @property
    def ShardStorage(self):
        """分片存储大小，单位 GB
        :rtype: int
        """
        return self._ShardStorage

    @ShardStorage.setter
    def ShardStorage(self, ShardStorage):
        self._ShardStorage = ShardStorage

    @property
    def ShardNodeCount(self):
        """分片节点数
        :rtype: int
        """
        return self._ShardNodeCount

    @ShardNodeCount.setter
    def ShardNodeCount(self, ShardNodeCount):
        self._ShardNodeCount = ShardNodeCount


    def _deserialize(self, params):
        self._ShardInstanceIds = params.get("ShardInstanceIds")
        self._ShardMemory = params.get("ShardMemory")
        self._ShardStorage = params.get("ShardStorage")
        self._ShardNodeCount = params.get("ShardNodeCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlushBinlogRequest(AbstractModel):
    """FlushBinlog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlushBinlogResponse(AbstractModel):
    """FlushBinlog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class GrantAccountPrivilegesRequest(AbstractModel):
    """GrantAccountPrivileges请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param _UserName: 登录用户名。
        :type UserName: str
        :param _Host: 用户允许的访问 host，用户名+host唯一确定一个账号。
        :type Host: str
        :param _DbName: 数据库名。如果为 \*，表示查询全局权限（即 \*.\*），此时忽略 Type 和 Object 参数
        :type DbName: str
        :param _Privileges: 全局权限： SELECT，INSERT，UPDATE，DELETE，CREATE，DROP，REFERENCES，INDEX，ALTER，CREATE TEMPORARY TABLES，LOCK TABLES，EXECUTE，CREATE VIEW，SHOW VIEW，CREATE ROUTINE，ALTER ROUTINE，EVENT，TRIGGER，SHOW DATABASES，REPLICATION CLIENT，REPLICATION SLAVE
库权限： SELECT，INSERT，UPDATE，DELETE，CREATE，DROP，REFERENCES，INDEX，ALTER，CREATE TEMPORARY TABLES，LOCK TABLES，EXECUTE，CREATE VIEW，SHOW VIEW，CREATE ROUTINE，ALTER ROUTINE，EVENT，TRIGGER 
表权限： SELECT，INSERT，UPDATE，DELETE，CREATE，DROP，REFERENCES，INDEX，ALTER，CREATE VIEW，SHOW VIEW，TRIGGER  
字段权限： INSERT，REFERENCES，SELECT，UPDATE
        :type Privileges: list of str
        :param _Type: 类型,可以填入 table 和 \*。当 DbName 为具体数据库名，Type为 \* 时，表示设置该数据库权限（即db.\*），此时忽略 Object 参数
        :type Type: str
        :param _Object: 具体的 Type 的名称，例如 Type 为 table 时就是具体的表名。DbName 和 Type 都为具体名称，则 Object 表示具体对象名，不能为 \* 或者为空
        :type Object: str
        :param _ColName: 当 Type=table 时，ColName 为 \* 表示对表授权，如果为具体字段名，表示对字段授权
        :type ColName: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Host = None
        self._DbName = None
        self._Privileges = None
        self._Type = None
        self._Object = None
        self._ColName = None

    @property
    def InstanceId(self):
        """实例 ID，形如：dcdbt-ow728lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        """登录用户名。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        """用户允许的访问 host，用户名+host唯一确定一个账号。
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def DbName(self):
        """数据库名。如果为 \*，表示查询全局权限（即 \*.\*），此时忽略 Type 和 Object 参数
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Privileges(self):
        """全局权限： SELECT，INSERT，UPDATE，DELETE，CREATE，DROP，REFERENCES，INDEX，ALTER，CREATE TEMPORARY TABLES，LOCK TABLES，EXECUTE，CREATE VIEW，SHOW VIEW，CREATE ROUTINE，ALTER ROUTINE，EVENT，TRIGGER，SHOW DATABASES，REPLICATION CLIENT，REPLICATION SLAVE
库权限： SELECT，INSERT，UPDATE，DELETE，CREATE，DROP，REFERENCES，INDEX，ALTER，CREATE TEMPORARY TABLES，LOCK TABLES，EXECUTE，CREATE VIEW，SHOW VIEW，CREATE ROUTINE，ALTER ROUTINE，EVENT，TRIGGER 
表权限： SELECT，INSERT，UPDATE，DELETE，CREATE，DROP，REFERENCES，INDEX，ALTER，CREATE VIEW，SHOW VIEW，TRIGGER  
字段权限： INSERT，REFERENCES，SELECT，UPDATE
        :rtype: list of str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges

    @property
    def Type(self):
        """类型,可以填入 table 和 \*。当 DbName 为具体数据库名，Type为 \* 时，表示设置该数据库权限（即db.\*），此时忽略 Object 参数
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Object(self):
        """具体的 Type 的名称，例如 Type 为 table 时就是具体的表名。DbName 和 Type 都为具体名称，则 Object 表示具体对象名，不能为 \* 或者为空
        :rtype: str
        """
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object

    @property
    def ColName(self):
        """当 Type=table 时，ColName 为 \* 表示对表授权，如果为具体字段名，表示对字段授权
        :rtype: str
        """
        return self._ColName

    @ColName.setter
    def ColName(self, ColName):
        self._ColName = ColName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._DbName = params.get("DbName")
        self._Privileges = params.get("Privileges")
        self._Type = params.get("Type")
        self._Object = params.get("Object")
        self._ColName = params.get("ColName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrantAccountPrivilegesResponse(AbstractModel):
    """GrantAccountPrivileges返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class InitDCDBInstancesRequest(AbstractModel):
    """InitDCDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 待初始化的实例ID列表，形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceIds: list of str
        :param _Params: 参数列表。本接口的可选值为：character_set_server（字符集，必传），lower_case_table_names（表名大小写敏感，必传，0 - 敏感；1-不敏感），innodb_page_size（innodb数据页，默认16K），sync_mode（同步模式：0 - 异步； 1 - 强同步；2 - 强同步可退化。默认为强同步）。
        :type Params: list of DBParamValue
        """
        self._InstanceIds = None
        self._Params = None

    @property
    def InstanceIds(self):
        """待初始化的实例ID列表，形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Params(self):
        """参数列表。本接口的可选值为：character_set_server（字符集，必传），lower_case_table_names（表名大小写敏感，必传，0 - 敏感；1-不敏感），innodb_page_size（innodb数据页，默认16K），sync_mode（同步模式：0 - 异步； 1 - 强同步；2 - 强同步可退化。默认为强同步）。
        :rtype: list of DBParamValue
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("Params") is not None:
            self._Params = []
            for item in params.get("Params"):
                obj = DBParamValue()
                obj._deserialize(item)
                self._Params.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitDCDBInstancesResponse(AbstractModel):
    """InitDCDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowIds: 异步任务ID，可通过 DescribeFlow 查询任务状态。
        :type FlowIds: list of int non-negative
        :param _InstanceIds: 透传入参。
        :type InstanceIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowIds = None
        self._InstanceIds = None
        self._RequestId = None

    @property
    def FlowIds(self):
        """异步任务ID，可通过 DescribeFlow 查询任务状态。
        :rtype: list of int non-negative
        """
        return self._FlowIds

    @FlowIds.setter
    def FlowIds(self, FlowIds):
        self._FlowIds = FlowIds

    @property
    def InstanceIds(self):
        """透传入参。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowIds = params.get("FlowIds")
        self._InstanceIds = params.get("InstanceIds")
        self._RequestId = params.get("RequestId")


class InstanceBackupFileItem(AbstractModel):
    """实例备份文件信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _InstanceStatus: 实例状态
        :type InstanceStatus: int
        :param _ShardId: 分片ID
        :type ShardId: str
        :param _FilePath: 文件路径
        :type FilePath: str
        :param _FileName: 文件名
        :type FileName: str
        :param _FileSize: 文件大小
        :type FileSize: int
        :param _BackupType: 备份类型，Data:数据备份，Binlog:Binlog备份，Errlog:错误日志，Slowlog:慢日志
        :type BackupType: str
        :param _ManualBackup: 手动备份，0:否，1:是
        :type ManualBackup: int
        :param _StartTime: 备份开始时间
        :type StartTime: str
        :param _EndTime: 备份结束时间
        :type EndTime: str
        :param _StorageClass: 对象的存储类型，枚举值：STANDARD（标准存储）、ARCHIVE（归档存储）。
        :type StorageClass: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceStatus = None
        self._ShardId = None
        self._FilePath = None
        self._FileName = None
        self._FileSize = None
        self._BackupType = None
        self._ManualBackup = None
        self._StartTime = None
        self._EndTime = None
        self._StorageClass = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceStatus(self):
        """实例状态
        :rtype: int
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def ShardId(self):
        """分片ID
        :rtype: str
        """
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def FilePath(self):
        """文件路径
        :rtype: str
        """
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def FileName(self):
        """文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        """文件大小
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def BackupType(self):
        """备份类型，Data:数据备份，Binlog:Binlog备份，Errlog:错误日志，Slowlog:慢日志
        :rtype: str
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def ManualBackup(self):
        """手动备份，0:否，1:是
        :rtype: int
        """
        return self._ManualBackup

    @ManualBackup.setter
    def ManualBackup(self, ManualBackup):
        self._ManualBackup = ManualBackup

    @property
    def StartTime(self):
        """备份开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """备份结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StorageClass(self):
        """对象的存储类型，枚举值：STANDARD（标准存储）、ARCHIVE（归档存储）。
        :rtype: str
        """
        return self._StorageClass

    @StorageClass.setter
    def StorageClass(self, StorageClass):
        self._StorageClass = StorageClass


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceStatus = params.get("InstanceStatus")
        self._ShardId = params.get("ShardId")
        self._FilePath = params.get("FilePath")
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._BackupType = params.get("BackupType")
        self._ManualBackup = params.get("ManualBackup")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._StorageClass = params.get("StorageClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDCDBInstanceRequest(AbstractModel):
    """IsolateDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例 ID，格式如：tdsqlshard-avw0207d，与云数据库控制台页面中显示的实例 ID 相同，可使用 查询实例列表 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        """实例 ID，格式如：tdsqlshard-avw0207d，与云数据库控制台页面中显示的实例 ID 相同，可使用 查询实例列表 接口获取，其值为输出参数中字段 InstanceId 的值。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDCDBInstanceResponse(AbstractModel):
    """IsolateDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuccessInstanceIds: 隔离成功实例ID列表。
        :type SuccessInstanceIds: list of str
        :param _FailedInstanceIds: 隔离失败实例ID列表。
        :type FailedInstanceIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessInstanceIds = None
        self._FailedInstanceIds = None
        self._RequestId = None

    @property
    def SuccessInstanceIds(self):
        """隔离成功实例ID列表。
        :rtype: list of str
        """
        return self._SuccessInstanceIds

    @SuccessInstanceIds.setter
    def SuccessInstanceIds(self, SuccessInstanceIds):
        self._SuccessInstanceIds = SuccessInstanceIds

    @property
    def FailedInstanceIds(self):
        """隔离失败实例ID列表。
        :rtype: list of str
        """
        return self._FailedInstanceIds

    @FailedInstanceIds.setter
    def FailedInstanceIds(self, FailedInstanceIds):
        self._FailedInstanceIds = FailedInstanceIds

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessInstanceIds = params.get("SuccessInstanceIds")
        self._FailedInstanceIds = params.get("FailedInstanceIds")
        self._RequestId = params.get("RequestId")


class IsolateDedicatedDBInstanceRequest(AbstractModel):
    """IsolateDedicatedDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 Id，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例 Id，形如：dcdbt-ow728lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDedicatedDBInstanceResponse(AbstractModel):
    """IsolateDedicatedDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class IsolateHourDCDBInstanceRequest(AbstractModel):
    """IsolateHourDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 待升级的实例ID列表。形如：["dcdbt-ow728lmc"]，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        """待升级的实例ID列表。形如：["dcdbt-ow728lmc"]，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateHourDCDBInstanceResponse(AbstractModel):
    """IsolateHourDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuccessInstanceIds: 隔离成功的实例id列表
        :type SuccessInstanceIds: list of str
        :param _FailedInstanceIds: 隔离失败的实例id列表
        :type FailedInstanceIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessInstanceIds = None
        self._FailedInstanceIds = None
        self._RequestId = None

    @property
    def SuccessInstanceIds(self):
        """隔离成功的实例id列表
        :rtype: list of str
        """
        return self._SuccessInstanceIds

    @SuccessInstanceIds.setter
    def SuccessInstanceIds(self, SuccessInstanceIds):
        self._SuccessInstanceIds = SuccessInstanceIds

    @property
    def FailedInstanceIds(self):
        """隔离失败的实例id列表
        :rtype: list of str
        """
        return self._FailedInstanceIds

    @FailedInstanceIds.setter
    def FailedInstanceIds(self, FailedInstanceIds):
        self._FailedInstanceIds = FailedInstanceIds

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessInstanceIds = params.get("SuccessInstanceIds")
        self._FailedInstanceIds = params.get("FailedInstanceIds")
        self._RequestId = params.get("RequestId")


class KillSessionRequest(AbstractModel):
    """KillSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _SessionId: 会话ID列表
        :type SessionId: list of int
        :param _ShardId: 分片ID，与ShardSerialId设置一个
        :type ShardId: str
        :param _ShardSerialId: 分片序列ID，与ShardId设置一个
        :type ShardSerialId: str
        """
        self._InstanceId = None
        self._SessionId = None
        self._ShardId = None
        self._ShardSerialId = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SessionId(self):
        """会话ID列表
        :rtype: list of int
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def ShardId(self):
        """分片ID，与ShardSerialId设置一个
        :rtype: str
        """
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def ShardSerialId(self):
        """分片序列ID，与ShardId设置一个
        :rtype: str
        """
        return self._ShardSerialId

    @ShardSerialId.setter
    def ShardSerialId(self, ShardSerialId):
        self._ShardSerialId = ShardSerialId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SessionId = params.get("SessionId")
        self._ShardId = params.get("ShardId")
        self._ShardSerialId = params.get("ShardSerialId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillSessionResponse(AbstractModel):
    """KillSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class LogFileInfo(AbstractModel):
    """拉取的日志信息

    """

    def __init__(self):
        r"""
        :param _Mtime: Log最后修改时间
        :type Mtime: int
        :param _Length: 文件长度
        :type Length: int
        :param _Uri: 下载Log时用到的统一资源标识符
        :type Uri: str
        :param _FileName: 文件名
        :type FileName: str
        """
        self._Mtime = None
        self._Length = None
        self._Uri = None
        self._FileName = None

    @property
    def Mtime(self):
        """Log最后修改时间
        :rtype: int
        """
        return self._Mtime

    @Mtime.setter
    def Mtime(self, Mtime):
        self._Mtime = Mtime

    @property
    def Length(self):
        """文件长度
        :rtype: int
        """
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def Uri(self):
        """下载Log时用到的统一资源标识符
        :rtype: str
        """
        return self._Uri

    @Uri.setter
    def Uri(self, Uri):
        self._Uri = Uri

    @property
    def FileName(self):
        """文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName


    def _deserialize(self, params):
        self._Mtime = params.get("Mtime")
        self._Length = params.get("Length")
        self._Uri = params.get("Uri")
        self._FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountConfigRequest(AbstractModel):
    """ModifyAccountConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：tdsqlshard-kpkvq5oj，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _UserName: 账号的名称
        :type UserName: str
        :param _Host: 账号的域名
        :type Host: str
        :param _Configs: 配置列表，每一个元素是Config和Value的组合
        :type Configs: list of ConfigValue
        """
        self._InstanceId = None
        self._UserName = None
        self._Host = None
        self._Configs = None

    @property
    def InstanceId(self):
        """实例 ID，格式如：tdsqlshard-kpkvq5oj，与云数据库控制台页面中显示的实例 ID 相同。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        """账号的名称
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        """账号的域名
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Configs(self):
        """配置列表，每一个元素是Config和Value的组合
        :rtype: list of ConfigValue
        """
        return self._Configs

    @Configs.setter
    def Configs(self, Configs):
        self._Configs = Configs


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        if params.get("Configs") is not None:
            self._Configs = []
            for item in params.get("Configs"):
                obj = ConfigValue()
                obj._deserialize(item)
                self._Configs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountConfigResponse(AbstractModel):
    """ModifyAccountConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyAccountDescriptionRequest(AbstractModel):
    """ModifyAccountDescription请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param _UserName: 登录用户名。
        :type UserName: str
        :param _Host: 用户允许的访问 host，用户名+host唯一确定一个账号。
        :type Host: str
        :param _Description: 新的账号备注，长度 0~256。
        :type Description: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Host = None
        self._Description = None

    @property
    def InstanceId(self):
        """实例 ID，形如：dcdbt-ow728lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        """登录用户名。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        """用户允许的访问 host，用户名+host唯一确定一个账号。
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Description(self):
        """新的账号备注，长度 0~256。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountDescriptionResponse(AbstractModel):
    """ModifyAccountDescription返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyAccountPrivilegesRequest(AbstractModel):
    """ModifyAccountPrivileges请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：tdsql-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _Accounts: 数据库的账号，包括用户名和域名。
        :type Accounts: list of Account
        :param _GlobalPrivileges: 全局权限。其中，GlobalPrivileges 中权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE", "PROCESS", "DROP","REFERENCES","INDEX","ALTER","SHOW DATABASES","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER"。
注意，不传该参数表示保留现有权限，如需清除，该字段传空数组。
        :type GlobalPrivileges: list of str
        :param _DatabasePrivileges: 数据库的权限。Privileges 权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE", "DROP","REFERENCES","INDEX","ALTER","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER"。
注意，不传该参数表示保留现有权限，如需清除，请在复杂类型Privileges字段传空数组。
        :type DatabasePrivileges: list of DatabasePrivilege
        :param _TablePrivileges: 数据库中表的权限。Privileges 权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE", "DROP","REFERENCES","INDEX","ALTER","CREATE VIEW","SHOW VIEW", "TRIGGER"。
注意，不传该参数表示保留现有权限，如需清除，请在复杂类型Privileges字段传空数组。
        :type TablePrivileges: list of TablePrivilege
        :param _ColumnPrivileges: 数据库表中列的权限。Privileges 权限的可选值为："SELECT","INSERT","UPDATE","REFERENCES"。
注意，不传该参数表示保留现有权限，如需清除，请在复杂类型Privileges字段传空数组。
        :type ColumnPrivileges: list of ColumnPrivilege
        :param _ViewPrivileges: 数据库视图的权限。Privileges 权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE", "DROP","REFERENCES","INDEX","ALTER","CREATE VIEW","SHOW VIEW", "TRIGGER"。
注意，不传该参数表示保留现有权限，如需清除，请在复杂类型Privileges字段传空数组。
        :type ViewPrivileges: list of ViewPrivileges
        """
        self._InstanceId = None
        self._Accounts = None
        self._GlobalPrivileges = None
        self._DatabasePrivileges = None
        self._TablePrivileges = None
        self._ColumnPrivileges = None
        self._ViewPrivileges = None

    @property
    def InstanceId(self):
        """实例 ID，格式如：tdsql-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        """数据库的账号，包括用户名和域名。
        :rtype: list of Account
        """
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def GlobalPrivileges(self):
        """全局权限。其中，GlobalPrivileges 中权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE", "PROCESS", "DROP","REFERENCES","INDEX","ALTER","SHOW DATABASES","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER"。
注意，不传该参数表示保留现有权限，如需清除，该字段传空数组。
        :rtype: list of str
        """
        return self._GlobalPrivileges

    @GlobalPrivileges.setter
    def GlobalPrivileges(self, GlobalPrivileges):
        self._GlobalPrivileges = GlobalPrivileges

    @property
    def DatabasePrivileges(self):
        """数据库的权限。Privileges 权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE", "DROP","REFERENCES","INDEX","ALTER","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER"。
注意，不传该参数表示保留现有权限，如需清除，请在复杂类型Privileges字段传空数组。
        :rtype: list of DatabasePrivilege
        """
        return self._DatabasePrivileges

    @DatabasePrivileges.setter
    def DatabasePrivileges(self, DatabasePrivileges):
        self._DatabasePrivileges = DatabasePrivileges

    @property
    def TablePrivileges(self):
        """数据库中表的权限。Privileges 权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE", "DROP","REFERENCES","INDEX","ALTER","CREATE VIEW","SHOW VIEW", "TRIGGER"。
注意，不传该参数表示保留现有权限，如需清除，请在复杂类型Privileges字段传空数组。
        :rtype: list of TablePrivilege
        """
        return self._TablePrivileges

    @TablePrivileges.setter
    def TablePrivileges(self, TablePrivileges):
        self._TablePrivileges = TablePrivileges

    @property
    def ColumnPrivileges(self):
        """数据库表中列的权限。Privileges 权限的可选值为："SELECT","INSERT","UPDATE","REFERENCES"。
注意，不传该参数表示保留现有权限，如需清除，请在复杂类型Privileges字段传空数组。
        :rtype: list of ColumnPrivilege
        """
        return self._ColumnPrivileges

    @ColumnPrivileges.setter
    def ColumnPrivileges(self, ColumnPrivileges):
        self._ColumnPrivileges = ColumnPrivileges

    @property
    def ViewPrivileges(self):
        """数据库视图的权限。Privileges 权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE", "DROP","REFERENCES","INDEX","ALTER","CREATE VIEW","SHOW VIEW", "TRIGGER"。
注意，不传该参数表示保留现有权限，如需清除，请在复杂类型Privileges字段传空数组。
        :rtype: list of ViewPrivileges
        """
        return self._ViewPrivileges

    @ViewPrivileges.setter
    def ViewPrivileges(self, ViewPrivileges):
        self._ViewPrivileges = ViewPrivileges


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._GlobalPrivileges = params.get("GlobalPrivileges")
        if params.get("DatabasePrivileges") is not None:
            self._DatabasePrivileges = []
            for item in params.get("DatabasePrivileges"):
                obj = DatabasePrivilege()
                obj._deserialize(item)
                self._DatabasePrivileges.append(obj)
        if params.get("TablePrivileges") is not None:
            self._TablePrivileges = []
            for item in params.get("TablePrivileges"):
                obj = TablePrivilege()
                obj._deserialize(item)
                self._TablePrivileges.append(obj)
        if params.get("ColumnPrivileges") is not None:
            self._ColumnPrivileges = []
            for item in params.get("ColumnPrivileges"):
                obj = ColumnPrivilege()
                obj._deserialize(item)
                self._ColumnPrivileges.append(obj)
        if params.get("ViewPrivileges") is not None:
            self._ViewPrivileges = []
            for item in params.get("ViewPrivileges"):
                obj = ViewPrivileges()
                obj._deserialize(item)
                self._ViewPrivileges.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountPrivilegesResponse(AbstractModel):
    """ModifyAccountPrivileges返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步任务的请求 ID，可使用此 ID [查询异步任务的执行结果](https://cloud.tencent.com/document/product/237/16177)。
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """异步任务的请求 ID，可使用此 ID [查询异步任务的执行结果](https://cloud.tencent.com/document/product/237/16177)。
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyBackupConfigsRequest(AbstractModel):
    """ModifyBackupConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：tdsqlshard-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _Days: 常规备份存储时长，范围[1, 3650]。
        :type Days: int
        :param _StartBackupTime: 每天备份执行的区间的开始时间，格式 mm:ss，形如 22:00。
        :type StartBackupTime: str
        :param _EndBackupTime: 每天备份执行的区间的结束时间，格式 mm:ss，形如 23:59。
        :type EndBackupTime: str
        :param _WeekDays: 执行备份周期，枚举值：Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday
        :type WeekDays: list of str
        :param _ArchiveDays: 沉降到归档存储时长，-1表示关闭归档设置。
        :type ArchiveDays: int
        :param _BackupConfigSet: 超期备份配置。
        :type BackupConfigSet: list of NewBackupConfig
        """
        self._InstanceId = None
        self._Days = None
        self._StartBackupTime = None
        self._EndBackupTime = None
        self._WeekDays = None
        self._ArchiveDays = None
        self._BackupConfigSet = None

    @property
    def InstanceId(self):
        """实例 ID，格式如：tdsqlshard-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Days(self):
        """常规备份存储时长，范围[1, 3650]。
        :rtype: int
        """
        return self._Days

    @Days.setter
    def Days(self, Days):
        self._Days = Days

    @property
    def StartBackupTime(self):
        """每天备份执行的区间的开始时间，格式 mm:ss，形如 22:00。
        :rtype: str
        """
        return self._StartBackupTime

    @StartBackupTime.setter
    def StartBackupTime(self, StartBackupTime):
        self._StartBackupTime = StartBackupTime

    @property
    def EndBackupTime(self):
        """每天备份执行的区间的结束时间，格式 mm:ss，形如 23:59。
        :rtype: str
        """
        return self._EndBackupTime

    @EndBackupTime.setter
    def EndBackupTime(self, EndBackupTime):
        self._EndBackupTime = EndBackupTime

    @property
    def WeekDays(self):
        """执行备份周期，枚举值：Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday
        :rtype: list of str
        """
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays

    @property
    def ArchiveDays(self):
        """沉降到归档存储时长，-1表示关闭归档设置。
        :rtype: int
        """
        return self._ArchiveDays

    @ArchiveDays.setter
    def ArchiveDays(self, ArchiveDays):
        self._ArchiveDays = ArchiveDays

    @property
    def BackupConfigSet(self):
        """超期备份配置。
        :rtype: list of NewBackupConfig
        """
        return self._BackupConfigSet

    @BackupConfigSet.setter
    def BackupConfigSet(self, BackupConfigSet):
        self._BackupConfigSet = BackupConfigSet


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Days = params.get("Days")
        self._StartBackupTime = params.get("StartBackupTime")
        self._EndBackupTime = params.get("EndBackupTime")
        self._WeekDays = params.get("WeekDays")
        self._ArchiveDays = params.get("ArchiveDays")
        if params.get("BackupConfigSet") is not None:
            self._BackupConfigSet = []
            for item in params.get("BackupConfigSet"):
                obj = NewBackupConfig()
                obj._deserialize(item)
                self._BackupConfigSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupConfigsResponse(AbstractModel):
    """ModifyBackupConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDBEncryptAttributesRequest(AbstractModel):
    """ModifyDBEncryptAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id，形如：tdsqlshard-ow728lmc。
        :type InstanceId: str
        :param _EncryptEnabled: 是否启用数据加密，开启后暂不支持关闭。本接口的可选值为：1-开启数据加密。
        :type EncryptEnabled: int
        """
        self._InstanceId = None
        self._EncryptEnabled = None

    @property
    def InstanceId(self):
        """实例Id，形如：tdsqlshard-ow728lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EncryptEnabled(self):
        """是否启用数据加密，开启后暂不支持关闭。本接口的可选值为：1-开启数据加密。
        :rtype: int
        """
        return self._EncryptEnabled

    @EncryptEnabled.setter
    def EncryptEnabled(self, EncryptEnabled):
        self._EncryptEnabled = EncryptEnabled


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EncryptEnabled = params.get("EncryptEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBEncryptAttributesResponse(AbstractModel):
    """ModifyDBEncryptAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceNameRequest(AbstractModel):
    """ModifyDBInstanceName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，形如tdsql-hdaprz0v
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        """
        self._InstanceId = None
        self._InstanceName = None

    @property
    def InstanceId(self):
        """实例ID，形如tdsql-hdaprz0v
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceNameResponse(AbstractModel):
    """ModifyDBInstanceName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 数据库引擎名称，本接口取值：dcdb。
        :type Product: str
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _SecurityGroupIds: 要修改的安全组 ID 列表，一个或者多个安全组 ID 组成的数组。
        :type SecurityGroupIds: list of str
        """
        self._Product = None
        self._InstanceId = None
        self._SecurityGroupIds = None

    @property
    def Product(self):
        """数据库引擎名称，本接口取值：dcdb。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SecurityGroupIds(self):
        """要修改的安全组 ID 列表，一个或者多个安全组 ID 组成的数组。
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._InstanceId = params.get("InstanceId")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSecurityGroupsResponse(AbstractModel):
    """ModifyDBInstanceSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDBInstancesProjectRequest(AbstractModel):
    """ModifyDBInstancesProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 待修改的实例ID列表。实例 ID 形如：dcdbt-ow728lmc。
        :type InstanceIds: list of str
        :param _ProjectId: 要分配的项目 ID，可以通过 DescribeProjects 查询项目列表接口获取。
        :type ProjectId: int
        """
        self._InstanceIds = None
        self._ProjectId = None

    @property
    def InstanceIds(self):
        """待修改的实例ID列表。实例 ID 形如：dcdbt-ow728lmc。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ProjectId(self):
        """要分配的项目 ID，可以通过 DescribeProjects 查询项目列表接口获取。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstancesProjectResponse(AbstractModel):
    """ModifyDBInstancesProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDBParametersRequest(AbstractModel):
    """ModifyDBParameters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param _Params: 参数列表，每一个元素是Param和Value的组合
        :type Params: list of DBParamValue
        """
        self._InstanceId = None
        self._Params = None

    @property
    def InstanceId(self):
        """实例 ID，形如：dcdbt-ow728lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Params(self):
        """参数列表，每一个元素是Param和Value的组合
        :rtype: list of DBParamValue
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Params") is not None:
            self._Params = []
            for item in params.get("Params"):
                obj = DBParamValue()
                obj._deserialize(item)
                self._Params.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBParametersResponse(AbstractModel):
    """ModifyDBParameters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param _Result: 各参数修改结果
        :type Result: list of ParamModifyResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._Result = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """实例 ID，形如：dcdbt-ow728lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Result(self):
        """各参数修改结果
        :rtype: list of ParamModifyResult
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = ParamModifyResult()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyDBSyncModeRequest(AbstractModel):
    """ModifyDBSyncMode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 待修改同步模式的实例ID。形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param _SyncMode: 同步模式：0 异步，1 强同步， 2 强同步可退化
        :type SyncMode: int
        """
        self._InstanceId = None
        self._SyncMode = None

    @property
    def InstanceId(self):
        """待修改同步模式的实例ID。形如：dcdbt-ow728lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SyncMode(self):
        """同步模式：0 异步，1 强同步， 2 强同步可退化
        :rtype: int
        """
        return self._SyncMode

    @SyncMode.setter
    def SyncMode(self, SyncMode):
        self._SyncMode = SyncMode


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SyncMode = params.get("SyncMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBSyncModeResponse(AbstractModel):
    """ModifyDBSyncMode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步任务Id，可通过 DescribeFlow 查询任务状态。
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """异步任务Id，可通过 DescribeFlow 查询任务状态。
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceNetworkRequest(AbstractModel):
    """ModifyInstanceNetwork请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _VpcId: 希望转到的VPC网络的VpcId
        :type VpcId: str
        :param _SubnetId: 希望转到的VPC网络的子网ID
        :type SubnetId: str
        :param _Vip: 如果需要指定VIP，填上该字段
        :type Vip: str
        :param _Vipv6: 如果需要指定VIPv6，填上该字段
        :type Vipv6: str
        :param _VipReleaseDelay: VIP保留时长，单位小时，取值范围（0~168），0表示立即释放，有一分钟释放延迟。不传此参数，默认24小时释放VIP。
        :type VipReleaseDelay: int
        """
        self._InstanceId = None
        self._VpcId = None
        self._SubnetId = None
        self._Vip = None
        self._Vipv6 = None
        self._VipReleaseDelay = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VpcId(self):
        """希望转到的VPC网络的VpcId
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """希望转到的VPC网络的子网ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Vip(self):
        """如果需要指定VIP，填上该字段
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vipv6(self):
        """如果需要指定VIPv6，填上该字段
        :rtype: str
        """
        return self._Vipv6

    @Vipv6.setter
    def Vipv6(self, Vipv6):
        self._Vipv6 = Vipv6

    @property
    def VipReleaseDelay(self):
        """VIP保留时长，单位小时，取值范围（0~168），0表示立即释放，有一分钟释放延迟。不传此参数，默认24小时释放VIP。
        :rtype: int
        """
        return self._VipReleaseDelay

    @VipReleaseDelay.setter
    def VipReleaseDelay(self, VipReleaseDelay):
        self._VipReleaseDelay = VipReleaseDelay


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Vip = params.get("Vip")
        self._Vipv6 = params.get("Vipv6")
        self._VipReleaseDelay = params.get("VipReleaseDelay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceNetworkResponse(AbstractModel):
    """ModifyInstanceNetwork返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步任务ID，根据此FlowId通过DescribeFlow接口查询任务进行状态
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """异步任务ID，根据此FlowId通过DescribeFlow接口查询任务进行状态
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceVipRequest(AbstractModel):
    """ModifyInstanceVip请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Vip: 实例VIP
        :type Vip: str
        :param _Ipv6Flag: IPv6标志
        :type Ipv6Flag: int
        :param _VipReleaseDelay: VIP保留时长，单位小时，取值范围（0~168），0表示立即释放，有一分钟释放延迟。不传此参数，默认24小时释放VIP。
        :type VipReleaseDelay: int
        """
        self._InstanceId = None
        self._Vip = None
        self._Ipv6Flag = None
        self._VipReleaseDelay = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Vip(self):
        """实例VIP
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Ipv6Flag(self):
        """IPv6标志
        :rtype: int
        """
        return self._Ipv6Flag

    @Ipv6Flag.setter
    def Ipv6Flag(self, Ipv6Flag):
        self._Ipv6Flag = Ipv6Flag

    @property
    def VipReleaseDelay(self):
        """VIP保留时长，单位小时，取值范围（0~168），0表示立即释放，有一分钟释放延迟。不传此参数，默认24小时释放VIP。
        :rtype: int
        """
        return self._VipReleaseDelay

    @VipReleaseDelay.setter
    def VipReleaseDelay(self, VipReleaseDelay):
        self._VipReleaseDelay = VipReleaseDelay


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Vip = params.get("Vip")
        self._Ipv6Flag = params.get("Ipv6Flag")
        self._VipReleaseDelay = params.get("VipReleaseDelay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceVipResponse(AbstractModel):
    """ModifyInstanceVip返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步任务流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """异步任务流程ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceVportRequest(AbstractModel):
    """ModifyInstanceVport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Vport: 实例VPORT
        :type Vport: int
        """
        self._InstanceId = None
        self._Vport = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Vport(self):
        """实例VPORT
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceVportResponse(AbstractModel):
    """ModifyInstanceVport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyRealServerAccessStrategyRequest(AbstractModel):
    """ModifyRealServerAccessStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：tdsqlshard-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _RsAccessStrategy: RS就近模式, 0-无策略, 1-可用区就近访问。
        :type RsAccessStrategy: int
        """
        self._InstanceId = None
        self._RsAccessStrategy = None

    @property
    def InstanceId(self):
        """实例 ID，格式如：tdsqlshard-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RsAccessStrategy(self):
        """RS就近模式, 0-无策略, 1-可用区就近访问。
        :rtype: int
        """
        return self._RsAccessStrategy

    @RsAccessStrategy.setter
    def RsAccessStrategy(self, RsAccessStrategy):
        self._RsAccessStrategy = RsAccessStrategy


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RsAccessStrategy = params.get("RsAccessStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRealServerAccessStrategyResponse(AbstractModel):
    """ModifyRealServerAccessStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class NewBackupConfig(AbstractModel):
    """数据库超期备份配置

    """

    def __init__(self):
        r"""
        :param _EnableBackupPolicy: 备份策略是否启用。
        :type EnableBackupPolicy: bool
        :param _BeginDate: 超期保留开始日期，早于开始日期的超期备份不保留，格式：yyyy-mm-dd。
        :type BeginDate: str
        :param _MaxRetentionDays: 超期备份保留时长，超出保留时间的超期备份将被删除，可填写1-3650整数。
        :type MaxRetentionDays: int
        :param _Frequency: 备份模式，可选择按年月周模式保存
* 按年：annually
* 按月：monthly
* 按周：weekly
        :type Frequency: str
        :param _WeekDays: Frequency等于weekly时生效。
表示保留特定工作日备份。可选择周一到周日，支持多选，取星期英文：
* 星期一 ：Monday
* 星期二 ：Tuesday
* 星期三：Wednesday
* 星期四：Thursday
* 星期五：Friday
* 星期六：Saturday
* 星期日：Sunday
        :type WeekDays: list of str
        :param _BackupCount: 保留备份个数，Frequency等于monthly或weekly时生效。
备份模式选择按月时，可填写1-28整数；
备份模式选择年时，可填写1-336整数。
        :type BackupCount: int
        """
        self._EnableBackupPolicy = None
        self._BeginDate = None
        self._MaxRetentionDays = None
        self._Frequency = None
        self._WeekDays = None
        self._BackupCount = None

    @property
    def EnableBackupPolicy(self):
        """备份策略是否启用。
        :rtype: bool
        """
        return self._EnableBackupPolicy

    @EnableBackupPolicy.setter
    def EnableBackupPolicy(self, EnableBackupPolicy):
        self._EnableBackupPolicy = EnableBackupPolicy

    @property
    def BeginDate(self):
        """超期保留开始日期，早于开始日期的超期备份不保留，格式：yyyy-mm-dd。
        :rtype: str
        """
        return self._BeginDate

    @BeginDate.setter
    def BeginDate(self, BeginDate):
        self._BeginDate = BeginDate

    @property
    def MaxRetentionDays(self):
        """超期备份保留时长，超出保留时间的超期备份将被删除，可填写1-3650整数。
        :rtype: int
        """
        return self._MaxRetentionDays

    @MaxRetentionDays.setter
    def MaxRetentionDays(self, MaxRetentionDays):
        self._MaxRetentionDays = MaxRetentionDays

    @property
    def Frequency(self):
        """备份模式，可选择按年月周模式保存
* 按年：annually
* 按月：monthly
* 按周：weekly
        :rtype: str
        """
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def WeekDays(self):
        """Frequency等于weekly时生效。
表示保留特定工作日备份。可选择周一到周日，支持多选，取星期英文：
* 星期一 ：Monday
* 星期二 ：Tuesday
* 星期三：Wednesday
* 星期四：Thursday
* 星期五：Friday
* 星期六：Saturday
* 星期日：Sunday
        :rtype: list of str
        """
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays

    @property
    def BackupCount(self):
        """保留备份个数，Frequency等于monthly或weekly时生效。
备份模式选择按月时，可填写1-28整数；
备份模式选择年时，可填写1-336整数。
        :rtype: int
        """
        return self._BackupCount

    @BackupCount.setter
    def BackupCount(self, BackupCount):
        self._BackupCount = BackupCount


    def _deserialize(self, params):
        self._EnableBackupPolicy = params.get("EnableBackupPolicy")
        self._BeginDate = params.get("BeginDate")
        self._MaxRetentionDays = params.get("MaxRetentionDays")
        self._Frequency = params.get("Frequency")
        self._WeekDays = params.get("WeekDays")
        self._BackupCount = params.get("BackupCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeInfo(AbstractModel):
    """描述DB节点信息

    """

    def __init__(self):
        r"""
        :param _NodeId: DB节点ID
        :type NodeId: str
        :param _Role: DB节点角色，取值为master或者slave
        :type Role: str
        :param _Zone: 节点所在的可用区
        :type Zone: str
        """
        self._NodeId = None
        self._Role = None
        self._Zone = None

    @property
    def NodeId(self):
        """DB节点ID
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Role(self):
        """DB节点角色，取值为master或者slave
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Zone(self):
        """节点所在的可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._Role = params.get("Role")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenDBExtranetAccessRequest(AbstractModel):
    """OpenDBExtranetAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 待开放外网访问的实例ID。形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param _Ipv6Flag: 是否IPv6，默认0
        :type Ipv6Flag: int
        """
        self._InstanceId = None
        self._Ipv6Flag = None

    @property
    def InstanceId(self):
        """待开放外网访问的实例ID。形如：dcdbt-ow728lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ipv6Flag(self):
        """是否IPv6，默认0
        :rtype: int
        """
        return self._Ipv6Flag

    @Ipv6Flag.setter
    def Ipv6Flag(self, Ipv6Flag):
        self._Ipv6Flag = Ipv6Flag


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Ipv6Flag = params.get("Ipv6Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenDBExtranetAccessResponse(AbstractModel):
    """OpenDBExtranetAccess返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步任务ID，可通过 DescribeFlow 查询任务状态。
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """异步任务ID，可通过 DescribeFlow 查询任务状态。
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ParamConstraint(AbstractModel):
    """参数约束

    """

    def __init__(self):
        r"""
        :param _Type: 约束类型,如枚举enum，区间section
        :type Type: str
        :param _Enum: 约束类型为enum时的可选值列表
        :type Enum: str
        :param _Range: 约束类型为section时的范围
注意：此字段可能返回 null，表示取不到有效值。
        :type Range: :class:`tencentcloud.dcdb.v20180411.models.ConstraintRange`
        :param _String: 约束类型为string时的可选值列表
        :type String: str
        """
        self._Type = None
        self._Enum = None
        self._Range = None
        self._String = None

    @property
    def Type(self):
        """约束类型,如枚举enum，区间section
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Enum(self):
        """约束类型为enum时的可选值列表
        :rtype: str
        """
        return self._Enum

    @Enum.setter
    def Enum(self, Enum):
        self._Enum = Enum

    @property
    def Range(self):
        """约束类型为section时的范围
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ConstraintRange`
        """
        return self._Range

    @Range.setter
    def Range(self, Range):
        self._Range = Range

    @property
    def String(self):
        """约束类型为string时的可选值列表
        :rtype: str
        """
        return self._String

    @String.setter
    def String(self, String):
        self._String = String


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Enum = params.get("Enum")
        if params.get("Range") is not None:
            self._Range = ConstraintRange()
            self._Range._deserialize(params.get("Range"))
        self._String = params.get("String")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamDesc(AbstractModel):
    """DB参数描述

    """

    def __init__(self):
        r"""
        :param _Param: 参数名字
        :type Param: str
        :param _Value: 当前参数值
        :type Value: str
        :param _SetValue: 设置过的值，参数生效后，该值和value一样。未设置过就不返回该字段。
        :type SetValue: str
        :param _Default: 系统默认值
        :type Default: str
        :param _Constraint: 参数限制
        :type Constraint: :class:`tencentcloud.dcdb.v20180411.models.ParamConstraint`
        :param _HaveSetValue: 是否有设置过值，false:没有设置过值，true:有设置过值。
        :type HaveSetValue: bool
        :param _NeedRestart: 是否需要重启生效，false:不需要重启，
true:需要重启
        :type NeedRestart: bool
        """
        self._Param = None
        self._Value = None
        self._SetValue = None
        self._Default = None
        self._Constraint = None
        self._HaveSetValue = None
        self._NeedRestart = None

    @property
    def Param(self):
        """参数名字
        :rtype: str
        """
        return self._Param

    @Param.setter
    def Param(self, Param):
        self._Param = Param

    @property
    def Value(self):
        """当前参数值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def SetValue(self):
        """设置过的值，参数生效后，该值和value一样。未设置过就不返回该字段。
        :rtype: str
        """
        return self._SetValue

    @SetValue.setter
    def SetValue(self, SetValue):
        self._SetValue = SetValue

    @property
    def Default(self):
        """系统默认值
        :rtype: str
        """
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Constraint(self):
        """参数限制
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ParamConstraint`
        """
        return self._Constraint

    @Constraint.setter
    def Constraint(self, Constraint):
        self._Constraint = Constraint

    @property
    def HaveSetValue(self):
        """是否有设置过值，false:没有设置过值，true:有设置过值。
        :rtype: bool
        """
        return self._HaveSetValue

    @HaveSetValue.setter
    def HaveSetValue(self, HaveSetValue):
        self._HaveSetValue = HaveSetValue

    @property
    def NeedRestart(self):
        """是否需要重启生效，false:不需要重启，
true:需要重启
        :rtype: bool
        """
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart


    def _deserialize(self, params):
        self._Param = params.get("Param")
        self._Value = params.get("Value")
        self._SetValue = params.get("SetValue")
        self._Default = params.get("Default")
        if params.get("Constraint") is not None:
            self._Constraint = ParamConstraint()
            self._Constraint._deserialize(params.get("Constraint"))
        self._HaveSetValue = params.get("HaveSetValue")
        self._NeedRestart = params.get("NeedRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamModifyResult(AbstractModel):
    """修改参数结果

    """

    def __init__(self):
        r"""
        :param _Param: 修改参数名字
        :type Param: str
        :param _Code: 参数修改结果。0表示修改成功；-1表示修改失败；-2表示该参数值非法
        :type Code: int
        """
        self._Param = None
        self._Code = None

    @property
    def Param(self):
        """修改参数名字
        :rtype: str
        """
        return self._Param

    @Param.setter
    def Param(self, Param):
        self._Param = Param

    @property
    def Code(self):
        """参数修改结果。0表示修改成功；-1表示修改失败；-2表示该参数值非法
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code


    def _deserialize(self, params):
        self._Param = params.get("Param")
        self._Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Project(AbstractModel):
    """项目信息描述

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _OwnerUin: 资源拥有者（主账号）uin
        :type OwnerUin: int
        :param _AppId: 应用Id
        :type AppId: int
        :param _Name: 项目名称
        :type Name: str
        :param _CreatorUin: 创建者uin
        :type CreatorUin: int
        :param _SrcPlat: 来源平台
        :type SrcPlat: str
        :param _SrcAppId: 来源AppId
        :type SrcAppId: int
        :param _Status: 项目状态,0正常，-1关闭。默认项目为3
        :type Status: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _IsDefault: 是否默认项目，1 是，0 不是
        :type IsDefault: int
        :param _Info: 描述信息
        :type Info: str
        """
        self._ProjectId = None
        self._OwnerUin = None
        self._AppId = None
        self._Name = None
        self._CreatorUin = None
        self._SrcPlat = None
        self._SrcAppId = None
        self._Status = None
        self._CreateTime = None
        self._IsDefault = None
        self._Info = None

    @property
    def ProjectId(self):
        """项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def OwnerUin(self):
        """资源拥有者（主账号）uin
        :rtype: int
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def AppId(self):
        """应用Id
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Name(self):
        """项目名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CreatorUin(self):
        """创建者uin
        :rtype: int
        """
        return self._CreatorUin

    @CreatorUin.setter
    def CreatorUin(self, CreatorUin):
        self._CreatorUin = CreatorUin

    @property
    def SrcPlat(self):
        """来源平台
        :rtype: str
        """
        return self._SrcPlat

    @SrcPlat.setter
    def SrcPlat(self, SrcPlat):
        self._SrcPlat = SrcPlat

    @property
    def SrcAppId(self):
        """来源AppId
        :rtype: int
        """
        return self._SrcAppId

    @SrcAppId.setter
    def SrcAppId(self, SrcAppId):
        self._SrcAppId = SrcAppId

    @property
    def Status(self):
        """项目状态,0正常，-1关闭。默认项目为3
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IsDefault(self):
        """是否默认项目，1 是，0 不是
        :rtype: int
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def Info(self):
        """描述信息
        :rtype: str
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._OwnerUin = params.get("OwnerUin")
        self._AppId = params.get("AppId")
        self._Name = params.get("Name")
        self._CreatorUin = params.get("CreatorUin")
        self._SrcPlat = params.get("SrcPlat")
        self._SrcAppId = params.get("SrcAppId")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._IsDefault = params.get("IsDefault")
        self._Info = params.get("Info")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionInfo(AbstractModel):
    """售卖可用区信息

    """

    def __init__(self):
        r"""
        :param _Region: 地域英文ID
        :type Region: str
        :param _RegionId: 地域数字ID
        :type RegionId: int
        :param _RegionName: 地域中文名
        :type RegionName: str
        :param _ZoneList: 可用区列表
        :type ZoneList: list of ZonesInfo
        :param _AvailableChoice: 可选择的主可用区和从可用区
        :type AvailableChoice: list of ShardZoneChooseInfo
        :param _HostType: 主机类型，如：物理机：Machine，容器：Container。
        :type HostType: str
        :param _CpuType: Cpu类型，如：英特尔：Intel/AMD，海光：Hygon
        :type CpuType: str
        """
        self._Region = None
        self._RegionId = None
        self._RegionName = None
        self._ZoneList = None
        self._AvailableChoice = None
        self._HostType = None
        self._CpuType = None

    @property
    def Region(self):
        """地域英文ID
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionId(self):
        """地域数字ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        """地域中文名
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneList(self):
        """可用区列表
        :rtype: list of ZonesInfo
        """
        return self._ZoneList

    @ZoneList.setter
    def ZoneList(self, ZoneList):
        self._ZoneList = ZoneList

    @property
    def AvailableChoice(self):
        """可选择的主可用区和从可用区
        :rtype: list of ShardZoneChooseInfo
        """
        return self._AvailableChoice

    @AvailableChoice.setter
    def AvailableChoice(self, AvailableChoice):
        self._AvailableChoice = AvailableChoice

    @property
    def HostType(self):
        """主机类型，如：物理机：Machine，容器：Container。
        :rtype: str
        """
        return self._HostType

    @HostType.setter
    def HostType(self, HostType):
        self._HostType = HostType

    @property
    def CpuType(self):
        """Cpu类型，如：英特尔：Intel/AMD，海光：Hygon
        :rtype: str
        """
        return self._CpuType

    @CpuType.setter
    def CpuType(self, CpuType):
        self._CpuType = CpuType


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        if params.get("ZoneList") is not None:
            self._ZoneList = []
            for item in params.get("ZoneList"):
                obj = ZonesInfo()
                obj._deserialize(item)
                self._ZoneList.append(obj)
        if params.get("AvailableChoice") is not None:
            self._AvailableChoice = []
            for item in params.get("AvailableChoice"):
                obj = ShardZoneChooseInfo()
                obj._deserialize(item)
                self._AvailableChoice.append(obj)
        self._HostType = params.get("HostType")
        self._CpuType = params.get("CpuType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDCDBInstanceRequest(AbstractModel):
    """RenewDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 待续费的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param _Period: 续费时长，单位：月。
        :type Period: int
        :param _AutoVoucher: 是否自动使用代金券进行支付，默认不使用。
        :type AutoVoucher: bool
        :param _VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。
        :type VoucherIds: list of str
        """
        self._InstanceId = None
        self._Period = None
        self._AutoVoucher = None
        self._VoucherIds = None

    @property
    def InstanceId(self):
        """待续费的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Period(self):
        """续费时长，单位：月。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def AutoVoucher(self):
        """是否自动使用代金券进行支付，默认不使用。
        :rtype: bool
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        """代金券ID列表，目前仅支持指定一张代金券。
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Period = params.get("Period")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDCDBInstanceResponse(AbstractModel):
    """RenewDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealName: 长订单号。可以据此调用 DescribeOrders
 查询订单详细信息，或在支付失败时调用用户账号相关接口进行支付。
        :type DealName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        """长订单号。可以据此调用 DescribeOrders
 查询订单详细信息，或在支付失败时调用用户账号相关接口进行支付。
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class ReservedNetResource(AbstractModel):
    """保留的网络资源信息

    """

    def __init__(self):
        r"""
        :param _VpcId: 私有网络
        :type VpcId: str
        :param _SubnetId: 子网
        :type SubnetId: str
        :param _Vip: VpcId,SubnetId下保留的内网ip
        :type Vip: str
        :param _Vports: Vip下的端口
        :type Vports: list of int
        :param _RecycleTime: Vip的回收时间	
        :type RecycleTime: str
        """
        self._VpcId = None
        self._SubnetId = None
        self._Vip = None
        self._Vports = None
        self._RecycleTime = None

    @property
    def VpcId(self):
        """私有网络
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Vip(self):
        """VpcId,SubnetId下保留的内网ip
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vports(self):
        """Vip下的端口
        :rtype: list of int
        """
        return self._Vports

    @Vports.setter
    def Vports(self, Vports):
        self._Vports = Vports

    @property
    def RecycleTime(self):
        """Vip的回收时间	
        :rtype: str
        """
        return self._RecycleTime

    @RecycleTime.setter
    def RecycleTime(self, RecycleTime):
        self._RecycleTime = RecycleTime


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Vip = params.get("Vip")
        self._Vports = params.get("Vports")
        self._RecycleTime = params.get("RecycleTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordRequest(AbstractModel):
    """ResetAccountPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param _UserName: 登录用户名。
        :type UserName: str
        :param _Host: 用户允许的访问 host，用户名+host唯一确定一个账号。
        :type Host: str
        :param _Password: 新密码，由字母、数字或常见符号组成，不能包含分号、单引号和双引号，长度为6~32位。
        :type Password: str
        :param _EncryptedPassword: 使用GetPublicKey返回的RSA2048公钥加密后的密码，加密算法是PKCS1v15
        :type EncryptedPassword: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Host = None
        self._Password = None
        self._EncryptedPassword = None

    @property
    def InstanceId(self):
        """实例 ID，形如：dcdbt-ow728lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        """登录用户名。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        """用户允许的访问 host，用户名+host唯一确定一个账号。
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Password(self):
        """新密码，由字母、数字或常见符号组成，不能包含分号、单引号和双引号，长度为6~32位。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def EncryptedPassword(self):
        """使用GetPublicKey返回的RSA2048公钥加密后的密码，加密算法是PKCS1v15
        :rtype: str
        """
        return self._EncryptedPassword

    @EncryptedPassword.setter
    def EncryptedPassword(self, EncryptedPassword):
        self._EncryptedPassword = EncryptedPassword


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._Password = params.get("Password")
        self._EncryptedPassword = params.get("EncryptedPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordResponse(AbstractModel):
    """ResetAccountPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResourceTag(AbstractModel):
    """标签对象，包含tagKey & tagValue

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键key
        :type TagKey: str
        :param _TagValue: 标签值value
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """标签键key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签值value
        :rtype: str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroup(AbstractModel):
    """安全组详情

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _CreateTime: 创建时间，时间格式：yyyy-mm-dd hh:mm:ss
        :type CreateTime: str
        :param _SecurityGroupId: 安全组ID
        :type SecurityGroupId: str
        :param _SecurityGroupName: 安全组名称
        :type SecurityGroupName: str
        :param _SecurityGroupRemark: 安全组备注
        :type SecurityGroupRemark: str
        :param _Inbound: 入站规则
        :type Inbound: list of SecurityGroupBound
        :param _Outbound: 出站规则
        :type Outbound: list of SecurityGroupBound
        """
        self._ProjectId = None
        self._CreateTime = None
        self._SecurityGroupId = None
        self._SecurityGroupName = None
        self._SecurityGroupRemark = None
        self._Inbound = None
        self._Outbound = None

    @property
    def ProjectId(self):
        """项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreateTime(self):
        """创建时间，时间格式：yyyy-mm-dd hh:mm:ss
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SecurityGroupId(self):
        """安全组ID
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        """安全组名称
        :rtype: str
        """
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupRemark(self):
        """安全组备注
        :rtype: str
        """
        return self._SecurityGroupRemark

    @SecurityGroupRemark.setter
    def SecurityGroupRemark(self, SecurityGroupRemark):
        self._SecurityGroupRemark = SecurityGroupRemark

    @property
    def Inbound(self):
        """入站规则
        :rtype: list of SecurityGroupBound
        """
        return self._Inbound

    @Inbound.setter
    def Inbound(self, Inbound):
        self._Inbound = Inbound

    @property
    def Outbound(self):
        """出站规则
        :rtype: list of SecurityGroupBound
        """
        return self._Outbound

    @Outbound.setter
    def Outbound(self, Outbound):
        self._Outbound = Outbound


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CreateTime = params.get("CreateTime")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._SecurityGroupName = params.get("SecurityGroupName")
        self._SecurityGroupRemark = params.get("SecurityGroupRemark")
        if params.get("Inbound") is not None:
            self._Inbound = []
            for item in params.get("Inbound"):
                obj = SecurityGroupBound()
                obj._deserialize(item)
                self._Inbound.append(obj)
        if params.get("Outbound") is not None:
            self._Outbound = []
            for item in params.get("Outbound"):
                obj = SecurityGroupBound()
                obj._deserialize(item)
                self._Outbound.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupBound(AbstractModel):
    """安全出入口规则

    """

    def __init__(self):
        r"""
        :param _CidrIp: 来源 IP 或 IP 段，例如192.168.0.0/16
        :type CidrIp: str
        :param _Action: 策略，ACCEPT 或者 DROP
        :type Action: str
        :param _PortRange: 端口
        :type PortRange: str
        :param _IpProtocol: 网络协议，支持 UDP、TCP 等
        :type IpProtocol: str
        """
        self._CidrIp = None
        self._Action = None
        self._PortRange = None
        self._IpProtocol = None

    @property
    def CidrIp(self):
        """来源 IP 或 IP 段，例如192.168.0.0/16
        :rtype: str
        """
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def Action(self):
        """策略，ACCEPT 或者 DROP
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def PortRange(self):
        """端口
        :rtype: str
        """
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def IpProtocol(self):
        """网络协议，支持 UDP、TCP 等
        :rtype: str
        """
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol


    def _deserialize(self, params):
        self._CidrIp = params.get("CidrIp")
        self._Action = params.get("Action")
        self._PortRange = params.get("PortRange")
        self._IpProtocol = params.get("IpProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShardBriefInfo(AbstractModel):
    """DCDB分片信息

    """

    def __init__(self):
        r"""
        :param _ShardSerialId: 分片SerialId
        :type ShardSerialId: str
        :param _ShardInstanceId: 分片ID，形如shard-7vg1o339
        :type ShardInstanceId: str
        :param _Status: 分片运行状态
        :type Status: int
        :param _StatusDesc: 分片运行状态描述
        :type StatusDesc: str
        :param _CreateTime: 分片创建时间
        :type CreateTime: str
        :param _Memory: 分片内存大小，单位GB
        :type Memory: int
        :param _Storage: 分片磁盘大小，单位GB
        :type Storage: int
        :param _LogDisk: 分片日志磁盘空间大小，单位GB
        :type LogDisk: int
        :param _NodeCount: 分片节点个数
        :type NodeCount: int
        :param _StorageUsage: 分片磁盘空间使用率
        :type StorageUsage: float
        :param _ProxyVersion: 分片Proxy版本信息
        :type ProxyVersion: str
        :param _ShardMasterZone: 分片主DB可用区
        :type ShardMasterZone: str
        :param _ShardSlaveZones: 分片从DB可用区
        :type ShardSlaveZones: list of str
        :param _Cpu: 分片Cpu核数
        :type Cpu: int
        :param _NodesInfo: DB节点信息
        :type NodesInfo: list of NodeInfo
        """
        self._ShardSerialId = None
        self._ShardInstanceId = None
        self._Status = None
        self._StatusDesc = None
        self._CreateTime = None
        self._Memory = None
        self._Storage = None
        self._LogDisk = None
        self._NodeCount = None
        self._StorageUsage = None
        self._ProxyVersion = None
        self._ShardMasterZone = None
        self._ShardSlaveZones = None
        self._Cpu = None
        self._NodesInfo = None

    @property
    def ShardSerialId(self):
        """分片SerialId
        :rtype: str
        """
        return self._ShardSerialId

    @ShardSerialId.setter
    def ShardSerialId(self, ShardSerialId):
        self._ShardSerialId = ShardSerialId

    @property
    def ShardInstanceId(self):
        """分片ID，形如shard-7vg1o339
        :rtype: str
        """
        return self._ShardInstanceId

    @ShardInstanceId.setter
    def ShardInstanceId(self, ShardInstanceId):
        self._ShardInstanceId = ShardInstanceId

    @property
    def Status(self):
        """分片运行状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        """分片运行状态描述
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def CreateTime(self):
        """分片创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Memory(self):
        """分片内存大小，单位GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        """分片磁盘大小，单位GB
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def LogDisk(self):
        """分片日志磁盘空间大小，单位GB
        :rtype: int
        """
        return self._LogDisk

    @LogDisk.setter
    def LogDisk(self, LogDisk):
        self._LogDisk = LogDisk

    @property
    def NodeCount(self):
        """分片节点个数
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def StorageUsage(self):
        """分片磁盘空间使用率
        :rtype: float
        """
        return self._StorageUsage

    @StorageUsage.setter
    def StorageUsage(self, StorageUsage):
        self._StorageUsage = StorageUsage

    @property
    def ProxyVersion(self):
        """分片Proxy版本信息
        :rtype: str
        """
        return self._ProxyVersion

    @ProxyVersion.setter
    def ProxyVersion(self, ProxyVersion):
        self._ProxyVersion = ProxyVersion

    @property
    def ShardMasterZone(self):
        """分片主DB可用区
        :rtype: str
        """
        return self._ShardMasterZone

    @ShardMasterZone.setter
    def ShardMasterZone(self, ShardMasterZone):
        self._ShardMasterZone = ShardMasterZone

    @property
    def ShardSlaveZones(self):
        """分片从DB可用区
        :rtype: list of str
        """
        return self._ShardSlaveZones

    @ShardSlaveZones.setter
    def ShardSlaveZones(self, ShardSlaveZones):
        self._ShardSlaveZones = ShardSlaveZones

    @property
    def Cpu(self):
        """分片Cpu核数
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def NodesInfo(self):
        """DB节点信息
        :rtype: list of NodeInfo
        """
        return self._NodesInfo

    @NodesInfo.setter
    def NodesInfo(self, NodesInfo):
        self._NodesInfo = NodesInfo


    def _deserialize(self, params):
        self._ShardSerialId = params.get("ShardSerialId")
        self._ShardInstanceId = params.get("ShardInstanceId")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._CreateTime = params.get("CreateTime")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._LogDisk = params.get("LogDisk")
        self._NodeCount = params.get("NodeCount")
        self._StorageUsage = params.get("StorageUsage")
        self._ProxyVersion = params.get("ProxyVersion")
        self._ShardMasterZone = params.get("ShardMasterZone")
        self._ShardSlaveZones = params.get("ShardSlaveZones")
        self._Cpu = params.get("Cpu")
        if params.get("NodesInfo") is not None:
            self._NodesInfo = []
            for item in params.get("NodesInfo"):
                obj = NodeInfo()
                obj._deserialize(item)
                self._NodesInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShardInfo(AbstractModel):
    """分片信息

    """

    def __init__(self):
        r"""
        :param _ShardInstanceId: 分片ID
        :type ShardInstanceId: str
        :param _ShardSerialId: 分片Set ID
        :type ShardSerialId: str
        :param _Status: 状态：0 创建中，1 流程处理中， 2 运行中，3 分片未初始化，-2 分片已删除
        :type Status: int
        :param _Createtime: 创建时间
        :type Createtime: str
        :param _Memory: 内存大小，单位 GB
        :type Memory: int
        :param _Storage: 存储大小，单位 GB
        :type Storage: int
        :param _ShardId: 分片数字ID
        :type ShardId: int
        :param _NodeCount: 节点数，2 为一主一从， 3 为一主二从
        :type NodeCount: int
        :param _Pid: 产品类型 Id（过时字段，请勿依赖该值）
        :type Pid: int
        :param _Cpu: Cpu核数
        :type Cpu: int
        """
        self._ShardInstanceId = None
        self._ShardSerialId = None
        self._Status = None
        self._Createtime = None
        self._Memory = None
        self._Storage = None
        self._ShardId = None
        self._NodeCount = None
        self._Pid = None
        self._Cpu = None

    @property
    def ShardInstanceId(self):
        """分片ID
        :rtype: str
        """
        return self._ShardInstanceId

    @ShardInstanceId.setter
    def ShardInstanceId(self, ShardInstanceId):
        self._ShardInstanceId = ShardInstanceId

    @property
    def ShardSerialId(self):
        """分片Set ID
        :rtype: str
        """
        return self._ShardSerialId

    @ShardSerialId.setter
    def ShardSerialId(self, ShardSerialId):
        self._ShardSerialId = ShardSerialId

    @property
    def Status(self):
        """状态：0 创建中，1 流程处理中， 2 运行中，3 分片未初始化，-2 分片已删除
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Createtime(self):
        """创建时间
        :rtype: str
        """
        return self._Createtime

    @Createtime.setter
    def Createtime(self, Createtime):
        self._Createtime = Createtime

    @property
    def Memory(self):
        """内存大小，单位 GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        """存储大小，单位 GB
        :rtype: int
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def ShardId(self):
        """分片数字ID
        :rtype: int
        """
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def NodeCount(self):
        """节点数，2 为一主一从， 3 为一主二从
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def Pid(self):
        """产品类型 Id（过时字段，请勿依赖该值）
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def Cpu(self):
        """Cpu核数
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu


    def _deserialize(self, params):
        self._ShardInstanceId = params.get("ShardInstanceId")
        self._ShardSerialId = params.get("ShardSerialId")
        self._Status = params.get("Status")
        self._Createtime = params.get("Createtime")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._ShardId = params.get("ShardId")
        self._NodeCount = params.get("NodeCount")
        self._Pid = params.get("Pid")
        self._Cpu = params.get("Cpu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShardZoneChooseInfo(AbstractModel):
    """分片节点可用区选择

    """

    def __init__(self):
        r"""
        :param _MasterZone: 主可用区
        :type MasterZone: :class:`tencentcloud.dcdb.v20180411.models.ZonesInfo`
        :param _SlaveZones: 可选的从可用区
        :type SlaveZones: list of ZonesInfo
        """
        self._MasterZone = None
        self._SlaveZones = None

    @property
    def MasterZone(self):
        """主可用区
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ZonesInfo`
        """
        return self._MasterZone

    @MasterZone.setter
    def MasterZone(self, MasterZone):
        self._MasterZone = MasterZone

    @property
    def SlaveZones(self):
        """可选的从可用区
        :rtype: list of ZonesInfo
        """
        return self._SlaveZones

    @SlaveZones.setter
    def SlaveZones(self, SlaveZones):
        self._SlaveZones = SlaveZones


    def _deserialize(self, params):
        if params.get("MasterZone") is not None:
            self._MasterZone = ZonesInfo()
            self._MasterZone._deserialize(params.get("MasterZone"))
        if params.get("SlaveZones") is not None:
            self._SlaveZones = []
            for item in params.get("SlaveZones"):
                obj = ZonesInfo()
                obj._deserialize(item)
                self._SlaveZones.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogData(AbstractModel):
    """慢查询条目信息

    """

    def __init__(self):
        r"""
        :param _CheckSum: 语句校验和，用于查询详情
        :type CheckSum: str
        :param _Db: 数据库名称
        :type Db: str
        :param _FingerPrint: 抽象的SQL语句
        :type FingerPrint: str
        :param _LockTimeAvg: 平均的锁时间
        :type LockTimeAvg: str
        :param _LockTimeMax: 最大锁时间
        :type LockTimeMax: str
        :param _LockTimeMin: 最小锁时间
        :type LockTimeMin: str
        :param _LockTimeSum: 锁时间总和
        :type LockTimeSum: str
        :param _QueryCount: 查询次数
        :type QueryCount: str
        :param _QueryTimeAvg: 平均查询时间
        :type QueryTimeAvg: str
        :param _QueryTimeMax: 最大查询时间
        :type QueryTimeMax: str
        :param _QueryTimeMin: 最小查询时间
        :type QueryTimeMin: str
        :param _QueryTimeSum: 查询时间总和
        :type QueryTimeSum: str
        :param _RowsExaminedSum: 扫描行数
        :type RowsExaminedSum: str
        :param _RowsSentSum: 发送行数
        :type RowsSentSum: str
        :param _TsMax: 最后执行时间
        :type TsMax: str
        :param _TsMin: 首次执行时间
        :type TsMin: str
        :param _User: 账号
        :type User: str
        :param _ExampleSql: 样例Sql
        :type ExampleSql: str
        :param _Host: 账户的域名
        :type Host: str
        """
        self._CheckSum = None
        self._Db = None
        self._FingerPrint = None
        self._LockTimeAvg = None
        self._LockTimeMax = None
        self._LockTimeMin = None
        self._LockTimeSum = None
        self._QueryCount = None
        self._QueryTimeAvg = None
        self._QueryTimeMax = None
        self._QueryTimeMin = None
        self._QueryTimeSum = None
        self._RowsExaminedSum = None
        self._RowsSentSum = None
        self._TsMax = None
        self._TsMin = None
        self._User = None
        self._ExampleSql = None
        self._Host = None

    @property
    def CheckSum(self):
        """语句校验和，用于查询详情
        :rtype: str
        """
        return self._CheckSum

    @CheckSum.setter
    def CheckSum(self, CheckSum):
        self._CheckSum = CheckSum

    @property
    def Db(self):
        """数据库名称
        :rtype: str
        """
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def FingerPrint(self):
        """抽象的SQL语句
        :rtype: str
        """
        return self._FingerPrint

    @FingerPrint.setter
    def FingerPrint(self, FingerPrint):
        self._FingerPrint = FingerPrint

    @property
    def LockTimeAvg(self):
        """平均的锁时间
        :rtype: str
        """
        return self._LockTimeAvg

    @LockTimeAvg.setter
    def LockTimeAvg(self, LockTimeAvg):
        self._LockTimeAvg = LockTimeAvg

    @property
    def LockTimeMax(self):
        """最大锁时间
        :rtype: str
        """
        return self._LockTimeMax

    @LockTimeMax.setter
    def LockTimeMax(self, LockTimeMax):
        self._LockTimeMax = LockTimeMax

    @property
    def LockTimeMin(self):
        """最小锁时间
        :rtype: str
        """
        return self._LockTimeMin

    @LockTimeMin.setter
    def LockTimeMin(self, LockTimeMin):
        self._LockTimeMin = LockTimeMin

    @property
    def LockTimeSum(self):
        """锁时间总和
        :rtype: str
        """
        return self._LockTimeSum

    @LockTimeSum.setter
    def LockTimeSum(self, LockTimeSum):
        self._LockTimeSum = LockTimeSum

    @property
    def QueryCount(self):
        """查询次数
        :rtype: str
        """
        return self._QueryCount

    @QueryCount.setter
    def QueryCount(self, QueryCount):
        self._QueryCount = QueryCount

    @property
    def QueryTimeAvg(self):
        """平均查询时间
        :rtype: str
        """
        return self._QueryTimeAvg

    @QueryTimeAvg.setter
    def QueryTimeAvg(self, QueryTimeAvg):
        self._QueryTimeAvg = QueryTimeAvg

    @property
    def QueryTimeMax(self):
        """最大查询时间
        :rtype: str
        """
        return self._QueryTimeMax

    @QueryTimeMax.setter
    def QueryTimeMax(self, QueryTimeMax):
        self._QueryTimeMax = QueryTimeMax

    @property
    def QueryTimeMin(self):
        """最小查询时间
        :rtype: str
        """
        return self._QueryTimeMin

    @QueryTimeMin.setter
    def QueryTimeMin(self, QueryTimeMin):
        self._QueryTimeMin = QueryTimeMin

    @property
    def QueryTimeSum(self):
        """查询时间总和
        :rtype: str
        """
        return self._QueryTimeSum

    @QueryTimeSum.setter
    def QueryTimeSum(self, QueryTimeSum):
        self._QueryTimeSum = QueryTimeSum

    @property
    def RowsExaminedSum(self):
        """扫描行数
        :rtype: str
        """
        return self._RowsExaminedSum

    @RowsExaminedSum.setter
    def RowsExaminedSum(self, RowsExaminedSum):
        self._RowsExaminedSum = RowsExaminedSum

    @property
    def RowsSentSum(self):
        """发送行数
        :rtype: str
        """
        return self._RowsSentSum

    @RowsSentSum.setter
    def RowsSentSum(self, RowsSentSum):
        self._RowsSentSum = RowsSentSum

    @property
    def TsMax(self):
        """最后执行时间
        :rtype: str
        """
        return self._TsMax

    @TsMax.setter
    def TsMax(self, TsMax):
        self._TsMax = TsMax

    @property
    def TsMin(self):
        """首次执行时间
        :rtype: str
        """
        return self._TsMin

    @TsMin.setter
    def TsMin(self, TsMin):
        self._TsMin = TsMin

    @property
    def User(self):
        """账号
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def ExampleSql(self):
        """样例Sql
        :rtype: str
        """
        return self._ExampleSql

    @ExampleSql.setter
    def ExampleSql(self, ExampleSql):
        self._ExampleSql = ExampleSql

    @property
    def Host(self):
        """账户的域名
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._CheckSum = params.get("CheckSum")
        self._Db = params.get("Db")
        self._FingerPrint = params.get("FingerPrint")
        self._LockTimeAvg = params.get("LockTimeAvg")
        self._LockTimeMax = params.get("LockTimeMax")
        self._LockTimeMin = params.get("LockTimeMin")
        self._LockTimeSum = params.get("LockTimeSum")
        self._QueryCount = params.get("QueryCount")
        self._QueryTimeAvg = params.get("QueryTimeAvg")
        self._QueryTimeMax = params.get("QueryTimeMax")
        self._QueryTimeMin = params.get("QueryTimeMin")
        self._QueryTimeSum = params.get("QueryTimeSum")
        self._RowsExaminedSum = params.get("RowsExaminedSum")
        self._RowsSentSum = params.get("RowsSentSum")
        self._TsMax = params.get("TsMax")
        self._TsMin = params.get("TsMin")
        self._User = params.get("User")
        self._ExampleSql = params.get("ExampleSql")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecConfig(AbstractModel):
    """按机型分类的规格配置

    """

    def __init__(self):
        r"""
        :param _Machine: 规格机型
        :type Machine: str
        :param _SpecConfigInfos: 规格列表
        :type SpecConfigInfos: list of SpecConfigInfo
        """
        self._Machine = None
        self._SpecConfigInfos = None

    @property
    def Machine(self):
        """规格机型
        :rtype: str
        """
        return self._Machine

    @Machine.setter
    def Machine(self, Machine):
        self._Machine = Machine

    @property
    def SpecConfigInfos(self):
        """规格列表
        :rtype: list of SpecConfigInfo
        """
        return self._SpecConfigInfos

    @SpecConfigInfos.setter
    def SpecConfigInfos(self, SpecConfigInfos):
        self._SpecConfigInfos = SpecConfigInfos


    def _deserialize(self, params):
        self._Machine = params.get("Machine")
        if params.get("SpecConfigInfos") is not None:
            self._SpecConfigInfos = []
            for item in params.get("SpecConfigInfos"):
                obj = SpecConfigInfo()
                obj._deserialize(item)
                self._SpecConfigInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecConfigInfo(AbstractModel):
    """实例可售卖规格详细信息，创建实例和扩容实例时 NodeCount、Memory 确定售卖规格，硬盘大小可用区间为[MinStorage,MaxStorage]

    """

    def __init__(self):
        r"""
        :param _NodeCount: 节点个数，2 表示一主一从，3 表示一主二从
        :type NodeCount: int
        :param _Memory: 内存大小，单位 GB
        :type Memory: int
        :param _MinStorage: 数据盘规格最小值，单位 GB
        :type MinStorage: int
        :param _MaxStorage: 数据盘规格最大值，单位 GB
        :type MaxStorage: int
        :param _SuitInfo: 推荐的使用场景
        :type SuitInfo: str
        :param _Pid: 产品类型 Id
        :type Pid: int
        :param _Qps: 最大 Qps 值
        :type Qps: int
        :param _Cpu: CPU核数
        :type Cpu: int
        """
        self._NodeCount = None
        self._Memory = None
        self._MinStorage = None
        self._MaxStorage = None
        self._SuitInfo = None
        self._Pid = None
        self._Qps = None
        self._Cpu = None

    @property
    def NodeCount(self):
        """节点个数，2 表示一主一从，3 表示一主二从
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def Memory(self):
        """内存大小，单位 GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def MinStorage(self):
        """数据盘规格最小值，单位 GB
        :rtype: int
        """
        return self._MinStorage

    @MinStorage.setter
    def MinStorage(self, MinStorage):
        self._MinStorage = MinStorage

    @property
    def MaxStorage(self):
        """数据盘规格最大值，单位 GB
        :rtype: int
        """
        return self._MaxStorage

    @MaxStorage.setter
    def MaxStorage(self, MaxStorage):
        self._MaxStorage = MaxStorage

    @property
    def SuitInfo(self):
        """推荐的使用场景
        :rtype: str
        """
        return self._SuitInfo

    @SuitInfo.setter
    def SuitInfo(self, SuitInfo):
        self._SuitInfo = SuitInfo

    @property
    def Pid(self):
        """产品类型 Id
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def Qps(self):
        """最大 Qps 值
        :rtype: int
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def Cpu(self):
        """CPU核数
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu


    def _deserialize(self, params):
        self._NodeCount = params.get("NodeCount")
        self._Memory = params.get("Memory")
        self._MinStorage = params.get("MinStorage")
        self._MaxStorage = params.get("MaxStorage")
        self._SuitInfo = params.get("SuitInfo")
        self._Pid = params.get("Pid")
        self._Qps = params.get("Qps")
        self._Cpu = params.get("Cpu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SplitShardConfig(AbstractModel):
    """升级实例 -- 切分分片类型

    """

    def __init__(self):
        r"""
        :param _ShardInstanceIds: 分片ID数组
        :type ShardInstanceIds: list of str
        :param _SplitRate: 数据切分比例，固定50%
        :type SplitRate: int
        :param _ShardMemory: 分片内存大小，单位 GB
        :type ShardMemory: int
        :param _ShardStorage: 分片存储大小，单位 GB
        :type ShardStorage: int
        """
        self._ShardInstanceIds = None
        self._SplitRate = None
        self._ShardMemory = None
        self._ShardStorage = None

    @property
    def ShardInstanceIds(self):
        """分片ID数组
        :rtype: list of str
        """
        return self._ShardInstanceIds

    @ShardInstanceIds.setter
    def ShardInstanceIds(self, ShardInstanceIds):
        self._ShardInstanceIds = ShardInstanceIds

    @property
    def SplitRate(self):
        """数据切分比例，固定50%
        :rtype: int
        """
        return self._SplitRate

    @SplitRate.setter
    def SplitRate(self, SplitRate):
        self._SplitRate = SplitRate

    @property
    def ShardMemory(self):
        """分片内存大小，单位 GB
        :rtype: int
        """
        return self._ShardMemory

    @ShardMemory.setter
    def ShardMemory(self, ShardMemory):
        self._ShardMemory = ShardMemory

    @property
    def ShardStorage(self):
        """分片存储大小，单位 GB
        :rtype: int
        """
        return self._ShardStorage

    @ShardStorage.setter
    def ShardStorage(self, ShardStorage):
        self._ShardStorage = ShardStorage


    def _deserialize(self, params):
        self._ShardInstanceIds = params.get("ShardInstanceIds")
        self._SplitRate = params.get("SplitRate")
        self._ShardMemory = params.get("ShardMemory")
        self._ShardStorage = params.get("ShardStorage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDBInstanceHARequest(AbstractModel):
    """SwitchDBInstanceHA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id，形如 tdsql-ow728lmc。
        :type InstanceId: str
        :param _Zone: 指定可用区标识符，具体含义由zoneMode参数决定。 

- 当zoneMode为target时表示目标可用区 

- 当zoneMode为avoid时表示需避开的故障可用区
        :type Zone: str
        :param _ShardInstanceIds: 指定分片实例id进行切换
        :type ShardInstanceIds: list of str
        :param _ZoneMode: 可用区模式选择器，定义zone参数的语义类型。  - 默认值：target  - 可选值：target, avoid
        :type ZoneMode: str
        """
        self._InstanceId = None
        self._Zone = None
        self._ShardInstanceIds = None
        self._ZoneMode = None

    @property
    def InstanceId(self):
        """实例Id，形如 tdsql-ow728lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Zone(self):
        """指定可用区标识符，具体含义由zoneMode参数决定。 

- 当zoneMode为target时表示目标可用区 

- 当zoneMode为avoid时表示需避开的故障可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ShardInstanceIds(self):
        """指定分片实例id进行切换
        :rtype: list of str
        """
        return self._ShardInstanceIds

    @ShardInstanceIds.setter
    def ShardInstanceIds(self, ShardInstanceIds):
        self._ShardInstanceIds = ShardInstanceIds

    @property
    def ZoneMode(self):
        """可用区模式选择器，定义zone参数的语义类型。  - 默认值：target  - 可选值：target, avoid
        :rtype: str
        """
        return self._ZoneMode

    @ZoneMode.setter
    def ZoneMode(self, ZoneMode):
        self._ZoneMode = ZoneMode


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Zone = params.get("Zone")
        self._ShardInstanceIds = params.get("ShardInstanceIds")
        self._ZoneMode = params.get("ZoneMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDBInstanceHAResponse(AbstractModel):
    """SwitchDBInstanceHA返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步流程Id
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """异步流程Id
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class TableColumn(AbstractModel):
    """数据库列信息

    """

    def __init__(self):
        r"""
        :param _Col: 列名称
        :type Col: str
        :param _Type: 列类型
        :type Type: str
        """
        self._Col = None
        self._Type = None

    @property
    def Col(self):
        """列名称
        :rtype: str
        """
        return self._Col

    @Col.setter
    def Col(self, Col):
        self._Col = Col

    @property
    def Type(self):
        """列类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Col = params.get("Col")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TablePrivilege(AbstractModel):
    """数据库表权限

    """

    def __init__(self):
        r"""
        :param _Database: 数据库名
        :type Database: str
        :param _Table: 数据库表名
        :type Table: str
        :param _Privileges: 权限信息
        :type Privileges: list of str
        """
        self._Database = None
        self._Table = None
        self._Privileges = None

    @property
    def Database(self):
        """数据库名
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        """数据库表名
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Privileges(self):
        """权限信息
        :rtype: list of str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签值
        :rtype: str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateDedicatedDBInstanceRequest(AbstractModel):
    """TerminateDedicatedDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 Id，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例 Id，形如：dcdbt-ow728lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateDedicatedDBInstanceResponse(AbstractModel):
    """TerminateDedicatedDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步流程Id
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """异步流程Id
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class TmpInstance(AbstractModel):
    """临时实例

    """

    def __init__(self):
        r"""
        :param _AppId: 应用ID
        :type AppId: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _InstanceRemark: 实例备注
        :type InstanceRemark: str
        :param _TempType: 0:非临时实例 ,1:无效临时实例, 2:回档成功的有效临时实例
        :type TempType: int
        :param _Status: 实例状态,0:待初始化,1:流程处理中,2:有效状态,-1:已隔离，-2：已下线
        :type Status: int
        :param _InstanceId: 实例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param _Vip: 实例虚IP
        :type Vip: str
        :param _Vport: 实例虚端口
        :type Vport: int
        :param _PeriodEndTime: 有效期结束时间
        :type PeriodEndTime: str
        :param _SrcInstanceId: 源实例 ID，形如：tdsql-ow728lmc。
        :type SrcInstanceId: str
        :param _StatusDesc: 实例状态描述
        :type StatusDesc: str
        :param _Region: 实例所在地域
        :type Region: str
        :param _Zone: 实例所在可用区
        :type Zone: str
        :param _Vipv6: 实例虚IPv6
        :type Vipv6: str
        :param _Ipv6Flag: 实例IPv6标志
        :type Ipv6Flag: int
        """
        self._AppId = None
        self._CreateTime = None
        self._InstanceRemark = None
        self._TempType = None
        self._Status = None
        self._InstanceId = None
        self._Vip = None
        self._Vport = None
        self._PeriodEndTime = None
        self._SrcInstanceId = None
        self._StatusDesc = None
        self._Region = None
        self._Zone = None
        self._Vipv6 = None
        self._Ipv6Flag = None

    @property
    def AppId(self):
        """应用ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def InstanceRemark(self):
        """实例备注
        :rtype: str
        """
        return self._InstanceRemark

    @InstanceRemark.setter
    def InstanceRemark(self, InstanceRemark):
        self._InstanceRemark = InstanceRemark

    @property
    def TempType(self):
        """0:非临时实例 ,1:无效临时实例, 2:回档成功的有效临时实例
        :rtype: int
        """
        return self._TempType

    @TempType.setter
    def TempType(self, TempType):
        self._TempType = TempType

    @property
    def Status(self):
        """实例状态,0:待初始化,1:流程处理中,2:有效状态,-1:已隔离，-2：已下线
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceId(self):
        """实例 ID，形如：tdsql-ow728lmc。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Vip(self):
        """实例虚IP
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """实例虚端口
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def PeriodEndTime(self):
        """有效期结束时间
        :rtype: str
        """
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def SrcInstanceId(self):
        """源实例 ID，形如：tdsql-ow728lmc。
        :rtype: str
        """
        return self._SrcInstanceId

    @SrcInstanceId.setter
    def SrcInstanceId(self, SrcInstanceId):
        self._SrcInstanceId = SrcInstanceId

    @property
    def StatusDesc(self):
        """实例状态描述
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def Region(self):
        """实例所在地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """实例所在可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Vipv6(self):
        """实例虚IPv6
        :rtype: str
        """
        return self._Vipv6

    @Vipv6.setter
    def Vipv6(self, Vipv6):
        self._Vipv6 = Vipv6

    @property
    def Ipv6Flag(self):
        """实例IPv6标志
        :rtype: int
        """
        return self._Ipv6Flag

    @Ipv6Flag.setter
    def Ipv6Flag(self, Ipv6Flag):
        self._Ipv6Flag = Ipv6Flag


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._CreateTime = params.get("CreateTime")
        self._InstanceRemark = params.get("InstanceRemark")
        self._TempType = params.get("TempType")
        self._Status = params.get("Status")
        self._InstanceId = params.get("InstanceId")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._SrcInstanceId = params.get("SrcInstanceId")
        self._StatusDesc = params.get("StatusDesc")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._Vipv6 = params.get("Vipv6")
        self._Ipv6Flag = params.get("Ipv6Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDCDBInstanceRequest(AbstractModel):
    """UpgradeDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 待升级的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param _UpgradeType: 升级类型，取值范围: 
<li> ADD: 新增分片 </li> 
 <li> EXPAND: 升级实例中的已有分片 </li> 
 <li> SPLIT: 将已有分片中的数据切分到新增分片上</li>
        :type UpgradeType: str
        :param _AddShardConfig: 新增分片配置，当UpgradeType为ADD时生效。
        :type AddShardConfig: :class:`tencentcloud.dcdb.v20180411.models.AddShardConfig`
        :param _ExpandShardConfig: 扩容分片配置，当UpgradeType为EXPAND时生效。
        :type ExpandShardConfig: :class:`tencentcloud.dcdb.v20180411.models.ExpandShardConfig`
        :param _SplitShardConfig: 切分分片配置，当UpgradeType为SPLIT时生效。
        :type SplitShardConfig: :class:`tencentcloud.dcdb.v20180411.models.SplitShardConfig`
        :param _AutoVoucher: 是否自动使用代金券进行支付，默认不使用。
        :type AutoVoucher: bool
        :param _VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。
        :type VoucherIds: list of str
        :param _Zones: 变更部署时指定的新可用区列表，第1个为主可用区，其余为从可用区
        :type Zones: list of str
        :param _SwitchStartTime: 切换开始时间，格式如: "2019-12-12 07:00:00"。开始时间必须在当前时间一个小时以后，3天以内。
        :type SwitchStartTime: str
        :param _SwitchEndTime: 切换结束时间, 格式如: "2019-12-12 07:15:00"，结束时间必须大于开始时间。
        :type SwitchEndTime: str
        :param _SwitchAutoRetry: 是否自动重试。 0：不自动重试 1：自动重试
        :type SwitchAutoRetry: int
        """
        self._InstanceId = None
        self._UpgradeType = None
        self._AddShardConfig = None
        self._ExpandShardConfig = None
        self._SplitShardConfig = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._Zones = None
        self._SwitchStartTime = None
        self._SwitchEndTime = None
        self._SwitchAutoRetry = None

    @property
    def InstanceId(self):
        """待升级的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UpgradeType(self):
        """升级类型，取值范围: 
<li> ADD: 新增分片 </li> 
 <li> EXPAND: 升级实例中的已有分片 </li> 
 <li> SPLIT: 将已有分片中的数据切分到新增分片上</li>
        :rtype: str
        """
        return self._UpgradeType

    @UpgradeType.setter
    def UpgradeType(self, UpgradeType):
        self._UpgradeType = UpgradeType

    @property
    def AddShardConfig(self):
        """新增分片配置，当UpgradeType为ADD时生效。
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.AddShardConfig`
        """
        return self._AddShardConfig

    @AddShardConfig.setter
    def AddShardConfig(self, AddShardConfig):
        self._AddShardConfig = AddShardConfig

    @property
    def ExpandShardConfig(self):
        """扩容分片配置，当UpgradeType为EXPAND时生效。
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ExpandShardConfig`
        """
        return self._ExpandShardConfig

    @ExpandShardConfig.setter
    def ExpandShardConfig(self, ExpandShardConfig):
        self._ExpandShardConfig = ExpandShardConfig

    @property
    def SplitShardConfig(self):
        """切分分片配置，当UpgradeType为SPLIT时生效。
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.SplitShardConfig`
        """
        return self._SplitShardConfig

    @SplitShardConfig.setter
    def SplitShardConfig(self, SplitShardConfig):
        self._SplitShardConfig = SplitShardConfig

    @property
    def AutoVoucher(self):
        """是否自动使用代金券进行支付，默认不使用。
        :rtype: bool
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        """代金券ID列表，目前仅支持指定一张代金券。
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def Zones(self):
        """变更部署时指定的新可用区列表，第1个为主可用区，其余为从可用区
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def SwitchStartTime(self):
        """切换开始时间，格式如: "2019-12-12 07:00:00"。开始时间必须在当前时间一个小时以后，3天以内。
        :rtype: str
        """
        return self._SwitchStartTime

    @SwitchStartTime.setter
    def SwitchStartTime(self, SwitchStartTime):
        self._SwitchStartTime = SwitchStartTime

    @property
    def SwitchEndTime(self):
        """切换结束时间, 格式如: "2019-12-12 07:15:00"，结束时间必须大于开始时间。
        :rtype: str
        """
        return self._SwitchEndTime

    @SwitchEndTime.setter
    def SwitchEndTime(self, SwitchEndTime):
        self._SwitchEndTime = SwitchEndTime

    @property
    def SwitchAutoRetry(self):
        """是否自动重试。 0：不自动重试 1：自动重试
        :rtype: int
        """
        return self._SwitchAutoRetry

    @SwitchAutoRetry.setter
    def SwitchAutoRetry(self, SwitchAutoRetry):
        self._SwitchAutoRetry = SwitchAutoRetry


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UpgradeType = params.get("UpgradeType")
        if params.get("AddShardConfig") is not None:
            self._AddShardConfig = AddShardConfig()
            self._AddShardConfig._deserialize(params.get("AddShardConfig"))
        if params.get("ExpandShardConfig") is not None:
            self._ExpandShardConfig = ExpandShardConfig()
            self._ExpandShardConfig._deserialize(params.get("ExpandShardConfig"))
        if params.get("SplitShardConfig") is not None:
            self._SplitShardConfig = SplitShardConfig()
            self._SplitShardConfig._deserialize(params.get("SplitShardConfig"))
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._Zones = params.get("Zones")
        self._SwitchStartTime = params.get("SwitchStartTime")
        self._SwitchEndTime = params.get("SwitchEndTime")
        self._SwitchAutoRetry = params.get("SwitchAutoRetry")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDCDBInstanceResponse(AbstractModel):
    """UpgradeDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealName: 长订单号。可以据此调用 DescribeOrders
 查询订单详细信息，或在支付失败时调用用户账号相关接口进行支付。
        :type DealName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        """长订单号。可以据此调用 DescribeOrders
 查询订单详细信息，或在支付失败时调用用户账号相关接口进行支付。
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class UpgradeDedicatedDCDBInstanceRequest(AbstractModel):
    """UpgradeDedicatedDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UpgradeType: 升级类型，取值为ADD，SPLIT和EXPAND。ADD-添加分片；SPLIT-切分某个分片；EXPAND-垂直扩容某个分片
        :type UpgradeType: str
        :param _InstanceId: 实例ID，形如 dcdbt-mlfjm74h
        :type InstanceId: str
        :param _AddShardConfig: 当UpgradeType取值为ADD时，添加分片的配置参数
        :type AddShardConfig: :class:`tencentcloud.dcdb.v20180411.models.AddShardConfig`
        :param _ExpandShardConfig: 当UpgradeType取值为EXPAND时，垂直扩容分片的配置参数
        :type ExpandShardConfig: :class:`tencentcloud.dcdb.v20180411.models.ExpandShardConfig`
        :param _SplitShardConfig: 当UpgradeType取值为SPLIT时，切分分片的配置参数
        :type SplitShardConfig: :class:`tencentcloud.dcdb.v20180411.models.SplitShardConfig`
        :param _SwitchAutoRetry: 错过切换时间窗口时，是否自动重试一次，0-否，1-是
        :type SwitchAutoRetry: int
        :param _SwitchStartTime: 切换时间窗口开始时间
        :type SwitchStartTime: str
        :param _SwitchEndTime: 切换时间窗口结束时间
        :type SwitchEndTime: str
        """
        self._UpgradeType = None
        self._InstanceId = None
        self._AddShardConfig = None
        self._ExpandShardConfig = None
        self._SplitShardConfig = None
        self._SwitchAutoRetry = None
        self._SwitchStartTime = None
        self._SwitchEndTime = None

    @property
    def UpgradeType(self):
        """升级类型，取值为ADD，SPLIT和EXPAND。ADD-添加分片；SPLIT-切分某个分片；EXPAND-垂直扩容某个分片
        :rtype: str
        """
        return self._UpgradeType

    @UpgradeType.setter
    def UpgradeType(self, UpgradeType):
        self._UpgradeType = UpgradeType

    @property
    def InstanceId(self):
        """实例ID，形如 dcdbt-mlfjm74h
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AddShardConfig(self):
        """当UpgradeType取值为ADD时，添加分片的配置参数
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.AddShardConfig`
        """
        return self._AddShardConfig

    @AddShardConfig.setter
    def AddShardConfig(self, AddShardConfig):
        self._AddShardConfig = AddShardConfig

    @property
    def ExpandShardConfig(self):
        """当UpgradeType取值为EXPAND时，垂直扩容分片的配置参数
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ExpandShardConfig`
        """
        return self._ExpandShardConfig

    @ExpandShardConfig.setter
    def ExpandShardConfig(self, ExpandShardConfig):
        self._ExpandShardConfig = ExpandShardConfig

    @property
    def SplitShardConfig(self):
        """当UpgradeType取值为SPLIT时，切分分片的配置参数
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.SplitShardConfig`
        """
        return self._SplitShardConfig

    @SplitShardConfig.setter
    def SplitShardConfig(self, SplitShardConfig):
        self._SplitShardConfig = SplitShardConfig

    @property
    def SwitchAutoRetry(self):
        """错过切换时间窗口时，是否自动重试一次，0-否，1-是
        :rtype: int
        """
        return self._SwitchAutoRetry

    @SwitchAutoRetry.setter
    def SwitchAutoRetry(self, SwitchAutoRetry):
        self._SwitchAutoRetry = SwitchAutoRetry

    @property
    def SwitchStartTime(self):
        """切换时间窗口开始时间
        :rtype: str
        """
        return self._SwitchStartTime

    @SwitchStartTime.setter
    def SwitchStartTime(self, SwitchStartTime):
        self._SwitchStartTime = SwitchStartTime

    @property
    def SwitchEndTime(self):
        """切换时间窗口结束时间
        :rtype: str
        """
        return self._SwitchEndTime

    @SwitchEndTime.setter
    def SwitchEndTime(self, SwitchEndTime):
        self._SwitchEndTime = SwitchEndTime


    def _deserialize(self, params):
        self._UpgradeType = params.get("UpgradeType")
        self._InstanceId = params.get("InstanceId")
        if params.get("AddShardConfig") is not None:
            self._AddShardConfig = AddShardConfig()
            self._AddShardConfig._deserialize(params.get("AddShardConfig"))
        if params.get("ExpandShardConfig") is not None:
            self._ExpandShardConfig = ExpandShardConfig()
            self._ExpandShardConfig._deserialize(params.get("ExpandShardConfig"))
        if params.get("SplitShardConfig") is not None:
            self._SplitShardConfig = SplitShardConfig()
            self._SplitShardConfig._deserialize(params.get("SplitShardConfig"))
        self._SwitchAutoRetry = params.get("SwitchAutoRetry")
        self._SwitchStartTime = params.get("SwitchStartTime")
        self._SwitchEndTime = params.get("SwitchEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDedicatedDCDBInstanceResponse(AbstractModel):
    """UpgradeDedicatedDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步任务流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """异步任务流程ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class UpgradeHourDCDBInstanceRequest(AbstractModel):
    """UpgradeHourDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 待升级的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param _UpgradeType: 升级类型，取值范围: 
<li> ADD: 新增分片 </li> 
 <li> EXPAND: 升级实例中的已有分片 </li> 
 <li> SPLIT: 将已有分片中的数据切分到新增分片上</li>
        :type UpgradeType: str
        :param _AddShardConfig: 新增分片配置，当UpgradeType为ADD时生效。
        :type AddShardConfig: :class:`tencentcloud.dcdb.v20180411.models.AddShardConfig`
        :param _ExpandShardConfig: 扩容分片配置，当UpgradeType为EXPAND时生效。
        :type ExpandShardConfig: :class:`tencentcloud.dcdb.v20180411.models.ExpandShardConfig`
        :param _SplitShardConfig: 切分分片配置，当UpgradeType为SPLIT时生效。
        :type SplitShardConfig: :class:`tencentcloud.dcdb.v20180411.models.SplitShardConfig`
        :param _SwitchStartTime: 切换开始时间，格式如: "2019-12-12 07:00:00"。开始时间必须在当前时间一个小时以后，3天以内。
        :type SwitchStartTime: str
        :param _SwitchEndTime: 切换结束时间,  格式如: "2019-12-12 07:15:00"，结束时间必须大于开始时间。
        :type SwitchEndTime: str
        :param _SwitchAutoRetry: 是否自动重试。 0：不自动重试  1：自动重试
        :type SwitchAutoRetry: int
        :param _Zones: 变更部署时指定的新可用区列表，第1个为主可用区，其余为从可用区
        :type Zones: list of str
        """
        self._InstanceId = None
        self._UpgradeType = None
        self._AddShardConfig = None
        self._ExpandShardConfig = None
        self._SplitShardConfig = None
        self._SwitchStartTime = None
        self._SwitchEndTime = None
        self._SwitchAutoRetry = None
        self._Zones = None

    @property
    def InstanceId(self):
        """待升级的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UpgradeType(self):
        """升级类型，取值范围: 
<li> ADD: 新增分片 </li> 
 <li> EXPAND: 升级实例中的已有分片 </li> 
 <li> SPLIT: 将已有分片中的数据切分到新增分片上</li>
        :rtype: str
        """
        return self._UpgradeType

    @UpgradeType.setter
    def UpgradeType(self, UpgradeType):
        self._UpgradeType = UpgradeType

    @property
    def AddShardConfig(self):
        """新增分片配置，当UpgradeType为ADD时生效。
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.AddShardConfig`
        """
        return self._AddShardConfig

    @AddShardConfig.setter
    def AddShardConfig(self, AddShardConfig):
        self._AddShardConfig = AddShardConfig

    @property
    def ExpandShardConfig(self):
        """扩容分片配置，当UpgradeType为EXPAND时生效。
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ExpandShardConfig`
        """
        return self._ExpandShardConfig

    @ExpandShardConfig.setter
    def ExpandShardConfig(self, ExpandShardConfig):
        self._ExpandShardConfig = ExpandShardConfig

    @property
    def SplitShardConfig(self):
        """切分分片配置，当UpgradeType为SPLIT时生效。
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.SplitShardConfig`
        """
        return self._SplitShardConfig

    @SplitShardConfig.setter
    def SplitShardConfig(self, SplitShardConfig):
        self._SplitShardConfig = SplitShardConfig

    @property
    def SwitchStartTime(self):
        """切换开始时间，格式如: "2019-12-12 07:00:00"。开始时间必须在当前时间一个小时以后，3天以内。
        :rtype: str
        """
        return self._SwitchStartTime

    @SwitchStartTime.setter
    def SwitchStartTime(self, SwitchStartTime):
        self._SwitchStartTime = SwitchStartTime

    @property
    def SwitchEndTime(self):
        """切换结束时间,  格式如: "2019-12-12 07:15:00"，结束时间必须大于开始时间。
        :rtype: str
        """
        return self._SwitchEndTime

    @SwitchEndTime.setter
    def SwitchEndTime(self, SwitchEndTime):
        self._SwitchEndTime = SwitchEndTime

    @property
    def SwitchAutoRetry(self):
        """是否自动重试。 0：不自动重试  1：自动重试
        :rtype: int
        """
        return self._SwitchAutoRetry

    @SwitchAutoRetry.setter
    def SwitchAutoRetry(self, SwitchAutoRetry):
        self._SwitchAutoRetry = SwitchAutoRetry

    @property
    def Zones(self):
        """变更部署时指定的新可用区列表，第1个为主可用区，其余为从可用区
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UpgradeType = params.get("UpgradeType")
        if params.get("AddShardConfig") is not None:
            self._AddShardConfig = AddShardConfig()
            self._AddShardConfig._deserialize(params.get("AddShardConfig"))
        if params.get("ExpandShardConfig") is not None:
            self._ExpandShardConfig = ExpandShardConfig()
            self._ExpandShardConfig._deserialize(params.get("ExpandShardConfig"))
        if params.get("SplitShardConfig") is not None:
            self._SplitShardConfig = SplitShardConfig()
            self._SplitShardConfig._deserialize(params.get("SplitShardConfig"))
        self._SwitchStartTime = params.get("SwitchStartTime")
        self._SwitchEndTime = params.get("SwitchEndTime")
        self._SwitchAutoRetry = params.get("SwitchAutoRetry")
        self._Zones = params.get("Zones")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeHourDCDBInstanceResponse(AbstractModel):
    """UpgradeHourDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UserTaskInfo(AbstractModel):
    """用户任务信息

    """

    def __init__(self):
        r"""
        :param _Id: 任务ID
        :type Id: int
        :param _AppId: 用户账户ID
        :type AppId: int
        :param _Status: 任务状态，0-任务初始化中；1-任务运行中；2-任务成功；3-任务失败
        :type Status: int
        :param _UserTaskType: 任务类型，0-实例回档；1-实例创建；2-实例扩容；3-实例迁移；4-实例删除；5-实例重启
        :type UserTaskType: int
        :param _CreateTime: 任务创建时间
        :type CreateTime: str
        :param _EndTime: 任务结束时间
        :type EndTime: str
        :param _ErrMsg: 任务错误信息
        :type ErrMsg: str
        :param _InputData: 客户端参数
        :type InputData: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _RegionId: 地域ID
        :type RegionId: int
        """
        self._Id = None
        self._AppId = None
        self._Status = None
        self._UserTaskType = None
        self._CreateTime = None
        self._EndTime = None
        self._ErrMsg = None
        self._InputData = None
        self._InstanceId = None
        self._InstanceName = None
        self._RegionId = None

    @property
    def Id(self):
        """任务ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AppId(self):
        """用户账户ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Status(self):
        """任务状态，0-任务初始化中；1-任务运行中；2-任务成功；3-任务失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UserTaskType(self):
        """任务类型，0-实例回档；1-实例创建；2-实例扩容；3-实例迁移；4-实例删除；5-实例重启
        :rtype: int
        """
        return self._UserTaskType

    @UserTaskType.setter
    def UserTaskType(self, UserTaskType):
        self._UserTaskType = UserTaskType

    @property
    def CreateTime(self):
        """任务创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EndTime(self):
        """任务结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ErrMsg(self):
        """任务错误信息
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def InputData(self):
        """客户端参数
        :rtype: str
        """
        return self._InputData

    @InputData.setter
    def InputData(self, InputData):
        self._InputData = InputData

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def RegionId(self):
        """地域ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._AppId = params.get("AppId")
        self._Status = params.get("Status")
        self._UserTaskType = params.get("UserTaskType")
        self._CreateTime = params.get("CreateTime")
        self._EndTime = params.get("EndTime")
        self._ErrMsg = params.get("ErrMsg")
        self._InputData = params.get("InputData")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ViewPrivileges(AbstractModel):
    """视图权限信息

    """

    def __init__(self):
        r"""
        :param _Database: 数据库名
        :type Database: str
        :param _View: 数据库视图名
        :type View: str
        :param _Privileges: 权限信息
        :type Privileges: list of str
        """
        self._Database = None
        self._View = None
        self._Privileges = None

    @property
    def Database(self):
        """数据库名
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def View(self):
        """数据库视图名
        :rtype: str
        """
        return self._View

    @View.setter
    def View(self, View):
        self._View = View

    @property
    def Privileges(self):
        """权限信息
        :rtype: list of str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._View = params.get("View")
        self._Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZonesInfo(AbstractModel):
    """可用区信息

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区英文ID
        :type Zone: str
        :param _ZoneId: 可用区数字ID
        :type ZoneId: int
        :param _ZoneName: 可用区中文名
        :type ZoneName: str
        :param _OnSale: 是否在售
        :type OnSale: bool
        """
        self._Zone = None
        self._ZoneId = None
        self._ZoneName = None
        self._OnSale = None

    @property
    def Zone(self):
        """可用区英文ID
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneId(self):
        """可用区数字ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        """可用区中文名
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def OnSale(self):
        """是否在售
        :rtype: bool
        """
        return self._OnSale

    @OnSale.setter
    def OnSale(self, OnSale):
        self._OnSale = OnSale


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._OnSale = params.get("OnSale")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        