# import time
# from robots.get_resource import get_json_resource
# from robots.robot import *
# from grammar.grammar_rules import elan_grammar
# from lark import Lark
# 
# if __name__ == '__main__':
#     parser = Lark(elan_grammar(), parser='lalr')
#     param_test = [{
#                    "buystrategy": "ema( ema( 3) - ema(14), 7) crossdown ema( 3) - ema(14)",
#                    "sellstrategy": "ema(8) crossover ema(17)",
#                    "fromdate": "2018-1-10",
#                    "todate": "2018-12-30",
#                    "dataname": "MSFT",
#                    "cash": "1000",
#                    "linereturn": "ema( ema( 3) - ema(14), 7);ema( 3) - ema(14);ema( ema( 3) - ema(14), 7) crossdown ema( 3) - ema(14)"
#                 },
#         {
#             "buystrategy": "ema(ema(8),3) crossover ema(17)",
#             "sellstrategy": "ema(ema(ema(8),2),3) crossover ema(17) and slope(ema(8)) neg",
#             "fromdate": "2018-1-10",
#             "todate": "2018-12-30",
#             "dataname": "MSFT",
#             "cash": "1000",
#             "linereturn": "ema(ema(ema(8),2),3);ema(ema(8),3);slope(ema(8));ema(ema(ema(8),2),3) crossover ema(17) and slope(ema(8)) neg;ema(ema(8),3) crossover ema(17)"
#         },
#         {
#             "buystrategy": "sma(volume,3) crossover sma(volume,8)",
#             "sellstrategy": "sma(volume,3) crossover sma(volume,8)",
#             "fromdate": "2018-1-10",
#             "todate": "2018-12-30",
#             "dataname": "MSFT",
#             "cash": "1000",
#             "linereturn": "volume;sma(volume,3);sma(volume,8);sma(volume,3) crossover sma(volume,8)"
#         },
#         {
#             "buystrategy": "ema(volume,3) crossover ema(volume,8)",
#             "sellstrategy": "rsi(volume,3) crossover rsi(volume,8)",
#             "fromdate": "2018-1-10",
#             "todate": "2018-12-30",
#             "dataname": "MSFT",
#             "cash": "1000",
#             "linereturn": "volume;ema(volume,3);ema(volume,8);rsi(volume,3) crossover rsi(volume,8)"
#         },
#         {
#             "buystrategy": "slope(volume) neg ",
#             "sellstrategy": "slope(volume) pos",
#             "fromdate": "2018-1-10",
#             "todate": "2018-12-30",
#             "dataname": "MSFT",
#             "cash": "1000",
#             "linereturn": "volume;slope(volume);slope(volume) neg;slope(volume) pos"
#         },
# 
#     ]
#     robot_test = [AllInfoRobot, AllInfoRobot, AllInfoRobot, AllInfoRobot, AllInfoRobot]
# 
#     for idx, test in enumerate(zip(robot_test, param_test)):
#         start = time.time()
#         result = get_json_resource(test[0], test[1], parser)
#         print("result ", idx, " :", result)
#         end = time.time()
#         print("total time: ", end - start)
# 
#     # start = time.time()
#     # result = get_json_resource(robot_test[7], param_test[7], parser)
#     # print("result : ", result)
#     # end = time.time()
#     # print("total time: ", end - start)