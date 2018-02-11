import pytest
from Maxdiff import *


def test_Maxdiff():
    test_data1 = [1, 5, 6, 7, 12]
    test_data2 = [3, 4, 5, 56, 45]
    test_data3 = [6, 34, 23, 45, 57]
    output1 = Maxdiff(test_data1)
    output2 = Maxdiff(test_data2)
    output3 = Maxdiff(test_data3)

    assert output1 == 5
    assert output2 == 51
    assert output3 == 28
