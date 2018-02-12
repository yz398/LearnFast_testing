def max_difference(x):
    from math import fabs
    curr_max = 0.0
    for index, number in enumerate(x):
        if index > 0:
            diff = fabs(x[index] - x[index-1])
            curr_max = max(curr_max, diff)
            
    return curr_max


