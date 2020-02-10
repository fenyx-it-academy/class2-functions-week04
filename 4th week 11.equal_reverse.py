"""Write a function that controls the given inputs wheter they are equal with their reverse writing or not.
	Ex: madam, tacocat, utrecht
Result: True, True, False"""

def rev_equal(k):  # We define function rev_equal
    if k==k[::-1]: # And we set condition for controlling reverse writing is equal or not
        return True  #If it is equal we write True
    return False     #Else we write False
print(rev_equal("madam"))