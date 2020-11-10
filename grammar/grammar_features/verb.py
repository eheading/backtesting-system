from backtrader.indicators import CrossUp, CrossDown, CrossOver
from grammar.grammar_features.feature_base import FeatureBase
from operator import gt, ge, lt, le, eq, ne

verb_function_map = {
    "crossup": CrossUp,
    "crossdown": CrossDown,
    "crossover": CrossOver,
    ">": gt,
    ">=": ge,
    "<": lt,
    "<=": le,
    "==": eq,
    "!=": ne,

}


# verb defined methods to consume and understand verbs in language Elan
# Method are used in parsing tree reduction( in transformer )
class VerbBase(FeatureBase):
    """
    Words involve in language: []

    verb is the top level function in this feature
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def verb(self, args):
        return verb_function_map[args[0]]

    def crossup(self, args):
        return "crossup"

    def crossdown(self, args):
        return "crossdown"

    def greater_than(self, args):
        return ">"

    def greater_or_equal_than(self, args):
        return ">="

    def less_than(self, args):
        return "<"

    def equal(self, args):
        return "=="

    def not_equal(self, args):
        return "!="

    def less_or_equal_than(self, args):
        return "<="

    def crossover(self, args):
        return "crossover"
