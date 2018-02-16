def max_difference(x):
    """
        Returns the maximum difference of a list
        :param x: list to be input
        :type x: list
        :raises TypeError: if input is not a list
        :raises ValueError: if the list contains a non-float or integer
        :raises ValueError: if list contains +/-infinity

        :return: the maximum difference of adjacent numbers
        :rtype: float
        """
    try:
        import logging
        from math import fabs
    except ImportError:
        print("Necessary imports failed")
        return
    logging.basicConfig(filename='max_difference.log', filemode='w',
                        level=logging.DEBUG)
    if type(x) is not list:
        logging.error("Input is not a list")
        raise TypeError()
    curr_max = 0.0
    for index, entry in enumerate(x):
        try:
            num = float(entry)
        except ValueError:
            print("your input has a invalid value: {}".format(entry))
            return None
        if num == float('inf') or num == float('-inf'):
            logging.warning("List contains infinities")
            raise ValueError()
        if index > 0:
            diff = fabs(entry - x[index-1])
            curr_max = max(curr_max, diff)
    logging.info("Returning the maximum difference")
    return curr_max
