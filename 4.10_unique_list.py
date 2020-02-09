def unique_list(users_list):
    """filters unique elements o a list"""
    users_list = set(users_list)
    return list(users_list)


print(unique_list([9, 1, 2, 3, 3, 3, 3, 4, 5, 5]))
