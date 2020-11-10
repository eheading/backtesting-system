from utils import default
import json


# highest level robot action to grab all resource needed
# 1. receive grammar parser so that robot can understand the language used to describe strategies
# 2. get order regarding to strategy
# 3. run strategy and get back the result
def get_resources(robot_type, order, parser):
    robot = robot_type(parser)
    robot.accept_order(**order)
    robot.run_strategy()
    backtest_result = robot.get_backtest_result()
    return backtest_result


def get_json_resource(robot_type, order, parser):
    return json.dumps(get_resources(robot_type, order, parser), default=default)
