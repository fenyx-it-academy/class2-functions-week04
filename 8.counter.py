"""
Write a function that takes an input from user and than gives the number of upper case
 letters and smaller case letters of it.
        For example : 
                function call: counter("asdASD")
                output: smaller letter : 3
                upper letter : 3

"""
# take input for letter
user_letter = str(input("Enter a letter to find the number of upper case and smaller case of it : "))

# define a function named counter
def counter(user_arg):
    """ This function gives the number of upper case letters and smaller case letters of it """

    # use to filter and lambda functions to get upper list
    upper_list = list(filter(lambda x: x.isupper(), user_arg))
    # use to filter and lambda functions to get lower list
    lower_list = list(filter(lambda x: x.islower(), user_arg))
    return (f" smaller letter : {len(lower_list)} \n upper letter : {len(upper_list)}" )


print(counter(user_letter))

# The End