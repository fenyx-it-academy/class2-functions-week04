def equal_reverse(x):
    """this function controls the given inputs whether they are equal with their reverse writing or not. """
    if x == x[::-1]:
        return True
    return False


print(equal_reverse(x=input('Please enter a word..')))
