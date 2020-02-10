"""Write a function that takes an input form user which separates the words hyphen icon(-) and sort  the words
alphabetical order and then adds hyphen icon (-) between them and gives the output of it.
	For example: input= green-red-yellow-black-white
   output= black-green-red-white-yellow"""

def color():  # We define function color.
    clrs=[n for n in input("Enter the colors:").split('-')] #We want colors from user and use split for using'-'
    clrs.sort()                                             #between the colors
    return '-'.join(clrs)                                # Then we sort colors alphabetically and print
print(color())