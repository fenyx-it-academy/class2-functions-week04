#Perfect number, a positive integer that is equal to the sum of its proper divisors.
def perfect_numbers(number):
    total = 0
    for i in range(1,number):
        if number%i==0:#to find divisors of number
           total += i #to find the sum of divisors
    return total==number

for i in range(1,10001):
    if (perfect_numbers(i)):
          print("perfect number:",i)