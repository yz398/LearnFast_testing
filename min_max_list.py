def min_max_list(x):

    if not x:
        return (None, None)
    my_min = min(x)
    my_max = max(x)
    my_min_max = (my_min,my_max)
    
    return my_min_max

