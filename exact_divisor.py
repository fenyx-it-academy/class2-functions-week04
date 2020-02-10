'''


Write a function that finds the exact divisors of a given number.
	For example:
		function call : exact_divisor(12)
		output : 1,2,3,4,6,12

'''
#users number
number = int(input("Enter a number : "))
def exact_divisor(number) :
    i = 1
    while i <= number : # while True
        if ((number % i )==0) :
            print (i)
        i = i + 1

exact_divisor(number)
