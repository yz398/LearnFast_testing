import pytest


def test_min_max_list():
    """
    tests for assignment5
    prove everything well 
    """
    try:
        from list_module.min_max_list import min_max_list
    except ImportError as err:
        print('big problem\n', err)
        return 
    with pytest.raises(ValueError):
        return_error([])
    with pytest.raises(TypeError):
        return_error(['s', 's']) 
    test_data1 = [0, -3, -1.2, 10]
    test_data2 = [1, 3, 2, 5]
    test_data3 = [-3/2, -9, -3, -7, -1]
    test_data4 = []
    test_data5 = [1,2,'ag']
    test_data6 = (1,2,3)
    test_answer1 = (-3, 10)
    test_answer2 = (1, 5)
    test_answer3 = (-9, -1)
    test_answer4 = (None, None)
    test_answer5 = []
    test_answer6 = ['s','s']
    assert test_answer1 == min_max_list(test_data1)
    assert test_answer2 == min_max_list(test_data2)
    assert test_answer3 == min_max_list(test_data3)
    assert test_answer4 == min_max_list(test_data4)
    assert test_answer5 == min_max_list(test_data5)
    assert test_answer6 == min_max_list(test_data6) 
