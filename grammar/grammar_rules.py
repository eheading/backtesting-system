# This grammar is used twice: 1.initalization lines to do backtesting
#                             2. check line object in linereturn parameter

# reminder: "start: arith_expr" is used for linereturn parameter,
# it is a cheat to write less code and can run successfully with some unexpected
# input.
def elan_grammar():
    grammar = """
    // basic logical: logic_feature
    start: or_expr |  arith_expr
    ?or_expr: and_expr (or_ and_expr )*
    ?and_expr: logic_factor (and_ logic_factor)*
    ?logic_factor: action_expr |  "(" or_expr ")"
    or_: "OR" | "or" | "|"
    and_: "AND" | "and" | "&"

    // basic sentence construct
    action_expr:  interaction | description | spec_pattern
    spec_pattern: pattern                         
                | pattern_function
    pattern_function: pattern_line line_para    
                
    interaction: arith_expr verb arith_expr
    description: arith_expr adj
    adj: neg | pos


    // basic line: line feature 
    function_expr: line line_para           -> basic_function
                  |  keywords               -> keyword_func
                  |  number                 -> number_func
    keywords: buy_price  |  current_price | current_volume
    pattern_line: stop_loss | trailingstop_loss
    line: sma | slope | rsi | macd | highest | trailingstop_limit | lowest | ema | dif | dea
    line_para: "("  parameters  ")"          ->line_paras
               | "("   ")"                   ->line_para_empty

    // paramaters of a line object
    parameters: parameter ("," parameter)*     
    parameter: string |  arith_expr | none

    // lines terminal  
    stop_loss: "stoploss" | "stop_loss" | "cutloss" | "cut_loss"
    trailingstop_loss: "trailingstop_loss"| "ts_loss"
    rsi: "rsi"
    sma : "sma"
    ema: "ema"
    slope: "slope"
    macd: "macd"
    highest: "highest"
    lowest: "lowest"
    trailingstop_limit: "trailingstop_limit" | "ts_limit"
    dif: "dif"
    dea: "dea"
    
    // keywords
    buy_price: "buy" | "buyprice" | "BUY" | "BuyPrice" | "BUYPRICE" | "buy_price"| "buy price"|"cur_buy"
    current_price: "price" | "PRICE" | "curprice" |"cur_price" 
                  | "current price" | "current_price"
    current_volume: "volume"| "cur_volume" | "cur_vol" | "vol" |"current volume"
                   | "cur volume"| "cur vol"
                
    // basic arith: arith_feature
    arith_expr: arith_term (_add_op arith_term)*
    ?arith_term: arith_factor (_mul_op arith_factor)*
    ?arith_factor: factor_op arith_factor             ->factor_op_recursive
               |arith_atom ("**" arith_factor)?           ->factor_power_recursive
    ?arith_atom:  "(" arith_expr ")" | function_expr
    !factor_op: "+"     ->positive
                |"-"    ->negative
    !_add_op: "+"|"-"
    !_mul_op: "*"|"/"

    // adjective terminal
    neg: "neg" | "-ve" | "negative"
    pos: "pos" | "+ve" | "positive"

    // general terminal
    number: float | integer
    integer: SIGNED_INT  |  INT
    float: SIGNED_FLOAT | FLOAT
    string: /"[a-zA-Z_][0-9a-zA-Z_]*"/  
    none:

    // verb terminal : verb
    verb: crossup | crossdown | greater_than| greater_or_equal_than | equal
          | less_than |less_or_equal_than | crossover | not_equal
    crossup: "crossup"
    crossdown: "crossdown"
    crossover:"crossover"
    greater_than: ">" | "gt" 
    greater_or_equal_than: ">=" | "ge"  
    less_than: "<" | "lt" 
    less_or_equal_than: "<=" | "le"
    equal: "=" | "eq" | "=="
    not_equal: "!=" | "ne"

    //basic candle: candle_feature
    pattern: candle 
    candle: | cdl2crows | cdl3blackcrows | cdl3inside | cdl3linestrike
            | cdl3outside | cdl3starsinsouth | cdl3whitesoldiers | cdlabandonedbaby
            | cdladvanceblock | cdlbelthold | cdlbreakaway | cdlclosingmarubozu
            | cdlconcealbabyswall | cdlcounterattack | cdldarkcloudcover
            | cdldoji | cdldojistar | cdldragonflydoji | cdlengulfing
            | cdleveningdojistar | cdleveningstar | cdlgapsidesidewhite
            | cdlgravestonedoji | cdlhammer | cdlhangingman | cdlharami
            | cdlharamicross | cdlhighwave | cdlhikkake | cdlhikkakemod
            | cdlhomingpigeon | cdlidentical3crows | cdlinneck | cdlinvertedhammer
            | cdlkicking | cdlkickingbylength | cdlladderbottom | cdllongleggeddoji
            | cdllongline | cdlmarubozu | cdlmatchinglow | cdlmathold
            | cdlmorningdojistar | cdlmorningstar | cdlonneck | cdlpiercing
            | cdlrickshawman | cdlrisefall3methods | cdlseparatinglines | cdlshootingstar
            | cdlshortline | cdlspinningtop | cdlstalledpattern | cdlsticksandwich
            | cdltakuri | cdltasukigap | cdlthrusting | cdltristar | cdlunique3river
            | cdlupsidegap2crows | cdlxsidegap3methods

    cdl2crows: "cdl 2crows" | "candle 2crows" 
    cdl3blackcrows: "cdl 3blackcrows" | "candle 3blackcrows" 
    cdl3inside: "cdl 3inside" | "candle 3inside" 
    cdl3linestrike: "cdl 3linestrike" | "candle 3linestrike" 
    cdl3outside: "cdl 3outside" | "candle 3outside" 
    cdl3starsinsouth: "cdl 3starsinsouth" | "candle 3starsinsouth" 
    cdl3whitesoldiers: "cdl 3whitesoldiers" | "candle 3whitesoldiers" 
    cdlabandonedbaby: "cdl abandonedbaby" | "candle abandonedbaby" 
    cdladvanceblock: "cdl advanceblock" | "candle advanceblock" 
    cdlbelthold: "cdl belthold" | "candle belthold" 
    cdlbreakaway: "cdl breakaway" | "candle breakaway" 
    cdlclosingmarubozu: "cdl closingmarubozu" | "candle closingmarubozu" 
    cdlconcealbabyswall: "cdl concealbabyswall" | "candle concealbabyswall" 
    cdlcounterattack: "cdl counterattack" | "candle counterattack" 
    cdldarkcloudcover: "cdl darkcloudcover" | "candle darkcloudcover" 
    cdldoji: "cdl doji" | "candle doji" 
    cdldojistar: "cdl dojistar" | "candle dojistar" 
    cdldragonflydoji: "cdl dragonflydoji" | "candle dragonflydoji" 
    cdlengulfing: "cdl engulfing" | "candle engulfing" 
    cdleveningdojistar: "cdl eveningdojistar" | "candle eveningdojistar" 
    cdleveningstar: "cdl eveningstar" | "candle eveningstar" 
    cdlgapsidesidewhite: "cdl gapsidesidewhite" | "candle gapsidesidewhite" 
    cdlgravestonedoji: "cdl gravestonedoji" | "candle gravestonedoji" 
    cdlhammer: "cdl hammer" | "candle hammer" 
    cdlhangingman: "cdl hangingman" | "candle hangingman" 
    cdlharami: "cdl harami" | "candle harami" 
    cdlharamicross: "cdl haramicross" | "candle haramicross" 
    cdlhighwave: "cdl highwave" | "candle highwave" 
    cdlhikkake: "cdl hikkake" | "candle hikkake" 
    cdlhikkakemod: "cdl hikkakemod" | "candle hikkakemod" 
    cdlhomingpigeon: "cdl homingpigeon" | "candle homingpigeon" 
    cdlidentical3crows: "cdl identical3crows" | "candle identical3crows" 
    cdlinneck: "cdl inneck" | "candle inneck" 
    cdlinvertedhammer: "cdl invertedhammer" | "candle invertedhammer" 
    cdlkicking: "cdl kicking" | "candle kicking" 
    cdlkickingbylength: "cdl kickingbylength" | "candle kickingbylength" 
    cdlladderbottom: "cdl ladderbottom" | "candle ladderbottom" 
    cdllongleggeddoji: "cdl longleggeddoji" | "candle longleggeddoji" 
    cdllongline: "cdl longline" | "candle longline" 
    cdlmarubozu: "cdl marubozu" | "candle marubozu" 
    cdlmatchinglow: "cdl matchinglow" | "candle matchinglow" 
    cdlmathold: "cdl mathold" | "candle mathold" 
    cdlmorningdojistar: "cdl morningdojistar" | "candle morningdojistar" 
    cdlmorningstar: "cdl morningstar" | "candle morningstar" 
    cdlonneck: "cdl onneck" | "candle onneck" 
    cdlpiercing: "cdl piercing" | "candle piercing" 
    cdlrickshawman: "cdl rickshawman" | "candle rickshawman" 
    cdlrisefall3methods: "cdl risefall3methods" | "candle risefall3methods" 
    cdlseparatinglines: "cdl separatinglines" | "candle separatinglines" 
    cdlshootingstar: "cdl shootingstar" | "candle shootingstar" 
    cdlshortline: "cdl shortline" | "candle shortline" 
    cdlspinningtop: "cdl spinningtop" | "candle spinningtop" 
    cdlstalledpattern: "cdl stalledpattern" | "candle stalledpattern" 
    cdlsticksandwich: "cdl sticksandwich" | "candle sticksandwich" 
    cdltakuri: "cdl takuri" | "candle takuri" 
    cdltasukigap: "cdl tasukigap" | "candle tasukigap" 
    cdlthrusting: "cdl thrusting" | "candle thrusting" 
    cdltristar: "cdl tristar" | "candle tristar" 
    cdlunique3river: "cdl unique3river" | "candle unique3river" 
    cdlupsidegap2crows: "cdl upsidegap2crows" | "candle upsidegap2crows" 
    cdlxsidegap3methods: "cdl xsidegap3methods" | "candle xsidegap3methods" 

    %import common (NUMBER,  WS,SIGNED_INT,INT,SIGNED_FLOAT,FLOAT )
    %ignore WS
    """
    return grammar
