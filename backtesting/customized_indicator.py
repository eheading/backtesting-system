import backtrader as bt


class SMA(bt.ind.SimpleMovingAverage):
    def __init__(self):
        super().__init__()

    @classmethod
    def from_args(cls, *args):
        length = len(args)
        # Deafult arguments meanings:
        # 0 param
        # 1 param: period
        # 2 param: datafeed , period
        # reminder! datafeed can be any line input
        if length == 0:
            return cls(period=7)
        elif length == 1:
            return cls(period=args[0])
        elif length == 2:
            return cls(args[0], period=args[1])
        else:
            print("Error: SMA too many arguments")
            return None


class EMA(bt.ind.ExponentialMovingAverage):
    def __init__(self):
        super().__init__()

    @classmethod
    def from_args(cls, *args):
        length = len(args)
        # Deafult arguments meanings:
        # 0 param
        # 1 param: period
        # 2 param: datafeed , period
        # reminder! datafeed can be any line input
        if length == 0:
            return cls(period=7)
        elif length == 1:
            return cls(period=args[0])
        elif length == 2:
            return cls(args[0], period=args[1])
        else:
            print("Error: EMA too many arguments")
            return None

class Slope(bt.ind.Momentum):
    def __init__(self):
        super().__init__()

    @classmethod
    def from_args(cls, *args):
        # Deafult arguments meanings:
        # 0 param
        # 1 param: period
        # 2 param: datafeed , period
        # reminder! datafeed can be any line input
        length = len(args)
        if length == 0:
            return cls(period=1)
        elif length == 1:
            return cls(args[0], period=1)
        elif length == 2:
            return cls(args[0], period=args[1])
        else:
            print("Error: Slope too many arguments")
            return None


class RSI(bt.ind.RSI_Safe):
    def __init__(self):
        super().__init__()

    @classmethod
    def from_args(cls, *args):
        # Deafult arguments meanings:
        # 0 param
        # 1 param: period
        # 2 param: datafeed , period
        # reminder! datafeed can be any line input
        length = len(args)
        if length == 0:
            return cls(period=7)
        elif length == 1:
            return cls(period=args[0])
        elif length == 2:
            return cls(args[0], period=args[1])
        else:
            print("Error: RSI too many arguments")
            return None


class MACD(bt.ind.MACD):
    def __init__(self):
        super().__init__()

    @classmethod
    def from_args(cls, *args):
        # Deafult arguments meanings:
        # 0 param: use default period setting
        # 2 param: period_short , period_long
        length = len(args)
        if length == 0:
            return cls()
        elif length == 2:
            return cls(period_me1=args[0], period_me2=args[1])
        else:
            print("Error: RSI invalid number of arguments")
            return None


class Hightest(bt.ind.Highest):
    plotinfo = dict(subplot=False, plotabove=True)
    def __init__(self):
        super().__init__()

    @classmethod
    def from_args(cls, *args):
        # Deafult arguments meanings:
        # 0 param
        # 1 param: period
        length = len(args)
        if length == 0:
            return cls()
        elif length == 1:
            return cls(period=args[0])
        elif length == 2:
            return cls(args[0], period=args[1])
        else:
            print("Error: RSI too many arguments")
            return None


class Lowest(bt.ind.Lowest):
    plotinfo = dict(subplot=False, plotabove=True)
    def __init__(self):
        super().__init__()

    @classmethod
    def from_args(cls, *args):
        # Deafult arguments meanings:
        # 0 param
        # 1 param: period
        length = len(args)
        if length == 0:
            return cls()
        elif length == 1:
            return cls(period=args[0])
        elif length == 2:
            return cls(args[0], period=args[1])
        else:
            print("Error: RSI too many arguments")
            return None


class DynamicInd:
    pass


class CurrentBuy(DynamicInd, bt.Indicator):

    lines = ('cur_buy',)
    def __init__(self):
        super().__init__()
        self._old_tradeopen = False
        self._cur_tradeopen = False
        self.price = 0

    # param: <Bool> tradeopen_signal: True or False signal for tradeopen
    def tradeopen(self, trade):
        self._cur_tradeopen = trade.isopen
        if self.tradejustopen():
            self.price = trade.price


    def tradejustopen(self):
        return self._old_tradeopen is False and self._cur_tradeopen is True

    def next(self):

        if self.tradejustopen():
           self.lines.cur_buy[0] = self.price

        else:
            self.lines.cur_buy[0] = self.lines.cur_buy[-1]

        self._old_tradeopen = self._cur_tradeopen

    @classmethod
    def from_args(cls, *args):
        return cls()


class TrailingStopLimit(bt.Indicator):
    lines = ('trailstoplimit',)
    plotinfo = dict(subplot=False, plotabove=True)

    def __init__(self, percent):
        super().__init__()
        self.upsig = bt.ind.UpDay()
        self.percent = 1-percent

    def next(self):
        if self.upsig:
            self.lines.trailstoplimit[0] = self.data[0] * self.percent
        else:
            self.lines.trailstoplimit[0] = self.lines.trailstoplimit[-1]

    @classmethod
    def from_args(cls, *args):
        return cls(percent=args[0])


class TrailingStopLoss(bt.Indicator):
    lines = ('trailstoploss',)

    def __init__(self, percent):
        super().__init__()
        self.stoplimit = TrailingStopLimit(percent=percent)
        self.lines.trailstoploss = self.datas[0] < self.stoplimit

    @classmethod
    def from_args(cls, *args):
        return cls(percent=args[0])


class StopLoss(DynamicInd, bt.Indicator):
    lines = ('stoploss',)

    def __init__(self, percent):
        super().__init__()
        self.percent = 1 - percent
        self.buyprice = CurrentBuy()

    def next(self):
        self.lines.stoploss[0] = self.datas[0] < self.buyprice[0] * self.percent

    # using this to notify CurrentBuy() the trade info
    def tradeopen(self, trade):
        self.buyprice.tradeopen(trade)

    @classmethod
    def from_args(cls, *args):
        return cls(percent=args[0])


class DIF(bt.Indicator):
    lines = ('dif',)

    def __init__(self, period_short=12, period_long=24):
        super().__init__()
        self.short_ema = EMA.from_args(period_short)
        self.long_ema = EMA.from_args(period_long)
        self.lines.dif = self.short_ema - self.long_ema

    @classmethod
    def from_args(cls, *args):
        length = len(args)
        if length == 0:
            return cls()
        elif length == 1:
            return cls(period_short=args[0])
        elif length == 2:
            return cls(period_short=args[0], period_long=args[1])


class DEA(bt.Indicator):
    lines = ('dea',)

    def __init__(self, period_short=9, period_mid=12, period_long=26):
        super().__init__()
        self.dif = DIF.from_args(period_short, period_long)
        self.lines.dea = EMA.from_args(self.dif, period_mid)

    @classmethod
    def from_args(cls, *args):
        length = len(args)
        if length == 0:
            return cls()
        elif length == 1:
            return cls(period_mid=args[0])
        elif length == 2:
            return cls(period_short=args[0], period_long=args[1])
        elif length == 3:
            return cls(period_short=args[0], period_mid=args[1], period_long=args[2])


#class DynamicHighest(DynamicInd, bt.Indicator):
#    lines = ('dyn_highest',)
#    plotinfo = dict(subplot=False, plotabove=True)
#
#    def __init__(self):
#        super().__init__()
#        self._tradeopen = False
#
#    def tradeopen(self, yesno):
#        self._tradeopen = yesno
#
#    def next(self):
#        if self._tradeopen:
#            self.lines.dyn_highest[0] = max(self.data[0], self.dyn_highest[-1])
