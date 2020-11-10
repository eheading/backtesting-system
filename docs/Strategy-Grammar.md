---
tags: [grammar]
---

# Strategy-Grammar

## Grammar Overview

The design of grammar rules follows 3 principles:

- [x] **Intuitive**: Grammar rules are similar to natural language
- [x] **Simple**:  Users can be able describe the strategy with minimum length of words
- [x] **Expressive**:  Enable users to mix all operations in high degree of freedom. Nested operation are allowed

Here is a list of words that are commonly used in our language:

| Noun               | Verb      | Condition | Adjective | Special (Pattern)     | Special (Condition) |
| ------------------ | --------- | --------- | --------- | --------------------- | ------------------- |
| sma                | crossup   | or        | pos / +ve | candle 3linestrike    | trailingstop_loss   |
| slope              | crossdown | and       | neg / -ve | candle hammer         | stop_loss           |
| current price      | >         |           |           | candle invertedhammer |                     |
| buy price          | >=        |           |           | candle eveningstar    |                     |
| rsi                | \<        |           |           | candle morningstar    |                     |
| highest            | \<=       |           |           | candle 3whitesoldiers |                     |
| macd               | ==        |           |           | candle abandonedbaby  |                     |
| trailingstop_limit | !=        |           |           |                       |                     |
| ema                |           |           |           |                       |                     |
| volume             |           |           |           |                       |                     |

- we have 61 candle patterns but space are limited so we only provide 7 examples

> **sma**, **rsi** , **macd** are refering to **_Simple Moving Average_**, **_Relative Strength Index_**
> and **_Moving Average Convergence Divergence_** respectively. These indexes are commly use in technical analysis 

* * *

## Basic Sentence Structures

So, let’s start with simplest examples:

                              "sma(7)    upcross    sma(14)" 
                    Syntax:   { Noun      Verb        Noun }

                              "slope(sma(7))            neg" 
                    Syntax:   { Noun                  Adjective}

                              "    candle 3linestrike      "
                    
                    Syntax:   {           Special          }

- neg stands for negative

The basic structure of a query is a sentence. Sentences only have 3 Types: 

1. {Noun     Verb      Noun} 
2. {Noun      Adjective} 
3. {Special}

- special condition and special pattern are all grouped under special class 

- "sma(7) upcross sma(14)" has syntax of {Noun Verb Noun} 

- "slope(sma(7)) neg" has syntax of { Noun  Adjective}. 

- "candle 3linestrike" has syntax of { Special }. 

Therefore these 3 strategies are valid.

### Conclusion by graph

                                          Sentence
                                         /          
               {Noun Verb  Noun} | {Noun  Adj} | {Special}

### More examples

| Example | Noun                 | Verb      | Noun               |
| ------- | -------------------- | --------- | ------------------ |
| 1       | sma(7)               | crossdown | sma(14)            |
| 2       | current price        | crossup   | rsi(7)             |
| 3       | rsi(7)/3             | >=        | 1                  |
| 4       | slope(macd())        | \<        | 3                  |
| 5       | slope(macd())        | crossup   | rsi(14)            |
| 6       | sma(sma(7),5)        | crossup   | 100                |
| 7       | buy_price+(2\*9-5/8) | >=        | current price      |
| 8       | current price        | \<        | trailingstop_limit |

| Example | Noun      | Adj |
| ------- | --------- | --- |
| 1       | sma(7)    | pos |
| 2       | rsi()     | neg |
| 3       | cur_price | +ve |
| 4       | rsi()     | -ve |

| Example | Special                |
| ------- | ---------------------- |
| 1       | candle abandonedbaby   |
| 2       | candle eveningstar     |
| 3       | trailingstop_loss(0.1) |
| 4       | stop_loss(0.2)         |

* * *

## Logical Expression

Logical operations are necessary for building complicated strategies. Therefore, we provide 2 operartors: {and ,or}
to build logical expression:

               "sma(7)  upcross sma(14)        and                  sma(14) > 100" 

     Syntax:   {    Sentence                    op                     Sentence    }

              "sma(7)  upcross sma(14)    and   sma(14) > 100 or sma(14)<100      and sma(7)  downcross sma(14)" 

    Syntax: {           Sentence         op         Sentence     op     Sentence      op          Sentence }

- op stands for operator

 The basic structure of  logical expression has the following pattern: 

1. { Sentence     op     Sentence }
2. { Sentence     op     Sentence  op      Sentence     …   op    Sentence}

Like most language, "and" operator will be prioritized. That means we will  do all  "and" operation before "or" operation. We can use bracket if we really want to do operation first like:

    "sma(7)  upcross sma(14)         and       ( sma(14) > 100  or  cur_price > 100 ) " 

> For the sake of convenience, we provide alias(別名) for logical operator that has the same effect as original logical operator:

| Logical Operator | Alias   |
| ---------------- | ------- |
| and              | AND, &  |
| or               | OR , \| |

### Conclusion by graph

```

                                        Logical Expression
                                         /     
                { Sentence     op     Sentence  … op Sentence}                                                
                           /                      \
                    Sentence                    or  | and
                 /          \
 {Noun Verb  Noun}          {Noun  Adj}
```

