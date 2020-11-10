

# FeatureBase is the common base for all feature class for grammar
# Every Feature object must accept data_record from yahoo data feed
class FeatureBase:
    def __init__(self, data_record, reduction_record, **kwargs):
        self.reduction_record = reduction_record
        self.data_dict = data_record

    # the name of reduction object
    def name(self, *args):
        return "{}".format(args)

    # add reduction object into record
    def add_record(self, key, value):
        if key not in self.reduction_record.keys():
            self.reduction_record[key] = value
