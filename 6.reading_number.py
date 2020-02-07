"""
Write a function that gives the reading of entered any two-digit number. 
        For example: 28---------------->Twenty Eight

"""

# define a function named reading_digit
def reading_digit(ent_num):
    """ This function gives the reading of entered any two-digit number. """

    # create a string list which is reading of not repeated two-digit numbers
    numbers = [["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"],
    "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    # if given number is between 0 and 19, it is inside the list, which is the first element of numbers list 
    if 0 <= ent_num < 20:
        return (f"{numbers[0][ent_num]}")
    # if given number is between 20 and 100 
    elif 20 <= ent_num <= 99:
        # and if it is a multiple of 10,
        if not ent_num % 10 : 
            # return inside the numbers list
            return (f"{numbers[int(ent_num / 10) -1]}")
        # and if it not,   
        else:
            # return the first digit and the second digit separately
            return (f"{numbers[int(ent_num / 10) -1]} {numbers[0][ent_num % 10]}")

    return "Please, Don't enter a non-positive number or more than two-digit."


# invoke the function as result
result = reading_digit(28)

print(result)

# The End