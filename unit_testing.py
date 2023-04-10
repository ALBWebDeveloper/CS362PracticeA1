def avgList(list):
    """
    Averages the elements in a list
    :arg list: list of numbers
    :returns: the average of the list
    """

    sum = 0
    if len(list) ==0:
        raise Exception(ZeroDivisionError)
        return -1
    for num in list:
        sum = sum + num
    return int(sum) / len(list)