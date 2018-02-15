def max_difference(x):
    """
        Returns the maximum difference of a list
        
        :param x: list to be input
        :type x: list
        :raises TypeError: if input in is not a list
        :raises ValueErrorException: if the list contain non-number

        :return: the maximum difference of adjacent numbers
        :rtype: float
        """
    try:
        import logging
        from math import fabs
    except ImportError:
        print('you import filed')
    logging.basicConfig(filename='max_difference.log', filemode='w', level=logging.DEBUG)
    if type(x) is not list:
        logging.error('Input is not a list')
        raise TypeError
    curr_max = 0.0
    for index, number in enumerate(x):
        try:
            float(number)
        except ValueError:
            print('your input have a invalid number', number)
            return
        if index > 0:
            diff = fabs(x[index] - x[index - 1])
            curr_max = max(curr_max, diff)
    logging.info('Function works out as expected')
    return curr_max