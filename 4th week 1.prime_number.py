"""Write a function that checks if any given number is a prime number or not.
	For example:
		function call : prime_number(123)
		output : 123 is not prime number"""""



def prime_number(n):          #We define a prime_number function
    if n>1:                   #conditoin-1 if the number from user is greater than 1.
        for i in range(2,int(n-1)):  ##This is a prime number definition.We look divisor of number
            if n%i==0:               #if there is any divisor except 1 and itself.It is not prime number
                return "It is not prime number"
        return "It is a prime number"
    return "It is not prime"   # condition-2 if n<=1
print(prime_number(123))
