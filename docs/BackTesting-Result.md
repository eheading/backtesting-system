---
tags: [backTesting-Result]
---

# BackTesting-Result

### Platform Default Behavior

1. User start with a fix amount of money( if not mentioned , we use our default value)
2. Order will be rejected if users don't have enough money.
3. We will sell all positions automatically one day before the end of run. The last day is for buffering. Nothing can be done on last day.

### Line return

 linereturn parameter is designed to return specific line objects that exist in strategies.
 All objects return by "linereturn" are array.

 Only line objects that exist in strategy can be included in linereturn.I we have:

    sellstrategy="tailing_stop(0.01) or sma(3)>sma(14)"

Then, we can set:

    linereturn = "tailing_stop(0.01); sma(3) ;sma(14) ; sma(3)>sma(14); tailing_stop(0.01) or sma(3)>sma(14)"

-   sma(3)>sma(14) is also a line with value True(non-zero values) or False(0)
    All line object  should be separated by ; 

#### Examples of Invalid linereturn

Example：

    sellstrategy="tailing_stop(0.01) or sma(3)>sma(14)"

    linereturn ="tailing_stop(0.01) or sma(3)"

 Either sma(3)>sma(14) or tailing_stop(0.01) represents a line . We can't split them like linereturn ="tailing_stop(0.01) or sma(3)".
