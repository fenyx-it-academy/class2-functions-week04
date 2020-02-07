"""
Write a function that controls the given inputs wheter they are equal with their reverse writing or not. 
        Ex: madam, tacocat, utrecht 
Result: True, True, False
"""

# # define a function named unique_list parameter is arg *dromes
def palindromes_check(*dromes):

    # chech input items equal with their reverse
    check_list = [items.endswith(items[::-1]) for items in dromes]

    """for items in dromes:
        check_list.append(items.endswith(items[::-1]))"""

    return check_list


user_list = []
list_items = ''

# Enter the list items until q
while list_items != 'q':
    list_items = input("Enter the list items as a string: (to stop the program please enter 'q'): ")
    if list_items != 'q':
        user_list.append(list_items)
    else:
        break


print(palindromes_check(*user_list))


# The End