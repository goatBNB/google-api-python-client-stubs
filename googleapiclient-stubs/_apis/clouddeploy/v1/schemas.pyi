import typing

import typing_extensions

_list = list

@typing.type_check_only
class AbandonReleaseRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AbandonReleaseResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AdvanceChildRolloutJob(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AdvanceChildRolloutJobRun(typing_extensions.TypedDict, total=False):
    rollout: str
    rolloutPhaseId: str

@typing.type_check_only
class AdvanceRolloutRequest(typing_extensions.TypedDict, total=False):
    phaseId: str

@typing.type_check_only
class AdvanceRolloutResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AnthosCluster(typing_extensions.TypedDict, total=False):
    membership: str

@typing.type_check_only
class ApproveRolloutRequest(typing_extensions.TypedDict, total=False):
    approved: bool

@typing.type_check_only
class ApproveRolloutResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class BuildArtifact(typing_extensions.TypedDict, total=False):
    image: str
    tag: str

@typing.type_check_only
class Canary(typing_extensions.TypedDict, total=False):
    canaryDeployment: CanaryDeployment
    customCanaryDeployment: CustomCanaryDeployment
    runtimeConfig: RuntimeConfig

@typing.type_check_only
class CanaryDeployment(typing_extensions.TypedDict, total=False):
    percentages: _list[int]
    verify: bool

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CancelRolloutRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CancelRolloutResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ChildRolloutJobs(typing_extensions.TypedDict, total=False):
    advanceRolloutJobs: _list[Job]
    createRolloutJobs: _list[Job]

@typing.type_check_only
class CloudRunConfig(typing_extensions.TypedDict, total=False):
    automaticTrafficControl: bool

@typing.type_check_only
class CloudRunLocation(typing_extensions.TypedDict, total=False):
    location: str

@typing.type_check_only
class CloudRunMetadata(typing_extensions.TypedDict, total=False):
    revision: str
    service: str
    serviceUrls: _list[str]

@typing.type_check_only
class CloudRunRenderMetadata(typing_extensions.TypedDict, total=False):
    service: str

@typing.type_check_only
class Config(typing_extensions.TypedDict, total=False):
    defaultSkaffoldVersion: str
    name: str
    supportedVersions: _list[SkaffoldVersion]

@typing.type_check_only
class CreateChildRolloutJob(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CreateChildRolloutJobRun(typing_extensions.TypedDict, total=False):
    rollout: str
    rolloutPhaseId: str

@typing.type_check_only
class CustomCanaryDeployment(typing_extensions.TypedDict, total=False):
    phaseConfigs: _list[PhaseConfig]

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DefaultPool(typing_extensions.TypedDict, total=False):
    artifactStorage: str
    serviceAccount: str

@typing.type_check_only
class DeliveryPipeline(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    condition: PipelineCondition
    createTime: str
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    serialPipeline: SerialPipeline
    suspended: bool
    uid: str
    updateTime: str

@typing.type_check_only
class DeliveryPipelineNotificationEvent(typing_extensions.TypedDict, total=False):
    deliveryPipeline: str
    message: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "TYPE_PUBSUB_NOTIFICATION_FAILURE",
        "TYPE_RENDER_STATUES_CHANGE",
    ]

@typing.type_check_only
class DeployJob(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeployJobRun(typing_extensions.TypedDict, total=False):
    build: str
    failureCause: typing_extensions.Literal[
        "FAILURE_CAUSE_UNSPECIFIED",
        "CLOUD_BUILD_UNAVAILABLE",
        "EXECUTION_FAILED",
        "DEADLINE_EXCEEDED",
        "MISSING_RESOURCES_FOR_CANARY",
        "CLOUD_BUILD_REQUEST_FAILED",
    ]
    failureMessage: str
    metadata: DeployJobRunMetadata

@typing.type_check_only
class DeployJobRunMetadata(typing_extensions.TypedDict, total=False):
    cloudRun: CloudRunMetadata

@typing.type_check_only
class DeploymentJobs(typing_extensions.TypedDict, total=False):
    deployJob: Job
    verifyJob: Job

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExecutionConfig(typing_extensions.TypedDict, total=False):
    artifactStorage: str
    defaultPool: DefaultPool
    executionTimeout: str
    privatePool: PrivatePool
    serviceAccount: str
    usages: _list[str]
    workerPool: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GatewayServiceMesh(typing_extensions.TypedDict, total=False):
    deployment: str
    httpRoute: str
    service: str

@typing.type_check_only
class GkeCluster(typing_extensions.TypedDict, total=False):
    cluster: str
    internalIp: bool

@typing.type_check_only
class IgnoreJobRequest(typing_extensions.TypedDict, total=False):
    jobId: str
    phaseId: str

@typing.type_check_only
class IgnoreJobResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Job(typing_extensions.TypedDict, total=False):
    advanceChildRolloutJob: AdvanceChildRolloutJob
    createChildRolloutJob: CreateChildRolloutJob
    deployJob: DeployJob
    id: str
    jobRun: str
    skipMessage: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "DISABLED",
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
        "ABORTED",
        "SKIPPED",
        "IGNORED",
    ]
    verifyJob: VerifyJob

@typing.type_check_only
class JobRun(typing_extensions.TypedDict, total=False):
    advanceChildRolloutJobRun: AdvanceChildRolloutJobRun
    createChildRolloutJobRun: CreateChildRolloutJobRun
    createTime: str
    deployJobRun: DeployJobRun
    endTime: str
    etag: str
    jobId: str
    name: str
    phaseId: str
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
        "TERMINATING",
        "TERMINATED",
    ]
    uid: str
    verifyJobRun: VerifyJobRun

@typing.type_check_only
class JobRunNotificationEvent(typing_extensions.TypedDict, total=False):
    jobRun: str
    message: str
    pipelineUid: str
    releaseUid: str
    rolloutUid: str
    targetId: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "TYPE_PUBSUB_NOTIFICATION_FAILURE",
        "TYPE_RENDER_STATUES_CHANGE",
    ]

