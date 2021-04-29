import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

@typing.type_check_only
class GoogleAnalyticsAdminResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountSummariesResource(googleapiclient.discovery.Resource):
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaListAccountSummariesResponseHttpRequest: ...
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class UserLinksResource(googleapiclient.discovery.Resource):
            def audit(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaAuditUserLinksRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaAuditUserLinksResponseHttpRequest: ...
            def batchCreate(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaBatchCreateUserLinksRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaBatchCreateUserLinksResponseHttpRequest: ...
            def batchDelete(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaBatchDeleteUserLinksRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def batchGet(
                self,
                *,
                parent: str,
                names: typing.Union[str, typing.List[str]] = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaBatchGetUserLinksResponseHttpRequest: ...
            def batchUpdate(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksResponseHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaUserLink = ...,
                notifyNewUser: bool = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaUserLinkHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaUserLinkHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListUserLinksResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaUserLink = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaUserLinkHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleProtobufEmptyHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaAccountHttpRequest: ...
        def getDataSharingSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaDataSharingSettingsHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            showDeleted: bool = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaListAccountsResponseHttpRequest: ...
        def patch(
            self,
            *,
            name: str,
            body: GoogleAnalyticsAdminV1alphaAccount = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaAccountHttpRequest: ...
        def provisionAccountTicket(
            self,
            *,
            body: GoogleAnalyticsAdminV1alphaProvisionAccountTicketRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaProvisionAccountTicketResponseHttpRequest: ...
        def searchChangeHistoryEvents(
            self,
            *,
            account: str,
            body: GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponseHttpRequest: ...
        def userLinks(self) -> UserLinksResource: ...
    @typing.type_check_only
    class PropertiesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AndroidAppDataStreamsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class MeasurementProtocolSecretsResource(
                googleapiclient.discovery.Resource
            ):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret = ...,
                    **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1alphaMeasurementProtocolSecretHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1alphaMeasurementProtocolSecretHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1alphaMeasurementProtocolSecretHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaAndroidAppDataStreamHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListAndroidAppDataStreamsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaAndroidAppDataStream = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaAndroidAppDataStreamHttpRequest: ...
            def measurementProtocolSecrets(
                self,
            ) -> MeasurementProtocolSecretsResource: ...
        @typing.type_check_only
        class ConversionEventsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaConversionEvent = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaConversionEventHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaConversionEventHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListConversionEventsResponseHttpRequest: ...
        @typing.type_check_only
        class CustomDimensionsResource(googleapiclient.discovery.Resource):
            def archive(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaArchiveCustomDimensionRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaCustomDimension = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaCustomDimensionHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaCustomDimensionHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListCustomDimensionsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaCustomDimension = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaCustomDimensionHttpRequest: ...
        @typing.type_check_only
        class CustomMetricsResource(googleapiclient.discovery.Resource):
            def archive(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaArchiveCustomMetricRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaCustomMetric = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaCustomMetricHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaCustomMetricHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListCustomMetricsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaCustomMetric = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaCustomMetricHttpRequest: ...
        @typing.type_check_only
        class FirebaseLinksResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaFirebaseLink = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaFirebaseLinkHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListFirebaseLinksResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaFirebaseLink = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaFirebaseLinkHttpRequest: ...
        @typing.type_check_only
        class GoogleAdsLinksResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaGoogleAdsLink = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaGoogleAdsLinkHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaGoogleAdsLink = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaGoogleAdsLinkHttpRequest: ...
        @typing.type_check_only
        class IosAppDataStreamsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class MeasurementProtocolSecretsResource(
                googleapiclient.discovery.Resource
            ):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret = ...,
                    **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1alphaMeasurementProtocolSecretHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1alphaMeasurementProtocolSecretHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1alphaMeasurementProtocolSecretHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaIosAppDataStreamHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListIosAppDataStreamsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaIosAppDataStream = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaIosAppDataStreamHttpRequest: ...
            def measurementProtocolSecrets(
                self,
            ) -> MeasurementProtocolSecretsResource: ...
        @typing.type_check_only
        class UserLinksResource(googleapiclient.discovery.Resource):
            def audit(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaAuditUserLinksRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaAuditUserLinksResponseHttpRequest: ...
            def batchCreate(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaBatchCreateUserLinksRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaBatchCreateUserLinksResponseHttpRequest: ...
            def batchDelete(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaBatchDeleteUserLinksRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def batchGet(
                self,
                *,
                parent: str,
                names: typing.Union[str, typing.List[str]] = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaBatchGetUserLinksResponseHttpRequest: ...
            def batchUpdate(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksResponseHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaUserLink = ...,
                notifyNewUser: bool = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaUserLinkHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaUserLinkHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListUserLinksResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaUserLink = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaUserLinkHttpRequest: ...
        @typing.type_check_only
        class WebDataStreamsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class MeasurementProtocolSecretsResource(
                googleapiclient.discovery.Resource
            ):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret = ...,
                    **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1alphaMeasurementProtocolSecretHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1alphaMeasurementProtocolSecretHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1alphaMeasurementProtocolSecretHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaWebDataStream = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaWebDataStreamHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaWebDataStreamHttpRequest: ...
            def getEnhancedMeasurementSettings(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettingsHttpRequest: ...
            def getGlobalSiteTag(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaGlobalSiteTagHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListWebDataStreamsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaWebDataStream = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaWebDataStreamHttpRequest: ...
            def updateEnhancedMeasurementSettings(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettingsHttpRequest: ...
            def measurementProtocolSecrets(
                self,
            ) -> MeasurementProtocolSecretsResource: ...
        def create(
            self,
            *,
            body: GoogleAnalyticsAdminV1alphaProperty = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaPropertyHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaPropertyHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaPropertyHttpRequest: ...
        def getGoogleSignalsSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaGoogleSignalsSettingsHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            showDeleted: bool = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaListPropertiesResponseHttpRequest: ...
        def patch(
            self,
            *,
            name: str,
            body: GoogleAnalyticsAdminV1alphaProperty = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaPropertyHttpRequest: ...
        def updateGoogleSignalsSettings(
            self,
            *,
            name: str,
            body: GoogleAnalyticsAdminV1alphaGoogleSignalsSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaGoogleSignalsSettingsHttpRequest: ...
        def androidAppDataStreams(self) -> AndroidAppDataStreamsResource: ...
        def conversionEvents(self) -> ConversionEventsResource: ...
        def customDimensions(self) -> CustomDimensionsResource: ...
        def customMetrics(self) -> CustomMetricsResource: ...
        def firebaseLinks(self) -> FirebaseLinksResource: ...
        def googleAdsLinks(self) -> GoogleAdsLinksResource: ...
        def iosAppDataStreams(self) -> IosAppDataStreamsResource: ...
        def userLinks(self) -> UserLinksResource: ...
        def webDataStreams(self) -> WebDataStreamsResource: ...
    def accountSummaries(self) -> AccountSummariesResource: ...
    def accounts(self) -> AccountsResource: ...
    def properties(self) -> PropertiesResource: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaAccount: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAndroidAppDataStreamHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaAndroidAppDataStream: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAuditUserLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaAuditUserLinksResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchCreateUserLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaBatchCreateUserLinksResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchGetUserLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaBatchGetUserLinksResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaConversionEventHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaConversionEvent: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaCustomDimensionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaCustomDimension: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaCustomMetricHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaCustomMetric: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDataSharingSettingsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaDataSharingSettings: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettingsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaFirebaseLinkHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaFirebaseLink: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaGlobalSiteTagHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaGlobalSiteTag: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaGoogleAdsLinkHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaGoogleAdsLink: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaGoogleSignalsSettingsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaGoogleSignalsSettings: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaIosAppDataStreamHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaIosAppDataStream: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListAccountSummariesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListAccountSummariesResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListAccountsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListAccountsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListAndroidAppDataStreamsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListAndroidAppDataStreamsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListConversionEventsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListConversionEventsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListCustomDimensionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListCustomDimensionsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListCustomMetricsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListCustomMetricsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListFirebaseLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListFirebaseLinksResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListIosAppDataStreamsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListIosAppDataStreamsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListPropertiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListPropertiesResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListUserLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListUserLinksResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListWebDataStreamsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListWebDataStreamsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaMeasurementProtocolSecretHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaPropertyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaProperty: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaProvisionAccountTicketResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaProvisionAccountTicketResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaUserLinkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaUserLink: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaWebDataStreamHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaWebDataStream: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
