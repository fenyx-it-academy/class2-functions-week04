def counter(x):
    """This function gives how many upper case and smaller case letters in a word """
    list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'y', 'z']
    list2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'Y', 'Z']
    counter1 = sum(True for i in x if i in list1)
    counter2 = sum(True for i in x if i in list2)
    return '\nLowercase letter : ' + str(counter1) + '\nUppercase letter : ' + str(counter2)


print(counter(x=input('Write Anything..')))
