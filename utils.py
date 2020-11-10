import datetime
import numpy as np
from backtrader.utils import AutoOrderedDict, num2date


#  return new dictionary only with selected keys
# :param: <dict> old_dict: old dictionary
# :param: <list of string>: selected keys
# :return: <dict> new_dict: new dictionary with selected keys
def dict_filter(old_dict, mykeys):
    new_dict = AutoOrderedDict({your_key: old_dict[your_key] for your_key in mykeys})
    return new_dict


#  input date string and check whether it is valid. If valid, return the formal form\
#  {YYYY-MM-DD}. If input date string is invalid, return None.
# :param: <string> date_string: date
# :return: <datetime>
def date_formalized(date_string):
    try:
        formal_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return formal_date
    except:
        print("Error: incorrect date string format {}. It should be YYYY-MM-DD".format(date_string))
        return None


#  input date string and return its unix time
# :param: <string> date_string: date
# :return: <float>  unix_time
def str_to_unixtime(date_string):
    try:
        date = date_formalized(date_string)
        unix_time = date.timestamp()
        return unix_time
    except:
        return None


def formalstr_to_unixtime(date_string):
    try:
        unix_time = date_string.timestamp()
        return unix_time
    except:
        return None


def unixtime_to_str(unix_time):
    try:
        return datetime.datetime.fromtimestamp(unix_time).strftime("%Y-%m-%d")
    except:
        return None


#  convert nan to 0 in array a
# :param: <numpy array> a: an array with nan value
# :return: <numpy array>: an array with all nan-value replaced
def nan2_zero(a):
    return np.where(np.isnan(a), 0, a)


#  convert date in bt number to string
# :param: <float> date: a float number representing date in backtrader
# :return: <string>: a string of day in  "YYYY-mm-dd" form
def numdate2str(date):
    return num2date(date).strftime("%Y-%m-%d")


# Special json encoder for numpy types
def default(obj):
    if isinstance(obj, np.ndarray):
        return obj.tolist()


# decorator for function log: print function name and its argument
def log(func):
    def wrap_func(*args, **kwarg):
        print(func.__name__, ": ", args, kwarg)
        return func
    return wrap_func
