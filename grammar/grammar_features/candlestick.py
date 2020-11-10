import backtrader as bt
from grammar.grammar_features.feature_base import FeatureBase

candle_function_map = {
    "cdl2crows": bt.talib.CDL2CROWS,
    "cdl3blackcrows": bt.talib.CDL3BLACKCROWS,
    "cdl3inside": bt.talib.CDL3INSIDE,
    "cdl3linestrike": bt.talib.CDL3LINESTRIKE,
    "cdl3outside": bt.talib.CDL3OUTSIDE,
    "cdl3starsinsouth": bt.talib.CDL3STARSINSOUTH,
    "cdl3whitesoldiers": bt.talib.CDL3WHITESOLDIERS,
    "cdlabandonedbaby": bt.talib.CDLABANDONEDBABY,
    "cdladvanceblock": bt.talib.CDLADVANCEBLOCK,
    "cdlbelthold": bt.talib.CDLBELTHOLD,
    "cdlbreakaway": bt.talib.CDLBREAKAWAY,
    "cdlclosingmarubozu": bt.talib.CDLCLOSINGMARUBOZU,
    "cdlconcealbabyswall": bt.talib.CDLCONCEALBABYSWALL,
    "cdlcounterattack": bt.talib.CDLCOUNTERATTACK,
    "cdldarkcloudcover": bt.talib.CDLDARKCLOUDCOVER,
    "cdldoji": bt.talib.CDLDOJI,
    "cdldojistar": bt.talib.CDLDOJISTAR,
    "cdldragonflydoji": bt.talib.CDLDRAGONFLYDOJI,
    "cdlengulfing": bt.talib.CDLENGULFING,
    "cdleveningdojistar": bt.talib.CDLEVENINGDOJISTAR,
    "cdleveningstar": bt.talib.CDLEVENINGSTAR,
    "cdlgapsidesidewhite": bt.talib.CDLGAPSIDESIDEWHITE,
    "cdlgravestonedoji": bt.talib.CDLGRAVESTONEDOJI,
    "cdlhammer": bt.talib.CDLHAMMER,
    "cdlhangingman": bt.talib.CDLHANGINGMAN,
    "cdlharami": bt.talib.CDLHARAMI,
    "cdlharamicross": bt.talib.CDLHARAMICROSS,
    "cdlhighwave": bt.talib.CDLHIGHWAVE,
    "cdlhikkake": bt.talib.CDLHIKKAKE,
    "cdlhikkakemod": bt.talib.CDLHIKKAKEMOD,
    "cdlhomingpigeon": bt.talib.CDLHOMINGPIGEON,
    "cdlidentical3crows": bt.talib.CDLIDENTICAL3CROWS,
    "cdlinneck": bt.talib.CDLINNECK,
    "cdlinvertedhammer": bt.talib.CDLINVERTEDHAMMER,
    "cdlkicking": bt.talib.CDLKICKING,
    "cdlkickingbylength": bt.talib.CDLKICKINGBYLENGTH,
    "cdlladderbottom": bt.talib.CDLLADDERBOTTOM,
    "cdllongleggeddoji": bt.talib.CDLLONGLEGGEDDOJI,
    "cdllongline": bt.talib.CDLLONGLINE,
    "cdlmarubozu": bt.talib.CDLMARUBOZU,
    "cdlmatchinglow": bt.talib.CDLMATCHINGLOW,
    "cdlmathold": bt.talib.CDLMATHOLD,
    "cdlmorningdojistar": bt.talib.CDLMORNINGDOJISTAR,
    "cdlmorningstar": bt.talib.CDLMORNINGSTAR,
    "cdlonneck": bt.talib.CDLONNECK,
    "cdlpiercing": bt.talib.CDLPIERCING,
    "cdlrickshawman": bt.talib.CDLRICKSHAWMAN,
    "cdlrisefall3methods": bt.talib.CDLRISEFALL3METHODS,
    "cdlseparatinglines": bt.talib.CDLSEPARATINGLINES,
    "cdlshootingstar": bt.talib.CDLSHOOTINGSTAR,
    "cdlshortline": bt.talib.CDLSHORTLINE,
    "cdlspinningtop": bt.talib.CDLSPINNINGTOP,
    "cdlstalledpattern": bt.talib.CDLSTALLEDPATTERN,
    "cdlsticksandwich": bt.talib.CDLSTICKSANDWICH,
    "cdltakuri": bt.talib.CDLTAKURI,
    "cdltasukigap": bt.talib.CDLTASUKIGAP,
    "cdlthrusting": bt.talib.CDLTHRUSTING,
    "cdltristar": bt.talib.CDLTRISTAR,
    "cdlunique3river": bt.talib.CDLUNIQUE3RIVER,
    "cdlupsidegap2crows": bt.talib.CDLUPSIDEGAP2CROWS,
    "cdlxsidegap3methods": bt.talib.CDLXSIDEGAP3METHODS,

}


