from grammar.grammar_features.feature_base import FeatureBase


class NumberFunctionBase(FeatureBase):
    """
    Words involve in language: []

    number_func is the top level function in this feature
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def number_func(self, args):
        return args[0]

    def number(self, args):
        return args[0]

    def integer(self, args):
        return int(args[0])

    def float(self, args):
        return float(args[0])
