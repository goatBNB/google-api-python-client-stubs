import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class DeploymentManagerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class DeploymentsResource(googleapiclient.discovery.Resource):
        def cancelPreview(
            self,
            *,
            project: str,
            deployment: str,
            body: DeploymentsCancelPreviewRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            deployment: str,
            deletePolicy: typing_extensions.Literal["ABANDON", "DELETE"] = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, deployment: str, **kwargs: typing.Any
        ) -> DeploymentHttpRequest: ...
        def getIamPolicy(
            self, *, project: str, resource: str, **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: Deployment = ...,
            createPolicy: typing_extensions.Literal[
                "ACQUIRE", "CREATE_OR_ACQUIRE"
            ] = ...,
            preview: bool = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> DeploymentsListResponseHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            deployment: str,
            body: Deployment = ...,
            createPolicy: typing_extensions.Literal[
                "ACQUIRE", "CREATE_OR_ACQUIRE"
            ] = ...,
            deletePolicy: typing_extensions.Literal["ABANDON", "DELETE"] = ...,
            preview: bool = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            project: str,
            resource: str,
            body: GlobalSetPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def stop(
            self,
            *,
            project: str,
            deployment: str,
            body: DeploymentsStopRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            deployment: str,
            body: Deployment = ...,
            createPolicy: typing_extensions.Literal[
                "ACQUIRE", "CREATE_OR_ACQUIRE"
            ] = ...,
            deletePolicy: typing_extensions.Literal["ABANDON", "DELETE"] = ...,
            preview: bool = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    @typing.type_check_only
    class ManifestsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, project: str, deployment: str, manifest: str, **kwargs: typing.Any
        ) -> ManifestHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            deployment: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ManifestsListResponseHttpRequest: ...
    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, project: str, operation: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> OperationsListResponseHttpRequest: ...
    @typing.type_check_only
    class ResourcesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, project: str, deployment: str, resource: str, **kwargs: typing.Any
        ) -> ResourceHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            deployment: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ResourcesListResponseHttpRequest: ...
    @typing.type_check_only
    class TypesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            project: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> TypesListResponseHttpRequest: ...
    def deployments(self) -> DeploymentsResource: ...
    def manifests(self) -> ManifestsResource: ...
    def operations(self) -> OperationsResource: ...
    def resources(self) -> ResourcesResource: ...
    def types(self) -> TypesResource: ...

@typing.type_check_only
class DeploymentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Deployment: ...

@typing.type_check_only
class DeploymentsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DeploymentsListResponse: ...

@typing.type_check_only
class ManifestHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Manifest: ...

@typing.type_check_only
class ManifestsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ManifestsListResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

@typing.type_check_only
class OperationsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OperationsListResponse: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

@typing.type_check_only
class ResourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Resource: ...

@typing.type_check_only
class ResourcesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ResourcesListResponse: ...

@typing.type_check_only
class TestPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestPermissionsResponse: ...

@typing.type_check_only
class TypesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TypesListResponse: ...