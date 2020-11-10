from utils import numdate2str, AutoOrderedDict

read_history_map = {
    "pnl": lambda x: x.status.pnl,
    "pnlcomm": lambda x: x.status.pnlcomm,
    "value": lambda x: x.status.value,
    "size": lambda x: x.event.size,
    "price": lambda x: x.event.price,
    "commission": lambda x: x.event.commission,
    "dt": lambda x: x.event.order.dteos
}


# goal of history Reader is to provide a easy way to read history record
class HistoryReader:

    def __init__(self, hist, interested=("pnl", "pnlcomm", "value", "size", "price", "commission", "dt")):
        # select items that are useful in record
        self.interested = interested
        self.hist = hist
        self.lookup_dict = self.hist_lookup_dict()

    def hist_lookup_dict(self):
        # dt has to be manually added because the "dt" value in order object
        # represent the time when order is notified(some day after buy/sell)
        # that's why we have to get the real time ordering buy/sell in event.order.dteos

        sell_dict = AutoOrderedDict({rec: [] for rec in self.interested})
        sell_dict.dt = []
        buy_dict = AutoOrderedDict({rec: [] for rec in self.interested})
        buy_dict.dt = []
        lookup_dict = AutoOrderedDict(buy=buy_dict, sell=sell_dict)

        # decompose history records for into better format
        if self.hist:
            for rec in self.hist:
                for attr in self.interested:
                    # map correct object and add it to buy & sell dict
                    lookup_dict.buy[attr].append(read_history_map[attr](rec[0]))
                    lookup_dict.sell[attr].append(read_history_map[attr](rec[1]))
                                                                                                            
            # convert time in float into human readable string
            if "dt" in self.interested:
                lookup_dict.buy.dt = list(
                    map(lambda x: numdate2str(x), lookup_dict.buy.dt))
                lookup_dict.sell.dt = list(
                    map(lambda x: numdate2str(x), lookup_dict.sell.dt))
   
        # sample structure of return value
        # AutoOrderedDict([(
        # 'sell', AutoOrderedDict([('dt', array([734919., 734934.])),
        #    ('pnl', array([ 26.66,  20.21])),
        #    ('pnlcomm', array([ 24.65448,  18.15675])),
        #    ('value', array([0., 0.])),
        #    ('size', array([-43, -43])),
        #    ('price', array([23.63, 24.11])),
        #    ('commission', array([1.01609, 1.03673]))])),(
        # 'buy', AutoOrderedDict([
        #    ('dt', array([734908., 734929.])),
        #    ('pnl', array([0., 0.])),
        #    ('pnlcomm', array([-0.98943, -1.01652])),
        #    ('value', array([ 989.43, 1016.52])),
        #    ('size', array([43, 43])),
        #    ('price', array([23.01, 23.64])),
        #    ('commission', array([0.98943, 1.01652]))]))])
        #
        # pnl(buy): is always 0 because you won't gain or loss money until you sell it
        # pnlcomm(buy): is always negative because you need to pay the commission before
        #               when order a buy
        # dt(buy/ sell): is the date of orders executed, this strange value can be
        #                turn into human-readable date string by
        # value(buy): = price * size
        # the length of array is the total number of transactions(buy-sell pairs)

        return lookup_dict

    def get_hist_value(self, string):
        return self.lookup_dict[string]

    def update_hist(self, hist):
        self.hist = hist
        self.lookup_dict = self.hist_lookup_dict()

    def get_history(self):
        return self.lookup_dict
