"""
Write a function that filters unique(unrepeated) all elements of a given list. 
For example : 
                function call: unique_list([1,2,3,3,3,3,4,5,5])
                output : [1, 2, 3, 4, 5]

"""
# define a function named unique_list parameter is *arg
def unique_list(*args):
    """ This function filters unique(unrepeated) all elements of a given list. """

    # set compherension adds items of args to the set_args
    set_args = {items for items in args}

    """set_args = set()
    for items in args:
        set_args.add(items)"""

    return list(set_args)


print(unique_list(*[1,2,3,3,3,3,4,5,5]))


# The End