@typing.type_check_only
class KubernetesConfig(typing_extensions.TypedDict, total=False):
    gatewayServiceMesh: GatewayServiceMesh
    serviceNetworking: ServiceNetworking

@typing.type_check_only
class ListDeliveryPipelinesResponse(typing_extensions.TypedDict, total=False):
    deliveryPipelines: _list[DeliveryPipeline]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListJobRunsResponse(typing_extensions.TypedDict, total=False):
    jobRuns: _list[JobRun]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListReleasesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    releases: _list[Release]
    unreachable: _list[str]

@typing.type_check_only
class ListRolloutsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    rollouts: _list[Rollout]
    unreachable: _list[str]

@typing.type_check_only
class ListTargetsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    targets: _list[Target]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Metadata(typing_extensions.TypedDict, total=False):
    cloudRun: CloudRunMetadata

@typing.type_check_only
class MultiTarget(typing_extensions.TypedDict, total=False):
    targetIds: _list[str]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Phase(typing_extensions.TypedDict, total=False):
    childRolloutJobs: ChildRolloutJobs
    deploymentJobs: DeploymentJobs
    id: str
    skipMessage: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
        "ABORTED",
        "SKIPPED",
    ]

@typing.type_check_only
class PhaseArtifact(typing_extensions.TypedDict, total=False):
    manifestPath: str
    skaffoldConfigPath: str

@typing.type_check_only
class PhaseConfig(typing_extensions.TypedDict, total=False):
    percentage: int
    phaseId: str
    profiles: _list[str]
    verify: bool

@typing.type_check_only
class PipelineCondition(typing_extensions.TypedDict, total=False):
    pipelineReadyCondition: PipelineReadyCondition
    targetsPresentCondition: TargetsPresentCondition
    targetsTypeCondition: TargetsTypeCondition

