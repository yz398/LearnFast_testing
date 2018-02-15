import pytest

def test_max_difference():
    """
        To test the max_difference function in the list_module
    """
    try:
        from list_module.max_difference import max_difference
    except ImportError:
        print('you import filed')

    test_data1 = [1, 5, 6, 7, 12]
    test_data2 = [3, 4, 5, 56, 45]
    test_data3 = [6, 34, 23, 45, 57]
    test_data4 = []
    output1 = max_difference(test_data1)
    output2 = max_difference(test_data2)
    output3 = max_difference(test_data3)
    output4 = max_difference(test_data4)
    assert output1 == 5
    assert output2 == 51
    assert output3 == 28
    assert output4 == 0