# Candle feature defined methods to consume and understand candles in language Elan
# Method are used in parsing tree reduction( in transformer )
class CandleFeatureBase(FeatureBase):
    """
    Words involve in language: [candle , all words start with cdl or candle]

    candle is the top level function in this feature
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def candle(self, args):
        return candle_function_map[args[0]]

    def cdl2crows(self, args):
        return "cdl2crows"

    def cdl3blackcrows(self, args):
        return "cdl3blackcrows"

    def cdl3inside(self, args):
        return "cdl3inside"

    def cdl3linestrike(self, args):
        return "cdl3linestrike"

    def cdl3outside(self, args):
        return "cdl3outside"

    def cdl3starsinsouth(self, args):
        return "cdl3starsinsouth"

    def cdl3whitesoldiers(self, args):
        return "cdl3whitesoldiers"

    def cdlabandonedbaby(self, args):
        return "cdlabandonedbaby"

    def cdladvanceblock(self, args):
        return "cdladvanceblock"

    def cdlbelthold(self, args):
        return "cdlbelthold"

    def cdlbreakaway(self, args):
        return "cdlbreakaway"

    def cdlclosingmarubozu(self, args):
        return "cdlclosingmarubozu"

    def cdlconcealbabyswall(self, args):
        return "cdlconcealbabyswall"

    def cdlcounterattack(self, args):
        return "cdlcounterattack"

    def cdldarkcloudcover(self, args):
        return "cdldarkcloudcover"

    def cdldoji(self, args):
        return "cdldoji"

    def cdldojistar(self, args):
        return "cdldojistar"

    def cdldragonflydoji(self, args):
        return "cdldragonflydoji"

    def cdlengulfing(self, args):
        return "cdlengulfing"

    def cdleveningdojistar(self, args):
        return "cdleveningdojistar"

    def cdleveningstar(self, args):
        return "cdleveningstar"

    def cdlgapsidesidewhite(self, args):
        return "cdlgapsidesidewhite"

    def cdlgravestonedoji(self, args):
        return "cdlgravestonedoji"

    def cdlhammer(self, args):
        return "cdlhammer"

    def cdlhangingman(self, args):
        return "cdlhangingman"

    def cdlharami(self, args):
        return "cdlharami"

    def cdlharamicross(self, args):
        return "cdlharamicross"

    def cdlhighwave(self, args):
        return "cdlhighwave"

    def cdlhikkake(self, args):
        return "cdlhikkake"

    def cdlhikkakemod(self, args):
        return "cdlhikkakemod"

    def cdlhomingpigeon(self, args):
        return "cdlhomingpigeon"

    def cdlidentical3crows(self, args):
        return "cdlidentical3crows"

    def cdlinneck(self, args):
        return "cdlinneck"

    def cdlinvertedhammer(self, args):
        return "cdlinvertedhammer"

    def cdlkicking(self, args):
        return "cdlkicking"

    def cdlkickingbylength(self, args):
        return "cdlkickingbylength"

    def cdlladderbottom(self, args):
        return "cdlladderbottom"

    def cdllongleggeddoji(self, args):
        return "cdllongleggeddoji"

    def cdllongline(self, args):
        return "cdllongline"

    def cdlmarubozu(self, args):
        return "cdlmarubozu"

    def cdlmatchinglow(self, args):
        return "cdlmatchinglow"

    def cdlmathold(self, args):
        return "cdlmathold"

    def cdlmorningdojistar(self, args):
        return "cdlmorningdojistar"

    def cdlmorningstar(self, args):
        return "cdlmorningstar"

    def cdlonneck(self, args):
        return "cdlonneck"

    def cdlpiercing(self, args):
        return "cdlpiercing"

    def cdlrickshawman(self, args):
        return "cdlrickshawman"

    def cdlrisefall3methods(self, args):
        return "cdlrisefall3methods"

    def cdlseparatinglines(self, args):
        return "cdlseparatinglines"

    def cdlshootingstar(self, args):
        return "cdlshootingstar"

    def cdlshortline(self, args):
        return "cdlshortline"

    def cdlspinningtop(self, args):
        return "cdlspinningtop"

    def cdlstalledpattern(self, args):
        return "cdlstalledpattern"

    def cdlsticksandwich(self, args):
        return "cdlsticksandwich"

    def cdltakuri(self, args):
        return "cdltakuri"

    def cdltasukigap(self, args):
        return "cdltasukigap"

    def cdlthrusting(self, args):
        return "cdlthrusting"

    def cdltristar(self, args):
        return "cdltristar"

    def cdlunique3river(self, args):
        return "cdlunique3river"

    def cdlupsidegap2crows(self, args):
        return "cdlupsidegap2crows"

    def cdlxsidegap3methods(self, args):
        return "cdlxsidegap3methods"

    # methods that are not related to transformers

    @staticmethod
    def get_candlefunc(mapstr):
        return candle_function_map[mapstr]

    @staticmethod
    def get_candlefunc_dict():
        return candle_function_map
