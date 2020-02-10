"""Perfect number: Perfect number, a positive integer that is equal to the sum of its proper divisors.
The smallest perfect number is 6, which is the sum of 1, 2, and 3. Other perfect numbers are 28, 496 and 8128.
 Write a function that finds perfect numbers between 1 and 1000"""

def divisiors(x):      # Firstly we define function 'divisors' for finding all divisor of numbers
    return [y for y in range(1,int(x)) if x%y==0] #If list all divisor except itself
def perfect_numbers_in_range(a, b):  #Then we define function 'perfect_numbers_in_range'
    return [x for x in range(a,b+1) if sum(divisiors(x))==x] # If sum of divisor equal to x ,We list the numbers
print(perfect_numbers_in_range(1, 1000))                 #And we print the list of perfect number which range we want
