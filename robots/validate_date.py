import requests
import json
from exeception import StartDateValueException, EndDateValueException, InvalidDateFormatException, \
    AccessExternalDataException
from utils import unixtime_to_str, str_to_unixtime, formalstr_to_unixtime, date_formalized


def startend_timereader(ticker):
    get_url = "https://query1.finance.yahoo.com/v8/finance/chart/{}?interval=1d".format(ticker)
    json_res = json.loads(requests.get(get_url).content)
    start = json_res['chart']['result'][0]["meta"]['firstTradeDate']
    end = json_res['chart']['result'][0]["meta"]['regularMarketTime']
    return start, end


# check if date inputs are valid or not
# param: <string> start_in: input start date string
# param: <string> end_in: input end date string
# ticker: <string> ticker: ticker of the stock
def declare_inputdate_valid(start_in, end_in, ticker):
    # input format check for input start time
    start_time = date_formalized(start_in)
    if start_time is None:
        raise InvalidDateFormatException(
            details="Incorrect fromdate format:{}. It should be %Year-%month-%day.(e.g 2019-3-14)".format(start_in))

    # input format check for input end time
    end_time = date_formalized(end_in)
    if end_time is None:
        raise InvalidDateFormatException(
            details="Incorrect todate format:{}. It should be %Year-%month-%day.(e.g 2020-3-14)".format(end_in))

    start_time = formalstr_to_unixtime(start_time)
    if start_time is None:
        raise StartDateValueException(
            details="Invalid fromdate:{}. Date is valid only after 1 January 1970.".format(end_in))

    end_time = formalstr_to_unixtime(end_time)
    if end_time is None:
        raise EndDateValueException(
            details="Invalid todate:{}. Date is valid only after 1 January 1970.".format(end_in))
    try:
        start_bound, end_bound = startend_timereader(ticker)
    except:
        raise AccessExternalDataException(details="Connection error: Unable to get time period info from YahooFinanceAPI")

    # check user input time is within official range(from yahoo) or not
    if start_time < start_bound:
        local_time = unixtime_to_str(start_bound)
        raise StartDateValueException(details="fromdate should be after:{}".format(local_time))

    if end_bound < end_time:
        local_time = unixtime_to_str(end_bound)
        raise StartDateValueException(details="todate should be before:{}".format(local_time))

    if start_time > end_time:
        raise StartDateValueException(details="todate:{} earlier than fromdate:{}".format(end_in, start_in))