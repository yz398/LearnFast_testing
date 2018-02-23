import pytest
from figurelist import figurelist
from list_module.min_max_list import min_max_list 
from list_module.max_difference import max_difference 
from list_module.sum_list import (sum_list, EmptyError,
                                          DictionaryError) 
from tests.test_min_max_list import test_min_max_list
from tests.test_max_difference import test_max_difference
from tests.test_sum_list import test_sum_list

class test_figurelist():
    """
        tests for class figurelist
    """
    ls = figurelist(value = [1,9])
    ls.min_max_list() 
    ls.max_difference() 
    ls.sum_list() 
    test_min_max_list()
    test_sum_list() 
    assert ls.min_max == (1,9) 
    assert ls.sum == 10
    assert ls.max_diff == 8

