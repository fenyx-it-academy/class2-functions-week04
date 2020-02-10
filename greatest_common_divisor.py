'''
Write a function that gives the greatest common divisor  of any entered 2 numbers.
	For example:
		function call: greatest_common_divisor(15,25)
		output:5
'''

def greatest_common_divisord(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
x = int(input("Enter First Number : "))
y = int(input("Enter First Number : "))
print(greatest_common_divisord(x,y))
