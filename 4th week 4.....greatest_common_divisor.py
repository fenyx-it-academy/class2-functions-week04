"""Write a function that gives the greatest common divisor  of any entered 2 numbers.
	For example:
		function call: greatest_common_divisor(15,25)
		output:5"""

def greatest_common_divisor(x,y):  #We define greatest_common_divisor function.
    commondivisors=[]              #An empty list for for loop
    for i in range(1,int(x)+1):    #We scan all divisors numbers from 1 to x number or we can write y number
        if x%i==0 and y%i==0:      #If number i is divisor of x and y,we add i to my list
            commondivisors+=[i]
    return max(commondivisors)   # And we print only max divisor of x and y.This is greatest common_divisor of x and y
print(greatest_common_divisor(15,25))

