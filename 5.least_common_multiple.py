"""
Finding least_common_multiple: Two numbers are written side by side and the divider list is made.
It is continued starting from the smallest prime number. If both numbers are not divided, a large prime number
is passed. The process continues until both numbers are 1.
"""
def least_common_multiple(number1,number2):
    least_common_mult=1 #I started with the number 1 as we will proceed with the multiplication process while finding
    i=2 # When finding lcm(least common multiple), we first start by dividing by 2
    while True:
        # we will calculate each possibility separately
        if (number1%i==0 and number2%i==0):  #If number1 and number2 are fully divided by i
            least_common_mult*=i#This function multiplies all the parameters given to it.I can reach the result by multiplying the divisors.
            number1//=i #number1=number1//i. //:Floor division(15//2=7)
            number2//=i #The full part in i'a section
        elif (number1%i==0 and number2%i!=0):
            least_common_mult*=i
            number1//=i
        elif (number1 % i != 0 and number2 % i == 0):
            least_common_mult *= i
            number2//= i
        else:
            i+=1
        if (number1==1 and number2==1):
            break
    return  least_common_mult

number1=int(input("enter number1:"))
number2=int(input("enter number2:"))
print("least common  multiple:",least_common_multiple(number1,number2))
