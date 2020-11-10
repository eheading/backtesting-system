---
tags: [get started]
---

# Get Started!

## General strategy 
let's test the strategy I invented recently! The strategy is as follows:

| Ticker               | MSFT                             |
| -------------------- | -------------------------------- |
| buy when:            | 8 days sma crossdown 17 days sma |
| sell when:           | 8 days sma crossup 17 days sma   |
| from :               | 2018-1-10                        |
| to :                 | 2018-12-30                       |
| cash to start with : | 1000                             |

What we need to do is to copy the parameters mentioned above and we have finished.

Please click the get button and see the result:


```json http
{
  "method": "get",
  "url": "https://backtestingapp.herokuapp.com/api/v1/resources/bt/allinfo",
  "query": {
    "buystrategy": "sma(8) crossdown sma(17)",
    "sellstrategy": "sma(8) crossup sma(17)",
    "fromdate": "2018-1-10",
    "todate": "2018-12-30",
    "dataname": "MSFT",
    "cash": "1000"
  }
}
```

* * *


# More Examples

## Same strategy on different Ticker

| Ticker               | APPL                             |
| -------------------- | -------------------------------- |
| buy when:            | 8 days sma crossdown 17 days sma |
| sell when:           | 8 days sma crossup 17 days sma   |
| from :               | 2018-1-10                        |
| to :                 | 2018-12-30                       |
| cash to start with : | 1000                             |


