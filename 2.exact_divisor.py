liste=[]
def exact_divisor(number):#to call whenever we want, we wrote our function with this parameter
    for i in range(1,(number+1)):
        if number%i==0:
            liste.append(i) #Adding inside the function using the append () method also affected the list outside the function
    return liste

while True:
    number=int(input("enter number:"))
    if (exact_divisor(number)):
         print(*liste,sep=",") #With a star, numbers are out of square brackets intermittently.
         break
