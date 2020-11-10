from backtesting import run_strategy
from exeception import AccessExternalDataException
from robots.get_resource import get_resources
from backtesting.trade_stat import TradeStat
from robots.validate_date import declare_inputdate_valid
from utils import date_formalized, AutoOrderedDict, dict_filter, numdate2str, unixtime_to_str
import yfinance as yf
import backtrader as bt
# import concurrent.futures

# Robot is a client that can 0.know grammar of strategy order
#                            1.accept orders
#                            2.feed data to appropriate places and
#                            3.grasp all data you need in collection

# valid choice [1d, 5d, 1wk, 1mo, 3mo]
timeframe_map = {
            "day": "1d",
            "week": "1wk",
            "month": "1mo",
        }

default_param = {
    "buystrategy": None,
    "sellstrategy": None,
    "fromdate": None,
    "todate": None,
    "dataname": None,
    "linereturn": None,
    "datamode": bt.feeds.PandasData,
    "timeframe": "day",
    "cash": 10000000000,
    "commission": 0,

}


class MetaRobot:
    """
    all robots can accept an order and output a backtest result
    """
    def __init__(self, parser):
        self.parser = parser
        self.collection = AutoOrderedDict()
        self.order_dict = None
        self.run_result = None

    # prepare data to tell cerebro what to do
    def accept_order(self, order_dict):
        pass
    
    def get_order(self):
        return self.order_dict

    def get_collection(self):
        return self.collection

    def run_strategy(self):
        pass


class YahooDataRobot(MetaRobot):
    def __init__(self, parser):
        super(YahooDataRobot, self).__init__(parser)

    # get data from yahoo
    def get_yahoo_data(self):

        param_dict = AutoOrderedDict(
            start=date_formalized(self.order_dict["fromdate"]),
            end=date_formalized(self.order_dict["todate"]),
            tickers=self.order_dict["dataname"],
            interval=timeframe_map[self.order_dict["timeframe"]],
            treads=True,
        )
        try:
            yahoo_data = yf.download(**param_dict).dropna()
        except:
            raise AccessExternalDataException(details="Connection error: Unable to get stock info(open,close,etc) from YahooFinanceAPI")
        return yahoo_data


# general robot provide all detrails of result and all line object you need
# detrails + complicated result
class GeneralRobot(YahooDataRobot):

    def __init__(self, parser):
        super(GeneralRobot, self).__init__(parser)
        self.order_dict = dict_filter(default_param, ["datamode", "timeframe", "cash", "commission", "linereturn"])

    def accept_order(self, **kwargs):
        self.order_dict.update(kwargs)
        declare_inputdate_valid(self.order_dict["fromdate"], self.order_dict["todate"], self.order_dict["dataname"])
        # preare datafedd for run_strategy
        self.yahoo_data = self.get_yahoo_data()
        # split lines in linereturn
        if self.order_dict["linereturn"] is not None:
            self.order_dict["linereturn"] = self.order_dict["linereturn"].split(";")

        self.collection.datafeed = AutoOrderedDict(
                datamode=bt.feeds.PandasData,
                datafeed_dict=AutoOrderedDict(
                    dataname=self.yahoo_data,
                ),
                strategy_dict=AutoOrderedDict(
                    buystrategy=self.order_dict["buystrategy"],
                    sellstrategy=self.order_dict["sellstrategy"],
                    robot=self,
                    sell_all_date=self.yahoo_data.index[-2].strftime("%Y-%m-%d"),
                    linereturn=self.order_dict["linereturn"]
                ),
                commission=float(self.order_dict["commission"]),
                # default infinity large number
                cash=float(self.order_dict["cash"])
            )

    def update_collection_fromstrategy(self, strategy):
        ta = TradeStat(strategy.record.get_record("sell"))

        self.collection.backtesting_result.tradestat = ta.get_sumpnlcomm()
        self.collection.backtesting_result.linerecord = {k: v.get(size=len(v)).tolist() for k, v in
                                                         strategy.interested_obj.items()}
        self.collection.backtesting_result.tradestat = ta.get_allinfo_dict()
        self.collection.backtesting_result.cash = strategy.stats.broker.cash.get(
            size=len(strategy.stats.broker.value)).tolist()
        self.collection.backtesting_result.value = strategy.stats.broker.value.get(
            size=len(strategy.stats.broker.value)).tolist()
        self.collection.backtesting_result.date = list(
            map(lambda x: numdate2str(x), strategy.datadate.get(size=len(strategy.stats.broker.value)).tolist()))

    def run_strategy(self):
        try:
            run_strategy.runstrat(self)
            self.run_result = self.collection.backtesting_result
        except:
            self.run_result = {}

    def get_backtest_result(self):
        return self.run_result


