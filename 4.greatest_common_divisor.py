"""
Write a function that gives the greatest common divisor  of any entered 2 numbers.
        For example:
                function call: greatest_common_divisor(15,25)
                output:5

In mathematics, the greatest common divisor (gcd) of two or more integers,
 which are not all zero, is the largest positive integer that divides each of the integers.
"""


# define a function named greatest_common_divisor
def greatest_common_divisor(fir_num, sec_num):
    """ This function gives the greatest common divisor  of any entered 2 numbers. """
    # Create two sets for both numbers
    fir_set, sec_set = set(), set()

    # if one of them 1 
    if fir_num == 1 or sec_num == 1:
        return "The greatest common divisor is absolutely 1"

    elif fir_num > 0 and sec_num > 0:
        # when i try set compr as below it does not work clear why?
        fir_set = {i for i in range(1, fir_num+1) if fir_num % i == 0}
        # for "find some i in the range"
        """for i in range(1, fir_num+1):
            # if user_num can be divided into i value without remainder
            if fir_num % i == 0:
                # add it the set
                fir_set.add(i)     """

        # set Comprehension is same thing  as below
        sec_set = {j for j in range(1, sec_num+1) if sec_num % j == 0}
        """
        # for "find some j in the range"
        for j in range(1, sec_num+1):
            # if user_num can be divided into j value without remainder
            if sec_num % j == 0:
                # add it the set
                sec_set.add(j)          """
         # find to intersections two sets then get the max value and return
        return max(fir_set.intersection(sec_set))   
    return "The Given numbers have to be positive integers "





# invoke the function as result
result = greatest_common_divisor(15,25)

print(result)

# The End