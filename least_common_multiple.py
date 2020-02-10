'''
Write a function that gives the least common multiple  of entered 2 input numbers.
	For example :
		function call: least_common_multiple(3,4)
		output : 12
'''

def least_common_multiple(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while True:
       if((greater % x == 0) and (greater % y == 0)):
           least_common_multiple = greater
           break
       greater += 1

   return least_common_multiple

x = int(input("Enter first number : "))
y = int(input("Enter second number : "))

print(least_common_multiple(x, y))
