#We will find the necessary function for our prime number by return it with true and false.
def prime_number(number):
    for i in range(2,number):
        if number%i==0:
            return False
    return True
#We will get the input with our while loop and we will get the result
while True:
    number=input("enter number:")
    if number.upper()=="Q":
        print("you are exiting the program")
        break
    number=int(number)
    if number==1:
        print(number,"is not prime number.")
    elif number==2:
        print(number,"is prime number.")
    else:
        if (prime_number(number)):#here we call the returns we have prepared in the function.
             print(number,"is prime number")
        else:
            print(number,"is not prime number.")





