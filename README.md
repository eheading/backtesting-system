# backtesting

# Documentation
https://stoplight.io/p/docs/gh/Jensen12341234/backtesting

# guidelines for code modification

### How to create new API endpoints ?
prerequisite:
- know little flask
- know class inheritance
1. open new endpoints in endpoints/bt or endpoints/{New Name} (refer to flask tutorial)
2. define your own robot( the client that help you collect data) in robots/robot
3. done


### How to change grammar rule?
prerequisite:
- know context free grammar
- know regex
- know how to use lark to write grammar rules
1. change rules in grammar/grammar_rules( !warning: small change to grammar rule cause huge change to grammar behavior,
make sure you know what you are doing before adding/deleting)
2. done


### How to add error handling code?
prerequisite:
- know little flask
- know class inheritance
1. define your new error class in exception
2. define your error handler in endpoints/error_handlers
3. use error in your code
3. done


### How to add new standard line operator like sma,rsi,macd ?
prerequisite:
- know context free grammar
- know regex
- know how to use lark to write grammar rules
- know class inheritance
1. find the indicator in backtrader <https://www.backtrader.com/docu/indautoref/>
2. in backtesting/customized_indicator, customized the original backtrader indicator
3. add new indicators to grammar/grammar_rules( !warning: small change to grammar rule cause huge change to grammar behavior,
make sure you know what you are doing before adding). This move tell our language
parser how to understand strategy from users
4. find the corresponding categories in grammar/grammar_features
5. add functions that will be used for transformer in grammar/grammar_features/{Targeted file} and
add indicators to the mapping dictionary on the top of each file
6. done


### How to add highly customized indicator/lines ?
prerequisite:
- know backtrader's code well
- know context free grammar
- know regex
- know how to use lark to write grammar rules
- know class inheritance
1. find the indicator that maybe useful to construct your indicator <https://www.backtrader.com/docu/indautoref/>
2. in backtesting/customized_indicator, customized your own indicator
3. add new indicators to grammar/grammar_rules( !warning: small change to grammar rule cause huge change to grammar behavior,
make sure you know what you are doing before adding). This move tell our language
parser how to understand strategy from users
4. find the corresponding categories in grammar/grammar_features
5. add functions that will be used for transformer in grammar/grammar_features/{Targeted file} and
add indicators to the mapping dictionary on the top of each file
6. done

# Future Improvement
1. Speed

- multiprocessing can be used in some part of code to increase speed.
  - getting data from yahooapi
  - batch run
  - or more

- On average, PyPy is 4.2 times faster than CPython.
PYPY can be to interpret our python program but compatibility issue have to be solved by yourself
When installing libraries for PYPY that make use of C language e.g numpy, something unexpected may happen.
(pypy has the highly compatibility with linux machine.And Windows machine has the lowest compatibility)

- all robot objects can be precomputed so that the backend don't have to make a new one every time
it receives a get request

- most part of ElanLineReturnProcessor object can be precomputed so that the backend don't have to make a new one every time
it receives a get request. What we change is only the datafeed(from yahooapi)

- don't use yfinance. It has some bugs and unexpected behaviors.
Every time we receive the data, we have to call pandas.dropna to remove the unexpected
nan term.
Instead we can write a own code to get data from yahooapi directly and convert data to pandas dataframe.
It is faster and more stable.

2. Program Structure

- maybe we can use a customized observer(from backtrader built in ) to replace some functionality of existing program(recorder, return lines,etc).
This can make our program more elegant.(observer is not fully studied yet)

- 1 parser is used to parser strategy and returnline at the same time. We shouldn't do this because
the languages are not the same if you think carefully

- some functions in robots are poorly made because they are not intuitive.

- in customized_indicator I make a class function .fromargs which may not be necessary.

-  Elan(language use in strategy) is not so scalable by its nature(language construct by lark). For example, if we want to make
copy of the grammar and only modify a few word, we have to redefine a new grammar.


3. Best Practice

- complete error_handling is a must in api design. This is not completed yet.
We only have error handling for date input only.

-{ error: None, ... volume:xxx, } error: None can be added to return json indicating there is no error.

- do more testing in better way please
