'''
Perfect number: Perfect number, a positive integer that is equal to the sum of its proper divisors.
    	The smallest perfect number is 6, which is the sum of 1, 2, and 3. Other perfect numbers are 28, 496 and 8128.
    	Write a function that finds perfect numbers between 1 and 1000.

'''

def print_perfect_nums(start, end):
    for i in range(start, end + 1):
        sum = 0
        for x in range(1, i):
            if(i % x == 0):
                sum = sum + x
                if (sum == i):
                    print(i)
print_perfect_nums(0, 1000)