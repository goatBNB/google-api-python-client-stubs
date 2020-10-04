import typing

import typing_extensions
@typing.type_check_only
class ApplyParametersRequest(typing_extensions.TypedDict, total=False):
    applyAll: bool
    nodeIds: typing.List[str]

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudMemcacheV1beta2LocationMetadata(
    typing_extensions.TypedDict, total=False
):
    availableZones: typing.Dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudMemcacheV1beta2OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1Instance(
    typing_extensions.TypedDict, total=False
):
    consumerDefinedName: str
    createTime: str
    labels: typing.Dict[str, typing.Any]
    maintenancePolicyNames: typing.Dict[str, typing.Any]
    maintenanceSchedules: typing.Dict[str, typing.Any]
    maintenanceSettings: GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettings
    name: str
    producerMetadata: typing.Dict[str, typing.Any]
    provisionedResources: typing.List[
        GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResource
    ]
    slmInstanceTemplate: str
    sloMetadata: GoogleCloudSaasacceleratorManagementProvidersV1SloMetadata
    softwareVersions: typing.Dict[str, typing.Any]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "UPDATING",
        "REPAIRING",
        "DELETING",
        "ERROR",
    ]
    tenantProjectId: str
    updateTime: str

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSchedule(
    typing_extensions.TypedDict, total=False
):
    canReschedule: bool
    endTime: str
    rolloutManagementPolicy: str
    startTime: str

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettings(
    typing_extensions.TypedDict, total=False
):
    exclude: bool

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadata(
    typing_extensions.TypedDict, total=False
):
    exclusions: typing.List[GoogleCloudSaasacceleratorManagementProvidersV1SloExclusion]
    location: str
    nodeId: str

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResource(
    typing_extensions.TypedDict, total=False
):
    resourceType: str
    resourceUrl: str

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1SloEligibility(
    typing_extensions.TypedDict, total=False
):
    eligible: bool
    reason: str

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1SloExclusion(
    typing_extensions.TypedDict, total=False
):
    duration: str
    reason: str
    sliName: str
    startTime: str

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1SloMetadata(
    typing_extensions.TypedDict, total=False
):
    eligibility: GoogleCloudSaasacceleratorManagementProvidersV1SloEligibility
    exclusions: typing.List[GoogleCloudSaasacceleratorManagementProvidersV1SloExclusion]
    nodes: typing.List[GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadata]
    tier: str

@typing.type_check_only
class Instance(typing_extensions.TypedDict, total=False):
    authorizedNetwork: str
    createTime: str
    discoveryEndpoint: str
    displayName: str
    instanceMessages: typing.List[InstanceMessage]
    labels: typing.Dict[str, typing.Any]
    memcacheFullVersion: str
    memcacheNodes: typing.List[Node]
    memcacheVersion: typing_extensions.Literal[
        "MEMCACHE_VERSION_UNSPECIFIED", "MEMCACHE_1_5"
    ]
    name: str
    nodeConfig: NodeConfig
    nodeCount: int
    parameters: MemcacheParameters
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "DELETING", "PERFORMING_MAINTENANCE"
    ]
    updateTime: str
    zones: typing.List[str]

@typing.type_check_only
class InstanceMessage(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal["CODE_UNSPECIFIED", "ZONE_DISTRIBUTION_UNBALANCED"]
    message: str

@typing.type_check_only
class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    resources: typing.List[Instance]
    unreachable: typing.List[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class MemcacheParameters(typing_extensions.TypedDict, total=False):
    id: str
    params: typing.Dict[str, typing.Any]

@typing.type_check_only
class Node(typing_extensions.TypedDict, total=False):
    host: str
    nodeId: str
    parameters: MemcacheParameters
    port: int
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "DELETING", "UPDATING"
    ]
    zone: str

@typing.type_check_only
class NodeConfig(typing_extensions.TypedDict, total=False):
    cpuCount: int
    memorySizeMb: int

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class UpdateParametersRequest(typing_extensions.TypedDict, total=False):
    parameters: MemcacheParameters
    updateMask: str

@typing.type_check_only
class ZoneMetadata(typing_extensions.TypedDict, total=False): ...