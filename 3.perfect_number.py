"""
Perfect number, a positive integer that is equal to the sum of its proper divisors.
The smallest perfect number is 6, which is the sum of 1, 2, and 3.
Other perfect numbers are 28, 496 and 8128. 
Write a function that finds perfect numbers between 1 and 1000.

"""


# define a function named perfect_numbers
def perfect_numbers(num):
    """ This function finds perfect numbers between 1 and 1000. """
    # Create an empty list to add the perfect numbers
    per_list = []
    # define an integer number to count while loop between 1 and 1000
    cont_n = 1
    # while loop between 1 and 1000
    while cont_n <= num:
        sum = 0
        divisor = 1

        while divisor < cont_n:
            # if cont_n can be divided into divisor value without remainder
            # if cont_n % divisor == 0: 
            if not cont_n % divisor:
                # sum of its proper divisors.
                sum += divisor

            divisor +=  1
        # if cont_n is equal to the sum of its proper divisors.
        if sum == cont_n:
            # append this perfect numbers to the per_list
            per_list.append(cont_n)

        cont_n +=  1

    return per_list  



# define maximum searched number      
max_search_num = 1000

print("The List of Perfect numbers between 1 and {} is : \n{} ".format(max_search_num,perfect_numbers(max_search_num)))

# The End