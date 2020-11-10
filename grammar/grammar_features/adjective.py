from grammar.grammar_features.feature_base import FeatureBase
from operator import lt, gt

adjective_function_map = {
    "neg": lambda x: lt(x, 0),
    "pos": lambda x: gt(x, 0),
}


# adjective defined methods to consume and understand adjective in language Elan
# Method are used in parsing tree reduction( in transformer )
class AdjectiveBase(FeatureBase):
    """
    Words involve in language: []

    adj is the top level function in this feature
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def adj(self, args):
        return adjective_function_map[args[0]]

    def neg(self, args):
        return "neg"

    def pos(self, args):
        return "pos"