* * *

## Basic Atom: Noun

All Noun in this language are lines that can be plotted in 2-D plane. For example, sma(7)  is a curve . sma(7)+3 , sma(7) + sma(3) , (sma(7)+ rsi(4))\*\*2  -1 mathematically speaking are all curves. 

> Concepts:
>
> - Noun represents a line object
> - Noun remain Noun after mathematical operation ( +, - ,\*, /, \*\*)

- in python \*\* means power

### Conclusion by graph

                                    Noun     ← 
                                     | _____ |
                                   math operation 

                                    Line       ← 
                                     | _____ |
                                    math operation

Line objects can be combined by arithematic operation to form new line objects.
There are 3 atomic component of line objects that we can operate with: 

1. numer
2. functions
3. keywords

### Number

Numer in our grammar also represent a line. For example number 100 represent a horizontal line y=100. What the query "sma(7)    crossup    100" does is to check if sma(7) crossup a horizontal line y=100. By this way, number in our grammar are compatible with any line object mentioned above.

Number includes negative numbers, float number and integers.

### Functions

All functions in our grammar can be return a line object. All functions have the same structure: function name +  "(" + parameters + ")" . For example,

                                sma     (3)
                  Syntax   {funcName   parameters}

#### Function references

| Item                                  | Description                                                                                                                                                                                                                                                                                      | Functions                                           | Default parameters                     |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------- | -------------------------------------- |
| Simple Moving Average                 | A simple moving average (SMA) calculates the average of a selected range of prices, usually closing prices, by the number of periods in that range. More info: <https://en.wikipedia.org/wiki/Moving_average#Simple_moving_average>                                                              | sma( data , period )<br/>sma( period )<br/>sma()    | data: the close price <br/> period: 7  |
| N days hightest                       | Calculates the highest value for the data in a given period                                                                                                                                                                                                                                      | highest(period)                                     | period: 7                              |
| Slope                                 | Calculates the slope for the data in a given period                                                                                                                                                                                                                                              | slope(data, period)<br/>slope(data)<br/>slope()     | data : the close price <br/>period : 1 |
| Relative Strength Index               | The relative strength index (RSI) is a momentum indicator used in technical analysis that measures the magnitude of recent price changes to evaluate overbought or oversold conditions in the price of a stock or other asset. More info:<https://en.wikipedia.org/wiki/Relative_strength_index> | rsi(data, period)<br/>rsi(period)<br/>rsi()         | data: the close price <br/>period: 7   |
| Moving Average Convergence Divergence | Moving Average Convergence Divergence (MACD) is a trend-following momentum indicator that shows the relationship between two moving averages of a security’s price. More info: <https://en.wikipedia.org/wiki/MACD>                                                                              | macd(period1, period2)<br/>macd(period1)<br/>macd() | period1: 14<br/>period2: 26            |
| Trailing Stop Limit                   | A Trailing Stop Limit is a limit on the maximum possible loss(percentage).More info <https://www.investopedia.com/terms/t/trailingstop.asp>                                                                                                                                                      | trailingstop_limit(percent)<br/>ts_limit(percent)   |                                        |
| Exponential Moving Average            | A Moving Average that smoothes data exponentially over time. More info <http://en.wikipedia.org/wiki/Moving_average#Exponential_moving_average>                                                                                                                                                  | ema(data, period)</br>ema(period)</br>ema()         | data: the close price <br/> period: 7  |
DIF | DIF＝EMA（CLOSE，SHORT）－EMA（CLOSE，LONG）| dif(SHORT,LONG)<br/>dif(SHORT)<br/>dif()|SHORT:12<br/>LONG:24|
DEA | DIF＝EMA（CLOSE，SHORT）－EMA（CLOSE，LONG）<br/>DEA＝EMA（DIF，MID）      | dea(SHORT,MID,LONG)<br/>dea(SHORT,LONG)<br/>dea(MID)<br/>dea()| SHORT:9<br/>MID:12<br/>LONG:24 |
### Keywords

                                                         cur_buy
                                              Syntax:  {keywords}

Keywords are functions without parameters and brackets. They return lines object like functions. Therefore, keywords can compare with functions:

                                               "cur_buy  >  sma(7)"
                                              "cur_buy  crossup sma(7)"

Keywords can do arithmetic:

                                              "cur_buy * 2 + 1  > sma(7)"

For the sake of convenience, keywords always contains alias( different keywords mean the same thing). For instance, "cur_buy" and " current_buy" are referring to the same line. These alias can be used interchangeably in the query. 

                                 " cur_buy > sma(7) and slope(current_buy) negative  "                                    

#### keywords Reference

| Items         | Description             | Alias                                                        |
| ------------- | ----------------------- | ------------------------------------------------------------ |
| current price | The current close price | price, PRICE , curprice, cur_price, current_price            |
| buy price     | The current buy price   | buy, buyprice, BUY, BuyPrice, BUYPRICE ,buy_price            |
| volume        | The current volume      | cur_volume, cur_vol, vol, current volume,cur volume, cur vol |

* * *

## Basic Atom: Verb

