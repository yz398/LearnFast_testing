def sum_list(x):
    """
    Returns the sum of a list

    :param x: list to be summed
    :type x: list
    :raises EmptyListException: if empty list is passed in
    :raises DictionaryException: if dict is passed in

    :return: sum of list
    :rtype: float
    """
    try:
        import logging
    except ImportError:
        print("Could not import logging module")
        return
    else:
        logging.basicConfig(filename="./sum_list.log", filemode='w', 
                level=logging.DEBUG)
    if not x: 
        logging.warning("Passed in an empty list")
        raise EmptyListException()
        return None
    if type(x) == dict:
        raise DictionaryException()
        logging.warning("Passed in a dictionary")
        return None
    try:
        logging.info("Trying to find the sum")
        the_sum = sum(x)
    except TypeError:
        logging.error("Inccorect parameter type passed in")
        return None
    else:
        return float(the_sum)

class CustomListExceptions(BaseException):
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

class EmptyListException(CustomListExceptions):
    """
    Exception to be thrown if empty list is passed in
    """
    pass

class DictionaryException(CustomListExceptions):
    """
    Exception to be thrown if dictionary is passed in
    """
    pass
