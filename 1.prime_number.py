# Write a function that checks
# if any given number is a prime number or not.
	

# define a function named prime_number
def prime_number(user_num):
    
    """ This function returns the entered number is prime number or not """
    
    # prime number has to be greater than 1
    if user_num > 1:
        # for "find some i in the range" 
        for i in range(2, user_num):
            #if it can be formed by multiplying two smaller natural numbers, it is not a pn
            if user_num % i == 0:  
                return(f"{user_num} is not a prime number.Because; it equals {i} * {user_num // i}")
        # else "none was found do" so it is a prime number
        else:
            return(f"{user_num} is a prime number")

    # if it is less than 1,returns not prime number
    return(f"{user_num} is not a prime number")  


num_ent = int(input("Enter a number: "))

# invoke the function with argument
result = prime_number(num_ent)
print(result)

# THE END