@typing.type_check_only
class PipelineReadyCondition(typing_extensions.TypedDict, total=False):
    status: bool
    updateTime: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PrivatePool(typing_extensions.TypedDict, total=False):
    artifactStorage: str
    serviceAccount: str
    workerPool: str

@typing.type_check_only
class Release(typing_extensions.TypedDict, total=False):
    abandoned: bool
    annotations: dict[str, typing.Any]
    buildArtifacts: _list[BuildArtifact]
    condition: ReleaseCondition
    createTime: str
    deliveryPipelineSnapshot: DeliveryPipeline
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    renderEndTime: str
    renderStartTime: str
    renderState: typing_extensions.Literal[
        "RENDER_STATE_UNSPECIFIED", "SUCCEEDED", "FAILED", "IN_PROGRESS"
    ]
    skaffoldConfigPath: str
    skaffoldConfigUri: str
    skaffoldVersion: str
    targetArtifacts: dict[str, typing.Any]
    targetRenders: dict[str, typing.Any]
    targetSnapshots: _list[Target]
    uid: str

@typing.type_check_only
class ReleaseCondition(typing_extensions.TypedDict, total=False):
    releaseReadyCondition: ReleaseReadyCondition
    skaffoldSupportedCondition: SkaffoldSupportedCondition

@typing.type_check_only
class ReleaseNotificationEvent(typing_extensions.TypedDict, total=False):
    message: str
    release: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "TYPE_PUBSUB_NOTIFICATION_FAILURE",
        "TYPE_RENDER_STATUES_CHANGE",
    ]

@typing.type_check_only
class ReleaseReadyCondition(typing_extensions.TypedDict, total=False):
    status: bool

@typing.type_check_only
class ReleaseRenderEvent(typing_extensions.TypedDict, total=False):
    message: str
    release: str

@typing.type_check_only
class RenderMetadata(typing_extensions.TypedDict, total=False):
    cloudRun: CloudRunRenderMetadata

@typing.type_check_only
class RetryJobRequest(typing_extensions.TypedDict, total=False):
    jobId: str
    phaseId: str

@typing.type_check_only
class RetryJobResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Rollout(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    approvalState: typing_extensions.Literal[
        "APPROVAL_STATE_UNSPECIFIED",
        "NEEDS_APPROVAL",
        "DOES_NOT_NEED_APPROVAL",
        "APPROVED",
        "REJECTED",
    ]
    approveTime: str
    controllerRollout: str
    createTime: str
    deployEndTime: str
    deployFailureCause: typing_extensions.Literal[
        "FAILURE_CAUSE_UNSPECIFIED",
        "CLOUD_BUILD_UNAVAILABLE",
        "EXECUTION_FAILED",
        "DEADLINE_EXCEEDED",
        "RELEASE_FAILED",
        "RELEASE_ABANDONED",
        "VERIFICATION_CONFIG_NOT_FOUND",
        "CLOUD_BUILD_REQUEST_FAILED",
    ]
    deployStartTime: str
    deployingBuild: str
    description: str
    enqueueTime: str
    etag: str
    failureReason: str
    labels: dict[str, typing.Any]
    metadata: Metadata
    name: str
    phases: _list[Phase]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "SUCCEEDED",
        "FAILED",
        "IN_PROGRESS",
        "PENDING_APPROVAL",
        "APPROVAL_REJECTED",
        "PENDING",
        "PENDING_RELEASE",
        "CANCELLING",
        "CANCELLED",
        "HALTED",
    ]
    targetId: str
    uid: str

@typing.type_check_only
class RolloutNotificationEvent(typing_extensions.TypedDict, total=False):
    message: str
    pipelineUid: str
    releaseUid: str
    rollout: str
    targetId: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "TYPE_PUBSUB_NOTIFICATION_FAILURE",
        "TYPE_RENDER_STATUES_CHANGE",
    ]

@typing.type_check_only
class RuntimeConfig(typing_extensions.TypedDict, total=False):
    cloudRun: CloudRunConfig
    kubernetes: KubernetesConfig

