import typing

import typing_extensions

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Authority(typing_extensions.TypedDict, total=False):
    identityProvider: str
    issuer: str
    oidcJwks: str
    workloadIdentityPool: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ConnectAgentResource(typing_extensions.TypedDict, total=False):
    manifest: str
    type: TypeMeta

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GenerateConnectManifestResponse(typing_extensions.TypedDict, total=False):
    manifest: typing.List[ConnectAgentResource]

@typing.type_check_only
class GkeCluster(typing_extensions.TypedDict, total=False):
    resourceLink: str

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class KubernetesMetadata(typing_extensions.TypedDict, total=False):
    kubernetesApiServerVersion: str
    memoryMb: int
    nodeCount: int
    nodeProviderId: str
    updateTime: str
    vcpuCount: int

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

@typing.type_check_only
class ListMembershipsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    resources: typing.List[Membership]
    unreachable: typing.List[str]

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
class Membership(typing_extensions.TypedDict, total=False):
    authority: Authority
    createTime: str
    deleteTime: str
    description: str
    endpoint: MembershipEndpoint
    externalId: str
    labels: typing.Dict[str, typing.Any]
    lastConnectionTime: str
    name: str
    state: MembershipState
    uniqueId: str
    updateTime: str

@typing.type_check_only
class MembershipEndpoint(typing_extensions.TypedDict, total=False):
    gkeCluster: GkeCluster
    kubernetesMetadata: KubernetesMetadata

@typing.type_check_only
class MembershipState(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED",
        "CREATING",
        "READY",
        "DELETING",
        "UPDATING",
        "SERVICE_UPDATING",
    ]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    etag: str
    version: int

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TypeMeta(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
