class GeneralException(Exception):

    def __init__(self, message=None, details=None):

        super().__init__()
        self.message = message
        self.details = details
        self.status_code = "400"

    def to_dict(self):
        rv = dict()
        rv['message'] = self.message
        rv['error'] = self.status_code
        rv['details'] = self.details
        return rv


# error code: 400 series , user input errors
class StartDateValueException(GeneralException):
    def __init__(self, message="Invalid Field Value: fromdate", details=None):
        super().__init__(message, details)
        self.status_code = "400-200"


class EndDateValueException(GeneralException):
    def __init__(self, message="Invalid Field Value: todate", details=None):
        super().__init__(message, details)
        self.status_code = "400-201"


class InvalidDateFormatException(GeneralException):
    def __init__(self, message="Invalid Date Format",
                 details="Invalid date format and shouldn't input date before 1/1/1970"):
        super().__init__(message, details)
        self.status_code = "400-202"


# error code: 500 series , internal errors
class AccessExternalDataException(GeneralException):
    def __init__(self, message="Access External Data Error",
                 details="Access External Data Error"):
        super().__init__(message, details)
        self.status_code = "500-200"
