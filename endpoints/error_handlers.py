from flask import Blueprint
from flask import jsonify
from exeception import *

error = Blueprint('error', __name__)


@error.app_errorhandler(StartDateValueException)
def value_error_start_date(e):
    return jsonify(e.to_dict())


@error.app_errorhandler(EndDateValueException)
def value_error_end_date(e):
    return jsonify(e.to_dict())


@error.app_errorhandler(InvalidDateFormatException)
def invalid_date_format(e):
    return jsonify(e.to_dict())

@error.app_errorhandler(AccessExternalDataException)
def yahoo_getdata_error(e):
    return jsonify(e.to_dict())