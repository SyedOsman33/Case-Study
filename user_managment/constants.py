


STATUS_OK = True
STATUS_ERROR = False
RESPONSE_STATUS = "status"
RESPONSE_MESSAGE = "message"
RESPONSE_DATA = "response"
DEFAULT_ERROR_MESSAGE = "There is some issue your request cannot be processed."
ERROR_PARAMS_MISSING_TEXT = "Params are missing, Please check API Doc http://example.org"
SUCCESS = "success"
ERROR = "error"

ERROR_RESPONSE_BODY = {
    RESPONSE_STATUS: 500,
    RESPONSE_MESSAGE: DEFAULT_ERROR_MESSAGE,
}

ERROR_PARAMS_MISSING_BODY = {
    RESPONSE_STATUS: 403,
    RESPONSE_MESSAGE: ERROR_PARAMS_MISSING_TEXT
}
