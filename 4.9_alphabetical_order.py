def alphabetical_order(words=''):
    """takes an input form user in which the words seperated with hyphen icon(-), sorts the words in alphabetical order,
    adds hyphen icon (-) between them and gives the output of it."""
    words = words.split('-')
    words.sort()
    return '-'.join(words)


print(alphabetical_order(input('Write the words with hyphen icon(-) between them: ')))
