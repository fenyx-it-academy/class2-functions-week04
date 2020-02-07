# Write a function that finds the exact divisors of a given number.


# define a function named exact_divisor
def exact_divisor(user_num):

    """ This function finds the exact divisors of a given number. """
    # Create an empty list to add the exact divisors
    div_list = []
    # We just find the positive integer number
    if user_num > 0:
       
        # list Comprehension is same thing  as below
        div_list = [i for i in range(1, user_num+1) if user_num % i == 0 ]
        """
        # for "find some i in the range" 
        for i in range(1, user_num+1):
            # if user_num can be divided into i value without remainder
             if user_num % i == 0:
                # append it the list
                div_list.append(i)      """

        return div_list
    return "Please Enter a positive integer number"



num_ent = int(input("Enter a number to find the exact divisors of a given number: "))

# invoke the function with argument
result = exact_divisor(num_ent)
print(*result)

# THE END