# stat robot provide brief info of statistical result of performance
# simple + short + general view
class StatRobot(GeneralRobot):

    def __init__(self, parser):
        super(StatRobot, self).__init__(parser)

    def update_collection_fromstrategy(self, strategy):
        ta = TradeStat(strategy.record.get_record("sell"))
        self.collection.backtesting_result.tradestat = ta.get_simple_stat()


# pnlrobot provide only pnlfinal result
class PnlRobot(GeneralRobot):

    def __init__(self, parser):
        super(PnlRobot, self).__init__(parser)

    def update_collection_fromstrategy(self, strategy):
        ta = TradeStat(strategy.record.get_record("sell"))
        self.collection.backtesting_result.pnlfinal = ta.pnlfinal()


class BatchRunRobot(MetaRobot):

    def __init__(self, parser):
        super(BatchRunRobot, self).__init__(parser)
        self.dataname_list = None

    # BatchRun Robot call pnl robot to evaluate the pnlfinal
    # for comparision between tickers
    def eval_strategy(self, batch_dataname):
        batch_result = get_resources(PnlRobot, self.batch_order(batch_dataname), self.parser)
        return batch_result.pnlfinal

    def accept_order(self, **kwargs):
        self.dataname_list = kwargs["dataname"].split(';')
        self.order_dict = kwargs

    def batch_order(self, batch_dataname):
        # modify original dataname to the specific ticker and keep other order info unchanged
        batch_order = self.order_dict
        batch_order["dataname"] = batch_dataname
        return batch_order

    def run_strategy(self):
        # do batch run for all ticker names in dataname_list
        # sort them and output as json

        #with concurrent.futures.ThreadPoolExecutor() as executor:
        #    pnl_reuslt = list(executor.map(self.eval_strategy, self.dataname_list))
        try:
            pnl_reuslt = list(map(self.eval_strategy, self.dataname_list))
            sort_result = sorted(zip(pnl_reuslt, self.dataname_list), reverse=True)
            dict_result = {result[1]: result[0] for result in sort_result}
            self.run_result = dict_result
        except:
            self.run_result = {}

    def get_backtest_result(self):
        return self.run_result


class AllInfoRobot(GeneralRobot):

    def update_collection_frompandasdf(self):
        try:
            self.collection.backtesting_result.volume = self.yahoo_data["Volume"].tolist()
            self.collection.backtesting_result.open = self.yahoo_data["Open"].tolist()
            self.collection.backtesting_result.close = self.yahoo_data["Close"].tolist()
            self.collection.backtesting_result.high = self.yahoo_data["High"].tolist()
            self.collection.backtesting_result.low = self.yahoo_data["Low"].tolist()

        except:
            self.collection.backtesting_result.volume = []
            self.collection.backtesting_result.open = []
            self.collection.backtesting_result.close = []
            self.collection.backtesting_result.high = []
            self.collection.backtesting_result.low = []

    def accept_order(self, **kwargs):
        GeneralRobot.accept_order(self, **kwargs)
        self.update_collection_frompandasdf()