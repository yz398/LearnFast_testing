def max_difference(x):
    diff_array = []
    for index, number in enumerate(x):
        # if index > 0:
        if index > 0:
            print(index)
            diff = x[index] - x[index - 1]
            diff_array.append(diff)
            print(diff)
            print(diff_array)

    max_diff = max(diff_array)
    return max_diff


