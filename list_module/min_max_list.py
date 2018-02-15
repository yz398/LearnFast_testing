def min_max_list(x):
    """
    find the minimum and the maximum of a list and return a tuple
    :param x: the input should be a list
    :raises ImportError:  if the module not found
    :raises TypeError:  if the input is not a list or the input includes string
    :raises ValueError: if the input includes string
    
    :returns: return a tuple include minimum and maximum of the list 
    :rtype: (float,float)
    """
    try:
        import logging
    except ImportError:
        print('ImportError')
    else:
        logging.basicConfig(filename='example.log', level=logging.DEBUG, 
                            filemode='w')   
    if type(x) is not list:
        logging.error('Watch out!The input should be list')
        raise TypeError('TypeError with the input')
    for index in x:
        try:
            float(index)
        except ValueError as err:
            print('ValueError\n', err)
            raise ValueError('change the input')
            logging.debug('if the type is string, it will let us know')
            return
        except TypeError as err:
            raise TypeError('change the in put style')
            logging.debug('the type of index is wrong')
            print('TypeError\n', err)
            return    
    if not x:
        return (None, None)
        logging.warning('no index there')
    my_min = min(x)
    my_max = max(x)
    my_min_max = (my_min, my_max)
    logging.info('well done')
    return my_min_max 