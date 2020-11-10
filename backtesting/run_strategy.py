from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import backtrader as bt
from backtesting.general_strategy import GeneralStrategy


# run the general strategy and initialization for the strategy
def runstrat(myrobot):
    # Create a cerebro entity
    cerebro = bt.Cerebro(runonce=False, preload=True, quicknotify=True, maxcpus=2)  # tradehistory=True cheat_on_open=True)#tradehistory=True,
    cerebro.addobserver(bt.observers.Broker)

    cerebro.addstrategy(GeneralStrategy, **myrobot.collection.datafeed.strategy_dict)

    data = myrobot.collection.datafeed.datamode(**myrobot.collection.datafeed.datafeed_dict)

    # Add the Data Feed to Cerebro
    cerebro.adddata(data)
    # Set our desired cash start
    cerebro.broker.setcash(myrobot.collection.datafeed.cash)

    cerebro.broker.setcommission(commission=myrobot.collection.datafeed.commission)

    cerebro.broker.set_coc(True)

    # cerebro.addsizer(bt.sizers.SizerFix, stake=1)#bt.sizers.AllInSizerInt)

    # * 100 because n % where n should be scale up first
    cerebro.addsizer(bt.sizers.PercentSizerInt, percents=(1-myrobot.collection.datafeed.commission) * 100)

    # cerebro.addanalyzer(bt.analyzers.TradeAnalyzer)
    cerebro.run(tradehistory=True)
    # cerebro.plot(style='candlestick',volume=False)
    # cerebro.plot(volume=False)
