import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class AdMobResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class MediationReportResource(googleapiclient.discovery.Resource):
            def generate(
                self,
                *,
                parent: str,
                body: GenerateMediationReportRequest = ...,
                **kwargs: typing.Any
            ) -> GenerateMediationReportResponseHttpRequest: ...
        @typing.type_check_only
        class NetworkReportResource(googleapiclient.discovery.Resource):
            def generate(
                self,
                *,
                parent: str,
                body: GenerateNetworkReportRequest = ...,
                **kwargs: typing.Any
            ) -> GenerateNetworkReportResponseHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> PublisherAccountHttpRequest: ...
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> ListPublisherAccountsResponseHttpRequest: ...
        def mediationReport(self) -> MediationReportResource: ...
        def networkReport(self) -> NetworkReportResource: ...
    def accounts(self) -> AccountsResource: ...

@typing.type_check_only
class GenerateMediationReportResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GenerateMediationReportResponse: ...

@typing.type_check_only
class GenerateNetworkReportResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GenerateNetworkReportResponse: ...

@typing.type_check_only
class ListPublisherAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListPublisherAccountsResponse: ...

@typing.type_check_only
class PublisherAccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PublisherAccount: ...