@typing.type_check_only
class SerialPipeline(typing_extensions.TypedDict, total=False):
    stages: _list[Stage]

@typing.type_check_only
class ServiceNetworking(typing_extensions.TypedDict, total=False):
    deployment: str
    service: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SkaffoldSupportedCondition(typing_extensions.TypedDict, total=False):
    maintenanceModeTime: str
    skaffoldSupportState: typing_extensions.Literal[
        "SKAFFOLD_SUPPORT_STATE_UNSPECIFIED",
        "SKAFFOLD_SUPPORT_STATE_SUPPORTED",
        "SKAFFOLD_SUPPORT_STATE_MAINTENANCE_MODE",
        "SKAFFOLD_SUPPORT_STATE_UNSUPPORTED",
    ]
    status: bool
    supportExpirationTime: str

@typing.type_check_only
class SkaffoldVersion(typing_extensions.TypedDict, total=False):
    maintenanceModeTime: str
    supportEndDate: Date
    supportExpirationTime: str
    version: str

@typing.type_check_only
class Stage(typing_extensions.TypedDict, total=False):
    profiles: _list[str]
    strategy: Strategy
    targetId: str

@typing.type_check_only
class Standard(typing_extensions.TypedDict, total=False):
    verify: bool

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Strategy(typing_extensions.TypedDict, total=False):
    canary: Canary
    standard: Standard

@typing.type_check_only
class Target(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    anthosCluster: AnthosCluster
    createTime: str
    description: str
    etag: str
    executionConfigs: _list[ExecutionConfig]
    gke: GkeCluster
    labels: dict[str, typing.Any]
    multiTarget: MultiTarget
    name: str
    requireApproval: bool
    run: CloudRunLocation
    targetId: str
    uid: str
    updateTime: str

@typing.type_check_only
class TargetArtifact(typing_extensions.TypedDict, total=False):
    artifactUri: str
    manifestPath: str
    phaseArtifacts: dict[str, typing.Any]
    skaffoldConfigPath: str

@typing.type_check_only
class TargetNotificationEvent(typing_extensions.TypedDict, total=False):
    message: str
    target: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "TYPE_PUBSUB_NOTIFICATION_FAILURE",
        "TYPE_RENDER_STATUES_CHANGE",
    ]

@typing.type_check_only
class TargetRender(typing_extensions.TypedDict, total=False):
    failureCause: typing_extensions.Literal[
        "FAILURE_CAUSE_UNSPECIFIED",
        "CLOUD_BUILD_UNAVAILABLE",
        "EXECUTION_FAILED",
        "CLOUD_BUILD_REQUEST_FAILED",
    ]
    failureMessage: str
    metadata: RenderMetadata
    renderingBuild: str
    renderingState: typing_extensions.Literal[
        "TARGET_RENDER_STATE_UNSPECIFIED", "SUCCEEDED", "FAILED", "IN_PROGRESS"
    ]

@typing.type_check_only
class TargetsPresentCondition(typing_extensions.TypedDict, total=False):
    missingTargets: _list[str]
    status: bool
    updateTime: str

@typing.type_check_only
class TargetsTypeCondition(typing_extensions.TypedDict, total=False):
    errorDetails: str
    status: bool

@typing.type_check_only
class TerminateJobRunRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class TerminateJobRunResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class VerifyJob(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class VerifyJobRun(typing_extensions.TypedDict, total=False):
    artifactUri: str
    build: str
    eventLogPath: str
    failureCause: typing_extensions.Literal[
        "FAILURE_CAUSE_UNSPECIFIED",
        "CLOUD_BUILD_UNAVAILABLE",
        "EXECUTION_FAILED",
        "DEADLINE_EXCEEDED",
        "VERIFICATION_CONFIG_NOT_FOUND",
        "CLOUD_BUILD_REQUEST_FAILED",
    ]
    failureMessage: str
