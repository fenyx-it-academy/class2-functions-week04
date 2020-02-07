"""
Write a function that gives the least common multiple  of entered 2 input numbers.
        For example : 
                function call: least_common_multiple(3,4)
                output : 12

the least common multiple -the smallest positive integer that is divisible by boyh a and b
"""

# define a function named least_common_multiple
def least_common_multiple(fir_num, sec_num):
    """ This function gives the least common multiple  of entered 2 input numbers. """
    if fir_num > 0 and sec_num > 0:
        # create Set Comprehension and  get multible numbers of fir_num until max divisible by for loop 
        fir_set = {i for i in range(fir_num, fir_num * sec_num + 1, fir_num)}
            
        # create Set Comprehension and  get multible numbers of sec_num until max divisible by for loop 
        sec_set = {j for j in range(sec_num, fir_num * sec_num + 1, sec_num)}
    
        # return the minumum value of intersection of the two sets
        return min(fir_set.intersection(sec_set)) 
    return "The Given numbers have to be positive integers "

# invoke the function as result
result = least_common_multiple(3,4)

print(result)

# The End