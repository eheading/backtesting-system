from grammar.grammar_features.feature_base import FeatureBase
from backtrader.functions import Or, And
from utils import log

logic_function_map = {
    "or": Or,
    "and": And,
}


# Logic feature defined methods to consume and understand logic in language Elan
# Method are used in parsing tree reduction( in transformer )
# Logic are mainly two types: and , or
class LogicFeatureBase(FeatureBase):
    """
    Words involve in language:[]

    or_expr is the top level function in this feature
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # All methods for transformers
    def logical_expr(self, args):
        return args[0]

    def logic_factor(self, args):
        return args[0]


    def or_expr(self, args):

        func_name = self.name(args)

        if func_name in self.reduction_record.keys():
            return self.reduction_record[func_name]
        else:
            # [A,or,B,or,C]
            # only take the odd number term as argument
            para_args = args[0::2]
            result = logic_function_map["or"](*para_args)
            self.add_record(func_name, result)
            return result

    def and_expr(self, args):
        func_name = self.name(args)
        if func_name in self.reduction_record.keys():
            return self.reduction_record[func_name]
        else:
            # [A,and,B,and,C]
            # only take the odd number term as argument
            para_args = args[0::2]
            result = logic_function_map["and"](*para_args)
            self.add_record(func_name, result)
            return result

    def or_(self, args):
        return "or"

    def and_(self, args):
        return "and"
