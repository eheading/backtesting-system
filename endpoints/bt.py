from flask import Blueprint
from robots.get_resource import get_json_resource
from robots.robot import StatRobot, BatchRunRobot, AllInfoRobot
from grammar.grammar_rules import elan_grammar
from lark import Lark
from flask import request

# endpoint for get back test results
bt_result = Blueprint('bt', __name__)

# provide grammar parser of the language used in strategy that all robots should know
parser = Lark(elan_grammar(), parser='lalr')


# endpoint of details mode
@bt_result.route('/api/v1/resources/bt/allinfo', methods=['GET'])
def get_bt_allinfo():
    backtest_result = get_json_resource(AllInfoRobot, dict(request.args), parser)
    return backtest_result

# endpoint of simple mode
@bt_result.route('/api/v1/resources/bt/stat', methods=['GET'])
def get_bt_stat():
    backtest_result = get_json_resource(StatRobot, dict(request.args), parser)
    return backtest_result

# endpoint of batch mode
@bt_result.route('/api/v1/resources/bt/batch', methods=['GET'])
def get_bt_batchrun():
    backtest_result = get_json_resource(BatchRunRobot, dict(request.args), parser)
    return backtest_result

