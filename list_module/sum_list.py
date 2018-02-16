def sum_list(x):
    """
    Returns the sum of a list

    :param x: list to be summed
    :type x: list
    :raises EmptyListError: if empty list is passed in
    :raises DictionaryError: if dict is passed in

    :return: sum of list
    :rtype: float
    :return: None if sum() cannot be computed on the input
    :rtype: NoneType
    """
    try:
        import logging
    except ImportError:
        print("Could not import logging module")
        return
    logging.basicConfig(filename="./sum_list.log", filemode='w',
                        level=logging.DEBUG)
    if not x:
        logging.warning("Empty argument given: {}".format(x))
        raise EmptyError()
    if type(x) == dict:
        logging.warning("Passed in a dictionary: {}".format(x))
        raise DictionaryError()
    try:
        logging.info("Trying to find the sum")
        the_sum = sum(x)
    except TypeError:
        logging.error("Incorect parameter type passed in: {} is "
                      "{}".format(x, type(x)))
        return None
    if float('inf') in x or float('-inf') in x:
        logging.warning("List contains infinite value")
        raise ValueError()
    else:
        return float(the_sum)


class CustomListError(BaseException):
    """
    Custom set of exceptions for this list module
    """
    def __init__(self, message=""):
        """
        Creating an instance of an exception

        :param message: optional message to explain exception
        :type message: string
        """
        self.message = message


class EmptyError(CustomListError):
    """
    Exception to be thrown if empty list is passed in
    """
    pass


class DictionaryError(CustomListError):
    """
    Exception to be thrown if dictionary is passed in
    """
    pass

if __name__ == "__main__":

    print(sum_list(5))
