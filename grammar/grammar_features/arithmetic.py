from functools import reduce
from grammar.grammar_features.feature_base import FeatureBase
from operator import add, sub, mul, truediv, neg, pos, pow

arithmetic_function_map = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": truediv,
    "-ve": neg,
    "+ve": pos,
    "**": pow,
}


# Arithmetic feature defined methods to consume and understand arithmetic in language Elan
# Method are used in parsing tree reduction( in transformer )
class ArithmeticFeatureBase(FeatureBase):
    """
    Words involve in language:[arith_expr, arith_term, arith_factor,
    arith_atom, factor_op, _add_op, _mul_op, positive, negative,
    factor_op_recursive, factor_power_recursive]

    arith_expr is the top level function in this feature
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _add_op(self, args):
        return args[0]

    def _mul_op(self, args):
        return args[0]

    def factor_power_recursive(self, args):
        func_name = self.name(args)
        if func_name in self.reduction_record.keys():
            return self.reduction_record[func_name]
        else:
            length = len(args)
            if length == 2:
                result = arithmetic_function_map["**"](args[0], args[1])
                self.add_record(func_name, result)
                return result
            elif length == 1:
                result = args[0]
                self.add_record(func_name, result)
                return result

    def arith_term(self, args):
        func_name = self.name(args)
        if func_name in self.reduction_record.keys():
            return self.reduction_record[func_name]
        else:
            op_args = args[1::2]
            para_args = args[0::2]
            op_args = iter(op_args)
            result = reduce(lambda x, y: arithmetic_function_map[next(op_args)](x, y), para_args)
            self.add_record(func_name, result)
            return result

    def arith_expr(self, args):
        func_name = self.name(args)
        if func_name in self.reduction_record.keys():
            return self.reduction_record[func_name]
        else:
            op_args = args[1::2]
            para_args = args[0::2]
            op_args = iter(op_args)
            result = reduce(lambda x, y: arithmetic_function_map[next(op_args)](x, y), para_args)
            self.add_record(func_name, result)
            return result

    def factor_op_recursive(self, args):
        func_name = self.name(args)
        if func_name in self.reduction_record.keys():
            return self.reduction_record[func_name]
        else:
            result = arithmetic_function_map[args[0]](args[1])
            self.add_record(func_name, result)
            return result

    def arith_atom(self, args):
        return args[0]

    def positive(self, args):
        return "+ve"

    def negative(self, args):
        return "-ve"
