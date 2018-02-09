import pytest
from sum_list import *

def test_sum_list():
    
    test_data = ([1,1,1,1], [0,0], [], [5,-1,-10], [-9, -4], [1000, 2000, -1])
    test_answers = ([4, 0, 0, -6, -13, 2999])
    for (example, ans) in zip(test_data, test_answers):
        assert sum_list(example) == ans


