from grammar.grammar_features.feature_base import FeatureBase


# Sentence defined methods to consume and understand sentence structure in language Elan
# Method are used in parsing tree reduction( in transformer )
class SentenceBase(FeatureBase):
    """
    Words involve in language: []

    action_expr is the top level function in this feature
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def description(self, args):
        func_name = self.name(args)
        if func_name in self.reduction_record.keys():
            return self.reduction_record[func_name]
        else:
            # args[1] is unary function by default
            result = args[1](args[0])
            self.add_record(func_name, result)
            return result

    def action_expr(self, args):
        return args[0]

    def interaction(self, args):
        func_name = self.name(args)
        if func_name in self.reduction_record.keys():
            return self.reduction_record[func_name]
        else:
            # args[1] is binary function by default
            result = args[1](args[0], args[2])
            self.add_record(func_name, result)
            return result

    # pattern is for candle stick only at this moment
    def candle_pattern(self, args):
        func_name = self.name(args)
        if func_name in self.reduction_record.keys():
            return self.reduction_record[func_name]
        else:
            result = args[0](
                self.data_dict["current_open"],
                self.data_dict["current_high"],
                self.data_dict["current_low"],
                self.data_dict["current_close"],
            )
            self.add_record(func_name, result)
            return result

    def spec_pattern(self, args):
        return args[0]
