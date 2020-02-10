"""Write a function that finds the exact divisors of a given number.
	For example:
		function call : exact_divisor(12)
		output : 1,2,3,4,6,12"""


def exact_divisor(number):  #we define exact_divisor function
    divisors=[]             #we define empty divisors and alldivisors for using for loop
    al_divisors= []
    if (number== 0):        #0 is not a divisor,Firstly we set this condition
        return "Zero has no exact divisor"
    else:                   #if it is a number except 0
        for h in range(1,number+1): #We set a for loop for scanning divisors from 1 to this number.
            if (number % h==0):     #If any number h is divisor of this number,we add to list divisors
                divisors.append(h)
                al_divisors=divisors
        return al_divisors   #Then we print all divisor
print(*(exact_divisor(20)))