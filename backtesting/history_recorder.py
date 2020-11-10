from backtrader import AutoOrderedDict


# goal of recorder is to store history
class HistoryRecorder:

    def __init__(self):
        # record will be a dictionary with list values
        self.record = AutoOrderedDict()

    #  add the history to record
    # :para: <string> record_name: the look up key for the record
    # :para: <object > content: content that will be append to dictionary in list
    def add_hist(self,  content, record_name="new_record"):
        if record_name in self.record.keys():
            self.record[record_name].append(content)
        else:
            self.record[record_name] = [content]

    #  return the current history in a record
    # :para: <string> record_name: the record name
    # :para: <obj> if_none: return this value if empty record
    # :return: <obj>: the record recent item if it exist , otherwise return the None
    def get_cur_hist(self, record_name="new_record"):
        record = self.get_record(record_name)
        # mean return if the key exist and the record is not empty
        if record is not None and not self.is_empty(record):
            return record[-1]
        else:
            return None

    #  return the record
    # :para: <string> record_name: the record name
    # :return: <list>: return the record if it exist , otherwise return None
    def get_record(self, record_name="new_record"):
        return self.record[record_name] if record_name in self.record.keys() else None

    def is_empty(self, record):
        return not record
