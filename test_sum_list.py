import pytest

from list_module.sum_list import (sum_list, EmptyListException, 
DictionaryException)


def test_sum_list():
    test_data = ([1, 1, 1, 1], [0, 0], [5, -1, -10], [-9, -4], [1000, 2000, -1])
    test_answers = ([4, 0, -6, -13, 2999])
    for (example, ans) in zip(test_data, test_answers):
        assert sum_list(example) == ans
    test_type_fails = ("BME", 590, 3.0)
    for type_fail in test_type_fails:
        assert sum_list(type_fail) == None
    with pytest.raises(EmptyListException):
        sum_list([])
    with pytest.raises(DictionaryException):
        sum_list({1: 'a', 2: 'b'})
