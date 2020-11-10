import numpy as np
import json

from backtesting.history_reader import *


class TradeStat:
    # kwarg are used to put interested object for history reader
    def __init__(self, hist,  **kwargs):
        # self.lastprice = last_price
        # self.tradeclose = self.all_tradeclose(hist)
        # if self.tradeclose is not None:
        #     self.buyhist = hist
        #     if self.tradeclose:
        #         self.hist = hist
        #     else:
        #         self.hist = hist[:-1]
        # else:
        #     self.buyhist = hist
        #     self.hist = hist
        # select items that are useful
        #self.hist = hist
        # determine buy/sell hist
        self.hist = hist
        self.hist_reader = HistoryReader(self.hist, **kwargs)

        self.buysell_dict = self.form_buysell_dict()

    def form_buysell_dict(self):
        buysell_hist = self.hist_reader.get_history()
        # convert all list in dict to array for easy arithmetic
        self.hist_list2array(buysell_hist)
        return buysell_hist

    def pnlcomm_sum(self):
        return np.sum(self.buysell_dict.sell.pnlcomm)

    #  return the pnlpercentage(+ve mean gain money ; -ve mean losing money) \
    #  of transactions
    # :return: <numpy.array>: percentage profit of transaction
    def percent_income(self):
        # pnlcomm: income after paying the commission
        # buy.price: buy price without considering commission
        # buy.commission: commission for buying

        return self.buysell_dict.sell.pnlcomm\
               / (self.buysell_dict.buy.value+self.buysell_dict.buy.commission)

    #  return the pnlcomm(+ve mean gain money ; -ve mean losing money) of \
    #  transactions
    # :return: <numpy.array>: net profit of transactions
    def net_income(self):
        # pnlcomm: pnlcomm after paying the commission
        return self.buysell_dict.sell.pnlcomm

    #  return the buy array with same length as sell array by cutting the last n items
    # :return: <numpy.array> , <numpy.array>: two arr of same length
    def equal_size(self, buy_arr, sell_arr):
        sell_length = len(sell_arr)
        return buy_arr[:sell_length], sell_arr

    #  return the number of closed trade
    # :return: int : number of closed trade
    def transaction_num(self):
        if self.hist:
            return len(self.hist)
        else:
            return 0

    def trade_num(self):
        return self.transaction_num() * 2

    #  return the number of buy and sell
    # :return: int : number of buy and sell
    # def trade_num(self):
    #     if self.buyhist:
    #         if self.tradeclose:
    #             return len(self.hist) * 2
    #         else:
    #             return len(self.hist)*2 + 1
    #     else:
    #         return 0

    #  return the winning rate of transactions
    # :return: float: winning rate of transaction
    def winning_rate(self):
        percent = self.percent_income()
        return (percent > 0).sum() / self.transaction_num()

    #  return the maximum profit rate
    # :return: float: the maximum profit rate
    def max_profit_percent(self):
        mx = max(self.percent_income())
        return mx if mx > 0 else 0

    #  return the maximum loss rate
    # :return: float: the maximum loss rate
    def max_loss_percent(self):
        mn = min(self.percent_income())
        return mn if mn < 0 else 0

    #  recursively convert the values of in_dictin in all sub dictionary from list to numpy array
    # :param: <dictionary> in_dict: a history record with nested dictionary with list values
    def hist_list2array(self, in_dict):
        for key, value in in_dict.items():
            if isinstance(value, list):
                in_dict[key] = np.array(value)
            else:
                self.hist_list2array(value)

    #  recursively convert the values of in_dictin in all sub dictionary from array to numpy list
    # :param: <dictionary> in_dict: a history record with nested dictionary with array values
    def hist_array2list(self, in_dict):
        for key, value in in_dict.items():
            if isinstance(value, np.array):
                in_dict[key] = value.tolist()
            else:
                self.hist_list2array(value)

    #  return the json format of dict
    # :param: <dictionary> input_dict
    # :return: float: return the json format of dict
    def to_json(self, input_dict):
        return json.dumps(input_dict)

    def get_buysell_dict(self):
        return self.buysell_dict

    def get_allinfo_dict(self):
        if self.transaction_num() > 0:
            return {
                "sell": self.buysell_dict.sell,
                "buy": self.buysell_dict.buy,
                "maxprofitpercent": self.max_profit_percent(),
                "tradenum": self.trade_num(),
                "maxlosspercent": self.max_loss_percent(),
                "pnlcomm": self.net_income(),
                "pnlpercentage": self.percent_income(),
                "pnlfinal": self.pnlfinal(),
                "winrate": self.winning_rate(),
            }
        else:
            return {
                "sell": self.buysell_dict.sell,
                "buy": self.buysell_dict.buy,
                "maxprofitpercent": 0,
                "tradenum": self.trade_num(),
                "maxlosspercent": 0,
                "pnlcomm": 0,
                "pnlpercentage": 0,
                "sumpnlcomm": 0,
                "pnlfinal": self.pnlfinal(),
                "winrate": 0,
            }

    def get_sumpnlcomm(self):
        if self.trade_num() > 0:
            return self.pnlcomm_sum()
        else:
            return 0

    def pnlfinal(self):
        return np.prod((self.buysell_dict.sell.price
                        - (self.buysell_dict.sell.commission+self.buysell_dict.buy.commission)
                        / self.buysell_dict.buy.size)/self.buysell_dict.buy.price)

    #  return boolean telling whether all trade is closed
    # :return: <boolean> : True or False or None (None if no trade)
    def all_tradeclose(self, hist):
        if hist:
            length = len(hist[-1])
            # no pair of trade record: not closed
            if length == 1:
                return False
            # no pair of trade record: closed
            elif length == 2:
                return True
        # no trade record
        else:
            return None

    # simple stat are statistic with single number or string value. No array,object value
    def get_simple_stat(self):
        if self.transaction_num() > 0:
            return {
                "maxprofitpercent": self.max_profit_percent(),
                "tradenum": self.trade_num(),
                "maxlosspercent": self.max_loss_percent(),
                "pnlfinal": self.pnlfinal(),
                "winrate": self.winning_rate(),
            }
        else:
            return {
                "maxprofitpercent": 0,
                "tradenum": self.trade_num(),
                "maxlosspercent": 0,
                "pnlfinal": self.pnlfinal(),
                "winrate": 0,
            }