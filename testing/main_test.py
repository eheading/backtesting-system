# import time
# from robots.get_resource import get_json_resource
# from robots.robot import *
# from grammar.grammar_rules import elan_grammar
# from lark import Lark
# if __name__ == '__main__':
#     parser = Lark(elan_grammar(), parser='lalr')
#     param_test = [{
#                    "buystrategy": "sma(8) crossover sma(17)",
#                    "sellstrategy": "sma(8) crossover sma(17)",
#                    "fromdate": "2018-1-10",
#                    "todate": "2018-12-30",
#                    "dataname": "MSFT",
#                    "cash": "1000",
#                    "linereturn": "sma(8);sma(17);sma(8) crossover sma(17)"
#                 },
#                {
#                    "buystrategy": "sma(8) crossdown sma(17)",
#                    "sellstrategy": "sma(8) crossup sma(17)",
#                    "fromdate": "2018-1-10",
#                    "todate": "2018-12-30",
#                    "dataname": "AAPL",
#                    "cash": "1000",
#                    "linereturn": "sma(8);sma(17);sma(8) crossup sma(17);sma(8) crossdown sma(17)"
#                },
#                {
#                    "buystrategy": "sma(8) crossdown sma(17)",
#                    "sellstrategy": "sma(8) crossup sma(17)",
#                    "fromdate": "2018-1-1",
#                    "todate": "2020-3-2",
#                    "dataname": "MSFT",
#                    "cash": "1000",
#                    "linereturn": "sma(8);sma(17);sma(8) crossup sma(17);sma(8) crossdown sma(17)"
#                },
#                {
#                    "buystrategy": "sma(8) crossdown sma(17)",
#                    "sellstrategy": "sma(8) crossup sma(17)",
#                    "fromdate": "2018-1-10",
#                    "todate": "2018-12-30",
#                    "dataname": "AAPL",
#                    "cash": "1000",
#                    "linereturn": "sma(8);sma(17);sma(8) crossup sma(17);sma(8) crossdown sma(17)"
#                },
#                {
#                    "buystrategy": "sma(8) crossdown sma(17)",
#                    "sellstrategy": "sma(8) crossup sma(17)",
#                    "fromdate": "2018-1-1",
#                    "todate": "2020-3-2",
#                    "dataname": "MSFT",
#                    "cash": "1000",
#                    "linereturn": "sma(8);sma(17);sma(8) crossup sma(17);sma(8) crossdown sma(17)"
#                },
#                {
#                    "buystrategy": "sma(8) crossdown sma(17) and slope(sma(8)) neg",
#                    "sellstrategy": "sma(8) crossup sma(17)",
#                    "fromdate": "2018-1-10",
#                    "todate": "2018-12-30",
#                    "dataname": "MSFT",
#                    "timeframe": "day",
#                    "cash": "1000",
#                    "linereturn": "sma(8);sma(17);sma(8) crossup sma(17);sma(8) crossdown sma(17);slope(sma(8));sma(8) crossdown sma(17) and slope(sma(8)) neg"
#                },
#                {
#                    "buystrategy": "sma(8) crossdown sma(17)",
#                    "sellstrategy": "sma(8) crossup sma(17)",
#                    "fromdate": "2016-1-10",
#                    "todate": "2017-12-30",
#                    "dataname": "MSFT",
#                    "timeframe": "week",
#                    "cash": "1000",
#                    "linereturn": "sma(8);sma(17);sma(8) crossup sma(17);sma(8) crossdown sma(17)"
#                },
#                {
#                    "buystrategy": "candle hammer",
#                    "sellstrategy": "sma(8) crossdown sma(17)",
#                    "fromdate": "2010-5-23",
#                    "todate": "2011-5-3",
#                    "dataname": "MSFT",
#                    "cash": "1000",
#                    "linereturn": "sma(8);sma(17);sma(8) crossdown sma(17);candle hammer"
#                },
#                {
#                    "buystrategy": "sma(8) crossdown sma(17)",
#                    "sellstrategy": "sma(8) crossup sma(17)",
#                    "fromdate": "2018-1-10",
#                    "todate": "2018-12-30",
#                    "dataname": "MSFT",
#                    "linereturn": "sma(8);sma(17);sma(8) crossup sma(17);sma(8) crossdown sma(17)",
#                },
#                {
#                    "buystrategy": "sma(8) crossdown sma(17)",
#                    "sellstrategy": "sma(8) crossup sma(17)",
#                    "fromdate": "2018-1-1",
#                    "todate": "2020-3-2",
#                    "dataname": "MSFT",
#                    "linereturn": "sma(8);sma(17);sma(8) crossup sma(17);sma(8) crossdown sma(17)",
#                },
#                {
#                    "buystrategy": "sma(7) crossup sma(14)",
#                    "sellstrategy": "sma(7) crossdown sma(14)",
#                    "fromdate": "2019-5-3",
#                    "todate": "2020-5-3",
#                    "dataname": "STM;FB;T;ADBE;DELL;AAPL;AMZN;ZEUS",
#                },
#                {
#                    "buystrategy": "sma(8) crossdown sma(17)",
#                    "sellstrategy": "sma(8) crossup sma(17)",
#                    "fromdate": "2018-1-10",
#                    "todate": "2018-12-30",
#                    "dataname": "MSFT",
#                    "cash": "1000",
#                    "linereturn": "sma(8);sma(17);sma(8) crossup sma(17);sma(8) crossdown sma(17)"
#                },
#                {
#                    "buystrategy": "sma(8) crossdown sma(17)",
#                    "sellstrategy": "trailingstop_loss(0.06)",
#                    "fromdate": "2018-1-10",
#                    "todate": "2018-12-30",
#                    "dataname": "MSFT",
#                    "cash": "1000",
#                    "linereturn": "sma(8);sma(17);sma(8) crossdown sma(17);trailingstop_loss(0.06)"
#                },
#                {
#                    "buystrategy": "trailingstop_limit(0.05) > cur_price",
#                    "sellstrategy": "sma(8) crossup sma(17)",
#                    "fromdate": "2018-1-10",
#                    "todate": "2018-12-30",
#                    "dataname": "MSFT",
#                    "cash": "1000",
#                    "linereturn": "sma(8);sma(17);sma(8) crossup sma(17);trailingstop_limit(0.05);cur_price;trailingstop_limit(0.05) > cur_price"
#                },
#                {
#                    "buystrategy": "sma(8) crossdown sma(17)",
#                    "sellstrategy": "stop_loss(0.05)",
#                    "fromdate": "2018-1-10",
#                    "todate": "2018-12-30",
#                    "dataname": "MSFT",
#                    "cash": "1000",
#                    "linereturn": "sma(8);sma(17);sma(8) crossdown sma(17);stop_loss(0.05) "
#                },
#         {
#             "buystrategy": "sma(8) > sma(17) ",
#             "sellstrategy": "sma(8) < sma(17) ",
#             "fromdate": "2018-1-10",
#             "todate": "2018-12-30",
#             "dataname": "MSFT",
#             "cash": "1000",
#             "linereturn": "sma(8) > sma(17);sma(8) < sma(17)"
#         },
#         {
#             "buystrategy": "sma(8) > sma(17) and slope(sma(8)) neg",
#             "sellstrategy": "sma(8) < sma(17) or sma(8)==sma(17)",
#             "fromdate": "2018-1-10",
#             "todate": "2018-12-30",
#             "dataname": "MSFT",
#             "cash": "1000",
#             "linereturn": "sma(8) > sma(17);sma(8) < sma(17);slope(sma(8)) neg;sma(8)==sma(17);sma(8) > sma(17) and slope(sma(8)) neg;sma(8) < sma(17) or sma(8)==sma(17)"
#         },
#         {
#             "buystrategy": "sma(8) > sma(17) and slope(sma(8)) neg or sma(8)!=sma(17) and slope(sma(8)) pos",
#             "sellstrategy": "sma(8) < sma(17) ",
#             "fromdate": "2018-1-10",
#             "todate": "2018-12-30",
#             "dataname": "MSFT",
#             "cash": "1000",
#             "linereturn": "sma(8) > sma(17) and slope(sma(8)) neg; sma(8)!=sma(17) and slope(sma(8)) pos;sma(8) > sma(17) and slope(sma(8)) neg or sma(8)!=sma(17) and slope(sma(8)) pos;slope(sma(8)) neg or sma(8)!=sma(17)"
#         },
#         {
#             "buystrategy": "sma(8) > sma(17) or sma(8) == sma(17)",
#             "sellstrategy": "sma(8) != sma(17) and slope(sma(8)) neg or stop_loss(0.001)",
#             "fromdate": "2018-1-10",
#             "todate": "2018-12-30",
#             "dataname": "MSFT",
#             "cash": "1000",
#             "linereturn": "sma(8);sma(17);sma(8)>sma(17);sma(8)==sma(17);sma(8)!=sma(17);slope(sma(8)) neg;slope(sma(8));stop_loss(0.001);sma(8)!=sma(17) and slope(sma(8)) neg or stop_loss(0.001);sma(8) > sma(17) or sma(8) == sma(17);sma(8) != sma(17) and slope(sma(8)) neg"
#         }
#     ]
#     robot_test = [AllInfoRobot, AllInfoRobot, AllInfoRobot, AllInfoRobot, AllInfoRobot,
#                   AllInfoRobot, AllInfoRobot, AllInfoRobot, StatRobot, StatRobot,
#                   BatchRunRobot, AllInfoRobot, AllInfoRobot, AllInfoRobot, AllInfoRobot,
#                   AllInfoRobot, AllInfoRobot, AllInfoRobot, AllInfoRobot]
#     for idx, test in enumerate(zip(robot_test, param_test)):
#         start = time.time()
#         result = get_json_resource(test[0], test[1], parser)
#         print(idx, " result : ", result)
#         end = time.time()
#         print("total time: ", end - start)