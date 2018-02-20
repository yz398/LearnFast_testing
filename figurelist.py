
from list_module.sum_list import (sum_list, EmptyError,
                                          DictionaryError)
from list_module.min_max_list import min_max_list
from list_module.max_difference import max_difference
class figurelist():
    """
        returns the various figures
        
        :param self: list to be determined and used later
        :type self: list
        
        :return: different attributes
    """
    def __init__(self,value = [1,2,3]):
        self.value = value
        self.min_max = None
        self.max_diff = None
        self.sum = None
    def min_max_list(self):
        self.min_max = min_max_list(self.value)
        return self.min_max
    def max_difference(self):
        self.max_diff = max_difference(self.value)
        return self.max_diff
    def sum_list(self):
        self.sum = sum_list(self.value)
        return self.sum

