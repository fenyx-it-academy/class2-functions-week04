"""
Write a function that takes an input form user 
which separates the words hyphen icon(-) 
and sort  the words alphabetical order 
and then adds hyphen icon (-) between them 
and gives the output of it. 
        For example: input= green-red-yellow-black-white 
   output= black-green-red-white-yellow
"""

# define a function named alphabetical_order
def alphabetical_order(ordered_letter):
    """ This function sorts the words alphabetical order """

    # user inputs were splited into a list,name words_list, use "-" as a separator 
    words_list = ordered_letter.split("-")
    # words_list was sorted alphabetically
    words_list.sort()
    # define a seperator
    separator = "-"
    # add hyphen icon (-) between sorted list items 
    return (separator.join(words_list))


user_letter = input("Please enter your words and use hyphen icon(-) to separete them :")

# for example
if user_letter == "":
   user_letter = "green-red-yellow-black-white"


print(alphabetical_order(user_letter))


# The End