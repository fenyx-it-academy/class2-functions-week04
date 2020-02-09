def equal_reverse(text=''):
    """controls the input whether it is equal to its reverse writing or not."""
    if text == text[::-1]:
        return True
    return False


print(equal_reverse(input('Please enter a text: ')))
