# import time
# from robots.get_resource import get_json_resource
# from robots.robot import *
# from grammar.grammar_rules import elan_grammar
# from lark import Lark
#
# if __name__ == '__main__':
#     parser = Lark(elan_grammar(), parser='lalr')
#     param_test = [{
#                    "buystrategy": "dif(2,14) pos",
#                    "sellstrategy": "dif(2,14) neg",
#                    "fromdate": "2018-1-10",
#                    "todate": "2018-12-30",
#                    "dataname": "MSFT",
#                    "cash": "1000",
#                    "linereturn": "dif(2,14)"
#                 },
#         {
#             "buystrategy": "ema(dif(2,14),9) pos",
#             "sellstrategy": "ema(dif(2,14),9) neg",
#             "fromdate": "2018-1-10",
#             "todate": "2018-12-30",
#             "dataname": "MSFT",
#             "cash": "1000",
#             "linereturn": "ema(dif(2,14),9)"
#         },
#         {
#             "buystrategy": "dea(2,9,14) pos",
#             "sellstrategy": "dea(2,9,14) neg",
#             "fromdate": "2018-1-10",
#             "todate": "2018-12-30",
#             "dataname": "MSFT",
#             "cash": "1000",
#             "linereturn": "dea(2,9,14)"
#         },
#
#     ]
#     robot_test = [AllInfoRobot, AllInfoRobot, AllInfoRobot]
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