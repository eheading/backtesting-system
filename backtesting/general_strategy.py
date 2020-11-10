from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from backtesting.history_recorder import HistoryRecorder
from grammar.grammar_processor import ElanLineReturnProcessor
import backtrader as bt
from utils import numdate2str


class GeneralStrategy(bt.Strategy):
    params = dict(
        buystrategy="",
        sellstrategy="",
        linereturn=None,
        robot=None,
        sell_all_date=None
    )

    def __init__(self):
        self.robot = self.p.robot
        self.dataclose = self.datas[0].close
        self.datadate = self.datas[0].datetime
        data_record = {
            "current_close": self.datas[0].close,
            "current_open": self.datas[0].open,
            "current_high": self.datas[0].high,
            "current_low": self.datas[0].low,
            "current_volume": self.datas[0].volume,
        }

        # add data record to function dictionary
        self.Elan = ElanLineReturnProcessor(data_record, self.robot.parser)
        # initialization base on buy strategy and sell strategy

        self.ind_buysig = self.Elan.parse_query(self.p.buystrategy)
        self.ind_sellsig = self.Elan.parse_query(self.p.sellstrategy)

        # initialization of dictionary to store lines object that
        # the user are interested in
        if self.p.linereturn is not None:
            self.interested_obj = self.Elan.get_request_lines(self.p.linereturn)
        else:
            self.interested_obj = {}

        self.sellall = self.p.sell_all_date

        self.order = None
        # store dynamic object created during language processing
        self.dynamic_lines = self.Elan.get_dynamic_lines()

        # recorder that trace the trade history
        self.record = HistoryRecorder()

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def next(self):
        # self.log('Close, %.2f ' % (self.dataclose[0]))
        if self.order:
        # An order is pending ... nothing can be done
            return
        # Simply log the closing price of the series from the reference

        if not self.position:  # not in the market
            if self.ind_buysig:  # if fast crosses slow to the upside
                # self.log('BUY CREATE, %.2f' % self.dataclose[0])
                order = self.buy(coo=False, coc=True, execute_now=True)  # enter long
                self.order = order

        else:
            if self.ind_sellsig:
                # self.log('SELL CREATE, %.2f' % self.dataclose[0])
                order = self.close(coo=False, coc=True, execute_now=True)  # close long position
                self.order = order   
            elif self.sellall == numdate2str(self.datadate[0]):
                order = self.close(coo=False, coc=True, execute_now=True)
                self.order = order

    def notify_trade(self, trade):
        # add trade record to recorder
        # if trade.status == 1:
        #     self.record.add_hist(trade.history, record_name="buy")
        # status 2 for sell history
        # sell history includes buy history
        if trade.status == 2:
            self.record.add_hist(trade.history, record_name="sell")

        # inform the dynamic object to do the update
        for dyn in self.dynamic_lines:
            dyn.tradeopen(trade)

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            #self.log('ORDER ACCEPTED/SUBMITTED')
            self.order = order
            return
        # if order.status in [order.Expired]:
        #     pass
        #     self.log('BUY EXPIRED')
        # 
        # elif order.status in [order.Completed]:
        #     if order.isbuy():
        #         self.log('BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
        #             (order.executed.price,
        #              order.executed.value,
        #              order.executed.comm))
        # 
        #     else:  # Sell
        #         self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
        #                  (order.executed.price,
        #                   order.executed.value,
        #                   order.executed.comm))
        # 
        # elif order.status in [order.Canceled, order.Margin, order.Rejected]:
        #     self.log('Order Canceled/Margin/Rejected')
        # 
        # else:
        #     print("order", order.status)
        self.order = None

    def stop(self):
        self.robot.update_collection_fromstrategy(self)
