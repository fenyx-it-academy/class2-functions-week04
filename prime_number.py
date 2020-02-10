'''
Write a function that checks if any given number is a prime number or not.
	For example:
		function call : prime_number(123)
		output : 123 is not prime number

'''


def prime_number(number):
    s = 0
    for i in range(2, number + 1):
        if number % i == 0:
            s += 1
    if s == 1:
        print(number, " is prime number")
    else:
        print(number, " is not prime number")


number = int(input("Enter a number : "))
prime_number(number)