from grammar.grammar_features.feature_base import FeatureBase
from backtesting.customized_indicator import CurrentBuy

# we will add data record to this on initialization function
# which includes:
# data_dict = {
#             "current_close": self.datas[0].close,
#             "current_open": self.datas[0].open,
#             "current_high": self.datas[0].high,
#             "current_low": self.datas[0].low,
#             "current_low": self.datas[0].volume,
#         }
keyword_function_map = {
    "buy_price": CurrentBuy.from_args,
}


class KeywordFunctionBase(FeatureBase):
    """
    Words involve in language: []

    keyword_func is the top level function in this feature
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # integrate data_dict inherit from feature base into keyword_function
        # data dict provide data from directly from yahoo api
        # keywords(e.g price, volume...) highly depend on data dict thus we want to combine them first
        global keyword_function_map
        keyword_function_map = {**keyword_function_map, **self.data_dict}

    def keyword_func(self, args):
        func_name = self.name(args)
        if func_name in self.reduction_record.keys():
            return self.reduction_record[func_name]
        else:
            result = args[0]()
            self.add_record(func_name, result)
            return result

    def keywords(self, args):
        return keyword_function_map[args[0]]

    def buy_price(self, args):
        return "buy_price"

    def current_price(self, args):
        return "current_close"

    def current_volume(self, args):
        return "current_volume"
