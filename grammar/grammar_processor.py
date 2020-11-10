from lark import Transformer
from backtrader import AutoOrderedDict
from grammar.grammar_features.adjective import AdjectiveBase
from grammar.grammar_features.arithmetic import ArithmeticFeatureBase
from grammar.grammar_features.candlestick import CandleFeatureBase
from grammar.grammar_features.function import BasicFunctionBase
from grammar.grammar_features.keyword import KeywordFunctionBase
from grammar.grammar_features.logic import LogicFeatureBase
from grammar.grammar_features.number import NumberFunctionBase
from grammar.grammar_features.sentence import SentenceBase
from grammar.grammar_features.verb import VerbBase
from backtesting.customized_indicator import DynamicInd


# ElanTransoformer get all features from the base so that he know how to evaluate parsing tree
# build by the parser
class ElanTransformer(CandleFeatureBase, LogicFeatureBase, ArithmeticFeatureBase,
                      VerbBase, AdjectiveBase, NumberFunctionBase,
                      KeywordFunctionBase, BasicFunctionBase, SentenceBase,
                      Transformer):

    def __init__(self, data_record, reduction_record):
        super().__init__(data_record=data_record, reduction_record=reduction_record)
        # add data_record to function dictionary


# ElanProcessor has a parser(parse users strategy ) and transformer(eval strategy)
class ElanProcessor:
    def __init__(self, data_feed, parser):
        self.data_dict = data_feed
        self.parser = parser
        self.reduction_record = AutoOrderedDict()
        self.transformer = ElanTransformer(self.data_dict, self.reduction_record)

    def parse_query(self, query):
        # parse the input strategy and evaluate it by transformer .Then return the result.
        parse_tree = self.parser.parse(query)
        transform = self.transformer.transform(parse_tree)
        self.reduction_record.update(self.transformer.reduction_record)
        return transform.children[0]

    def get_parse_result(self, query, parser, transformer):
        try:
            ptree = parser.parse(query)
            transform = transformer.transform(ptree)
            self.reduction_record.update(self.transformer.reduction_record)
            return transform.children[0]
        except:
            return None

    def get_reduction_record(self):
        return self.reduction_record

    #  get a list a dynamic line object( the line can only be evaluated during runtime)
    # :return: <DynamicInd list>
    def get_dynamic_lines(self):
        return [obj for obj in self.get_reduction_record().values() if isinstance(obj, DynamicInd)]


# ElanProcessor with extra ability of returning line request by user
class ElanLineReturnProcessor(ElanProcessor):

    def __init__(self, data_feed, parser):
        super().__init__(data_feed, parser)
        self.linereturn_transformer = LineReturnElanTransformer(self.data_dict, self.get_reduction_record())

    #  user provide a namelist of line objects and the corresponding
    #  line objects are return in a list
    # :param: <string list> query_list : namelist of line objects user is\
    #  interested in e.g ["sma(4)","sma(3) > 100"]
    # :return: <dict> result_dict: dictionary which key is line_name and\
    #  value is the corresponding line object
    def get_request_lines(self, query_list):
        result_dict = {}
        match_transformer = self.linereturn_transformer

        # We are use existing line objects in reduction record to rebuild
        # line objects mentioned by user.
        #
        # Assumption: all line object exist in query_list must exist in
        # buystrategy or sellstrategy.
        #
        # By this way, we can easily overcome duplication problem caused by name
        # alias at the same time return correct line objects mentioned by user.
        for qline in query_list:
            lines = self.get_parse_result(qline, self.parser, match_transformer)

            # only return line object of line_name that parser can understand
            if lines is not None:
                result_dict[qline] = lines

        return result_dict


# Specialized transformer are forced to use line object created in reduction record\
# to locate the object mentioned by user
class LineReturnElanTransformer(ElanTransformer):

    def __init__(self, data_record, reduction_record):
        super().__init__(data_record, reduction_record)

    # common: all methods below override method in parents
    # common behavior: throw exception with invalid items in "linereturn"
    # common exception: when user is mentioning object not in reduction record

    def basic_function(self, args):
        # self.log(self.basic_function, args, info="NoEval ")
        func_name = self.name(args)
        if func_name in self.reduction_record.keys():
            return self.reduction_record[func_name]
        else:
            raise Exception("Invalid input: ", args)

    def description(self, args):
        # self.log(self.description, args, info="NoEval ")
        func_name = self.name(args)
        if func_name in self.reduction_record.keys():
            return self.reduction_record[func_name]
        else:
            raise Exception("Invalid input: ", args)

    def interaction(self, args):
        # self.log(self.interaction, args, info="NoEval ")
        func_name = self.name(args)
        if func_name in self.reduction_record.keys():
            return self.reduction_record[func_name]
        else:
            raise Exception("Invalid input: ", args)

    def or_expr(self, args):

        func_name = self.name(args)
        if func_name in self.reduction_record.keys():
            return self.reduction_record[func_name]
        else:
            raise Exception("Invalid input: ", args)

    def and_expr(self, args):
        # self.log(self.and_expr, args, info="NoEval ")
        func_name = self.name(args)
        if func_name in self.reduction_record.keys():
            return self.reduction_record[func_name]
        else:
            raise Exception("Invalid input: ", args)

    def keyword_func(self, args):
        # self.log(self.keyword_func, args, info="NoEval ")
        func_name = self.name(args)
        if func_name in self.reduction_record.keys():
            return self.reduction_record[func_name]
        else:
            raise Exception("Invalid input: ", args)

    def arith_expr(self, args):
        # self.log(self.arith_expr, args, info="NoEval ")
        func_name = self.name(args)
        if func_name in self.reduction_record.keys():
            return self.reduction_record[func_name]
        else:
            raise Exception("Invalid input: ", args)

    def pattern(self, args):
        # self.log(self.pattern, args)
        func_name = self.name(args)
        if func_name in self.reduction_record.keys():
            return self.reduction_record[func_name]
        else:
            raise Exception("Invalid input: ", args)