```json http
{
  "method": "get",
  "url": "https://backtestingapp.herokuapp.com/api/v1/resources/bt/allinfo",
  "query": {
    "buystrategy": "sma(8) crossdown sma(17)",
    "sellstrategy": "sma(8) crossup sma(17)",
    "fromdate": "2018-1-10",
    "todate": "2018-12-30",
    "dataname": "AAPL",
    "cash": "1000"
  }
}
````

| Ticker               | APPL                             |
| -------------------- | -------------------------------- |
| buy when:            | 8 days sma crossdown 17 days sma |
| sell when:           | 8 days sma crossup 17 days sma   |
| from :               | 2018-1-1                         |
| to :                 | 2019-3-2                         |
| cash to start with : | 1000                             |

## Longer time

```json http
{
  "method": "get",
  "url": "https://backtestingapp.herokuapp.com/api/v1/resources/bt/allinfo",
  "query": {
    "buystrategy": "sma(8) crossdown sma(17)",
    "sellstrategy": "sma(8) crossup sma(17)",
    "fromdate": "2018-1-1",
    "todate": "2020-3-2",
    "dataname": "MSFT",
    "cash": "1000"
  }
}
```

## Customized strategies

| Ticker               | MSFT                                                                    |
| -------------------- | ----------------------------------------------------------------------- |
| buy when:            | (8 days sma crossdown 17 days sma) and (slope of 8days sma is negative) |
| sell when:           | 8 days sma crossup 17 days sma                                          |
| from :               | 2018-1-10                                                               |
| to :                 | 2018-12-30                                                              |
| cash to start with : | 1000                                                                    |

```json http
{
  "method": "get",
  "url": "https://backtestingapp.herokuapp.com/api/v1/resources/bt/allinfo",
  "query": {
    "buystrategy": "sma(8) crossdown sma(17) and slope(sma(8)) neg",
    "sellstrategy": "sma(8) crossup sma(17)",
    "fromdate": "2018-1-10",
    "todate": "2018-12-30",
    "dataname": "MSFT",
    "timeframe": "day",
    "cash": "1000"
  }
}
```

| Ticker               | MSFT                            |
| -------------------- | ------------------------------- |
| buy when:            | current price \<= 90            |
| sell when:           | current price > current buy + 5 |
| from :               | 2018-1-1                        |
| to :                 | 2019-3-2                        |
| cash to start with : | 1000                            |

```json http
{
  "method": "get",
  "url": "https://backtestingapp.herokuapp.com/api/v1/resources/bt/allinfo",
  "query": {
    "buystrategy": "current price <= 90",
    "sellstrategy": " current price > buy price + 5 ",
    "fromdate": "2018-1-10",
    "todate": "2018-12-30",
    "dataname": "MSFT",
    "timeframe": "day",
    "cash": "1000"
  }
}
```

## Different Time Interval

possible timeframe: day, week ,month
If we change timeframe from day to week, the basic timeframe of all strategies changes.
e.g sma(6) means 6days sma using day timeframe<br/>
    sma(6) mean 6months sma using month timeframe

| Ticker               | MSFT                              |
| -------------------- | --------------------------------- |
| time interval        | week                              |
| buy when:            | 3 weeks sma crossdown 7 weeks sma |
| sell when:           | 3 weeks sma crossup 7 weeks sma   |
| from :               | 2017-1-10                         |
| to :                 | 2017-12-30                        |
| cash to start with : | 1000                              |

```json http
{
  "method": "get",
  "url": "https://backtestingapp.herokuapp.com/api/v1/resources/bt/allinfo",
  "query": {
    "buystrategy": "sma(3) crossdown sma(7)",
    "sellstrategy": "sma(3) crossup sma(7)",
    "fromdate": "2017-1-10",
    "todate": "2017-12-30",
    "dataname": "MSFT",
    "timeframe": "week",
    "cash": "1000"
  }
}
```

## Candle Strategy

Candlestick pattern can also be used to formulate strategies:

| Ticker               | MSFT                             |
| -------------------- | -------------------------------- |
| time interval        | day                              |
| buy when:            | candle pattern "hammer" exist    |
| sell when:           | 7 days sma crossdown 14 days sma |
| from :               | 2010-5-23                        |
| to :                 | 2011-5-3                         |
| cash to start with : | 1000                             |

```json http
{
  "method": "get",
  "url": "https://backtestingapp.herokuapp.com/api/v1/resources/bt/allinfo",
  "query": {
    "buystrategy": "candle hammer",
    "sellstrategy": "sma(7) crossdown sma(14)",
    "fromdate": "2010-5-23",
    "todate": "2011-5-3",
    "dataname": "MSFT",
    "cash": "1000"
  }
}
```
## Simple mode

Sometimes we only want to get some statistical result of the run. That's why we provide the simple mode.
Here are some examples:

```json http
{
  "method": "get",
  "url": "https://backtestingapp.herokuapp.com/api/v1/resources/bt/stat",
  "query": {
    "buystrategy": "sma(8) crossdown sma(17)",
    "sellstrategy": "sma(8) crossup sma(17)",
    "fromdate": "2018-1-10",
    "todate": "2018-12-30",
    "dataname": "MSFT",
  }
}
```

```json http
{
  "method": "get",
  "url": "https://backtestingapp.herokuapp.com/api/v1/resources/bt/stat",
  "query": {
    "buystrategy": "sma(8) crossdown sma(17)",
    "sellstrategy": "sma(8) crossup sma(17)",
    "fromdate": "2018-1-1",
    "todate": "2020-3-2",
    "dataname": "MSFT"
  }
}
```


## Batch run

Batch run operation are also support. Users can evaluate the performance of specific strategy on different stock data. The stock name should be separated by ;

| Batch Run Tickers    | STM,  FB,  T,  ADBE,  DELL,  AAPL,  AMZN,  ZEUS |
| -------------------- | -------------------------------- |
| buy when:            | 7 days sma crossup 14 days sma  |
| sell when:           | 7 days sma crossdown 14 days sma |
| from :               | 2019-5-3                         |
| to :                 | 2020-5-3                         |

```json http
{
  "method": "get",
  "url": "https://backtestingapp.herokuapp.com/api/v1/resources/bt/batch",
  "query": {
    "buystrategy": "sma(7) crossup sma(14)",
    "sellstrategy": "sma(7) crossdown sma(14)",
    "fromdate": "2019-5-3",
    "todate": "2020-5-3",
    "dataname": "STM;FB;T;ADBE;DELL;AAPL;AMZN;ZEUS",
  }
}
```
* * *

## Returen lines

Users can specify returnline parameter to ask for returning line object in strategy . The result is stored in return json linerecord

| Ticker               | MSFT                             |
| -------------------- | -------------------------------- |
| buy when:            | 8 days sma crossdown 17 days sma |
| sell when:           | 8 days sma crossup 17 days sma   |
| from :               | 2018-1-10                        |
| to :                 | 2018-12-30                       |
| cash to start with : | 1000                             |
| linereturn:          |8 days sma ; 17 days sma ; 8 days sma crossup 17 days sma |
```json http
{
  "method": "get",
  "url": "https://backtestingapp.herokuapp.com/api/v1/resources/bt/allinfo",
  "query": {
    "buystrategy": "sma(8) crossdown sma(17)",
    "sellstrategy": "sma(8) crossup sma(17)",
    "fromdate": "2018-1-10",
    "todate": "2018-12-30",
    "dataname": "MSFT",
    "cash": "1000",
    "linereturn": "sma(8);sma(7);sma(8) crossup sma(17)"
  }
}
```
* * *

# More about strategies

At this point, you have understand how to make a successful api call. If you really want to make a highly personalized and powerful strategies, please refers the Documenetation: Strategy Grammar.   
