def alphabetical_order(x):
    """This function sort elements of a list in alphabetical order"""
    x = x.split('-')
    x.sort()
    return '-'.join(x)


print(alphabetical_order(x=input('Write words with hyphen(-) between them..')))
