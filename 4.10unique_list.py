def unique_list(x):
    """This function returns unique elements of a list from small to big .. """
    x = set(x)
    return list(x)


print(unique_list([1, 2, 4, 5, 45, 4, 43, 56, 1, 1, 2, 3, 3, 5, 5, 5, 5]))