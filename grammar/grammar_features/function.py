from grammar.grammar_features.feature_base import FeatureBase
from backtesting.customized_indicator import *

# please split keyword, basic and number function latter.
line_function_map = {
    "sma": SMA.from_args,
    "highest": Hightest.from_args,
    "slope": Slope.from_args,
    "rsi": RSI.from_args,
    "macd": MACD.from_args,
    "trailingstop_limit": TrailingStopLimit.from_args,
    "lowest": Lowest.from_args,
    "ema": EMA.from_args,
    "dif": DIF.from_args,
    "dea": DEA.from_args,


}
pattern_line_function_map = {
    "stop_loss": StopLoss.from_args,
    "trailingstop_loss": TrailingStopLoss.from_args,
}


# line feature defined methods to consume and understand lines in language Elan
# Method are used in parsing tree reduction( in transformer )
class BasicFunctionBase(FeatureBase):
    """
    Words involve in language: []

    basic_function are the top level function in this feature
    """

    def __init__(self,  **kwargs):
        super().__init__(**kwargs)

    def basic_function(self, args):
        func_name = self.name(args)
        if func_name in self.reduction_record.keys():
            return self.reduction_record[func_name]
        else:
            result = args[0](*args[1])
            self.add_record(func_name, result)
            return result

    # same as basic_function
    def pattern_function(self, args):
        return self.basic_function(args)

    def sma(self, args):
        return "sma"

    def ema(self, args):
        return "ema"

    def macd(self, args):
        return "macd"

    def rsi(self, args):
        return "rsi"

    def slope(self, args):
        return "slope"

    def highest(self, args):
        return "highest"

    def lowest(self, args):
        return "lowest"

    def trailingstop_limit(self, args):
        return "trailingstop_limit"

    def stop_loss(self, args):
        return "stop_loss"

    def trailingstop_loss(self, args):
        return "trailingstop_loss"

    def line_paras(self, args):
        
        return args[0]

    def line_para_empty(self, args):
        return []

    def pattern_line(self, args):
        return pattern_line_function_map[args[0]]

    def line(self, args):
        return line_function_map[args[0]]

    def parameters(self, args):
        return args

    def parameter(self, args):
        return args[0]

    def string(self, args):
        if args:
            return args[0]

    def none(self, args):
        return None

    def dif(self, args):
        return "dif"

    def dea(self, args):
        return "dea"