Verbs describe the condition to aply the strategy. For example,

                       buy_query : " sma(7) crossup sma(14)"

are telling the program to buy under the crossup condition. On the other words, what verb does is to evaluate 2 line objects into a boolean (True/ False) line object. 

#### Verb Reference

| Items     | Description           | Alias |
| --------- | --------------------- | ----- |
| crossup   | crossup               |       |
| crossdown | crossdown             |       |
| crossover | crossover             |       |
| >         | greater               | gt    |
| >=        | greater or equal to   | ge    |
| \<        | less than             | lt    |
| \<=       | less than or equal to | le    |
| ==        | equal to              | eq,=  |
| !=        | not equal to          | ne    |

## Basic Atom: Adjective

#### Adj Refernce

| Items | Description | Alias |
| ----- | ----------- | ----- |
| neg   | negative    | -ve   |
| pos   | positive    | +ve   |

## Basic Atom: The Special

The Special are describing a special timing when special condition/event happens.For example, existence of candle hammer pattern and reaching trailingstop_loss condition are so important that worth making this special grammar for them.

Here are some common properties:

1. the special are all conditions
2. The Special can't involve in any arithmetic operation
3. The Special alone is a complete sentence
4. They are not Noun, Verb ,Ajective. There don't share the same properties with Noun, Verb ,Ajective.

#### Special Pattern Reference

| Items                   | Alias                |
| ----------------------- | -------------------- |
| candle 2crows           | cdl 2crows           |
| candle 3blackcrows      | cdl 3blackcrows      |
| candle 3inside          | cdl 3inside          |
| candle 3linestrike      | cdl 3linestrike      |
| candle 3outside         | cdl 3outside         |
| candle 3starsinsouth    | cdl 3starsinsouth    |
| candle 3whitesoldiers   | cdl 3whitesoldiers   |
| candle abandonedbaby    | cdl abandonedbaby    |
| candle advanceblock     | cdl advanceblock     |
| candle belthold         | cdl belthold         |
| candle breakaway        | cdl breakaway        |
| candle closingmarubozu  | cdl closingmarubozu  |
| candle concealbabyswall | cdl concealbabyswall |
| candle counterattack    | cdl counterattack    |
| candle darkcloudcover   | cdl darkcloudcover   |
| candle doji             | cdl doji             |
| candle dojistar         | cdl dojistar         |
| candle dragonflydoji    | cdl dragonflydoji    |
| candle engulfing        | cdl engulfing        |
| candle eveningdojistar  | cdl eveningdojistar  |
| candle eveningstar      | cdl eveningstar      |
| candle gapsidesidewhite | cdl gapsidesidewhite |
| candle gravestonedoji   | cdl gravestonedoji   |
| candle hammer           | cdl hammer           |
| candle hangingman       | cdl hangingman       |
| candle harami           | cdl harami           |
| candle haramicross      | cdl haramicross      |
| candle highwave         | cdl highwave         |
| candle hikkake          | cdl hikkake          |
| candle hikkakemod       | cdl hikkakemod       |
| candle homingpigeon     | cdl homingpigeon     |
| candle identical3crows  | cdl identical3crows  |
| candle inneck           | cdl inneck           |
| candle invertedhammer   | cdl invertedhammer   |
| candle kicking          | cdl kicking          |
| candle kickingbylength  | cdl kickingbylength  |
| candle ladderbottom     | cdl ladderbottom     |
| candle longleggeddoji   | cdl longleggeddoji   |
| candle longline         | cdl longline         |
| candle marubozu         | cdl marubozu         |
| candle matchinglow      | cdl matchinglow      |
| candle mathold          | cdl mathold          |
| candle morningdojistar  | cdl morningdojistar  |
| candle morningstar      | cdl morningstar      |
| candle onneck           | cdl onneck           |
| candle piercing         | cdl piercing         |
| candle rickshawman      | cdl rickshawman      |
| candle risefall3methods | cdl risefall3methods |
| candle separatinglines  | cdl separatinglines  |
| candle shootingstar     | cdl shootingstar     |
| candle shortline        | cdl shortline        |
| candle spinningtop      | cdl spinningtop      |
| candle stalledpattern   | cdl stalledpattern   |
| candle sticksandwich    | cdl sticksandwich    |
| candle takuri           | cdl takuri           |
| candle tasukigap        | cdl tasukigap        |
| candle thrusting        | cdl thrusting        |
| candle tristar          | cdl tristar          |
| candle unique3river     | cdl unique3river     |
| candle upsidegap2crows  | cdl upsidegap2crows  |
| candle xsidegap3methods | cdl xsidegap3methods |

#### Special Pattern Reference

| Items             | Description                                                                                                                                 | Alias                       | Function                   |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | -------------------------- |
| trailingstop_loss | sell when current price is lower than trailing stop limit( in percentage).More info <https://www.investopedia.com/terms/t/trailingstop.asp> | ts_loss                     | trailingstop_loss(percent) |
| stop_loss         | cut loss: sell when current price is lower than the specific percent of the buy price                                                       | stoploss, cutloss, cut_loss | stop_loss(percent)         |
