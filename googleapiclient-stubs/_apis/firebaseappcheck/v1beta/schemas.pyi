import typing

import typing_extensions

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaAttestationTokenResponse(
    typing_extensions.TypedDict, total=False
):
    attestationToken: str
    ttl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchGetDeviceCheckConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    configs: typing.List[GoogleFirebaseAppcheckV1betaDeviceCheckConfig]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchGetRecaptchaConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    configs: typing.List[GoogleFirebaseAppcheckV1betaRecaptchaConfig]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchUpdateServicesRequest(
    typing_extensions.TypedDict, total=False
):
    requests: typing.List[GoogleFirebaseAppcheckV1betaUpdateServiceRequest]
    updateMask: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchUpdateServicesResponse(
    typing_extensions.TypedDict, total=False
):
    services: typing.List[GoogleFirebaseAppcheckV1betaService]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaDebugToken(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    token: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaDeviceCheckConfig(
    typing_extensions.TypedDict, total=False
):
    keyId: str
    name: str
    privateKey: str
    privateKeySet: bool

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeCustomTokenRequest(
    typing_extensions.TypedDict, total=False
):
    customToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeDebugTokenRequest(
    typing_extensions.TypedDict, total=False
):
    debugToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeDeviceCheckTokenRequest(
    typing_extensions.TypedDict, total=False
):
    deviceToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeRecaptchaTokenRequest(
    typing_extensions.TypedDict, total=False
):
    recaptchaToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeSafetyNetTokenRequest(
    typing_extensions.TypedDict, total=False
):
    safetyNetToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaListDebugTokensResponse(
    typing_extensions.TypedDict, total=False
):
    debugTokens: typing.List[GoogleFirebaseAppcheckV1betaDebugToken]
    nextPageToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaListServicesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    services: typing.List[GoogleFirebaseAppcheckV1betaService]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaPublicJwk(typing_extensions.TypedDict, total=False):
    alg: str
    e: str
    kid: str
    kty: str
    n: str
    use: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaPublicJwkSet(
    typing_extensions.TypedDict, total=False
):
    keys: typing.List[GoogleFirebaseAppcheckV1betaPublicJwk]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaRecaptchaConfig(
    typing_extensions.TypedDict, total=False
):
    name: str
    siteSecret: str
    siteSecretSet: bool

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaService(typing_extensions.TypedDict, total=False):
    enforcementMode: typing_extensions.Literal["OFF", "UNENFORCED", "ENFORCED"]
    name: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaUpdateServiceRequest(
    typing_extensions.TypedDict, total=False
):
    service: GoogleFirebaseAppcheckV1betaService
    updateMask: str

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...
