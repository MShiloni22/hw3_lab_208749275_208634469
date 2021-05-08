def median(values):
    """
    Returns the median value in the list
    :param values: list of values
    :return: median value
    """
    number_of_elem = len(values)
    values_sorted = sorted(values)
    # split to two cases, determined by the total number of values - odd/even
    if number_of_elem % 2 == 0:
        median1 = (values_sorted[int(number_of_elem/2)]+values_sorted[(int(number_of_elem/2))-1])/2
    else:
        median1 = values_sorted[int(number_of_elem/2)]
    return median1