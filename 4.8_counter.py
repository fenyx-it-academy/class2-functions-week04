def counter(text=''):
    """ takes an input from user and gives the number of upper case letters and smaller case letters of it."""
    if text == '':
        return 'There is nothing to count!'
    return "Uppercase Letters: ", sum(True for count in text if count.isupper()), \
           "Lowercase Letters: ", sum(True for count in text if count.islower())


print(counter(input('Enter a text: ')))
