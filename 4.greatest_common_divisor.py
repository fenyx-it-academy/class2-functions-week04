def greatest_common_divisor(number1,number2):
   greatest_common_div=1
   i=1
   while (i<=number1 and i<=number2):#we are looking for the biggest number of divisor. that's why it was used this way
       if(number1%i==0 and number2%i==0):#both of the common divisor as 'i'
           greatest_common_div=i
       i+=1#Try all the numbers up to the ''number1 en number2'' by making 'i+=1'

   return greatest_common_div

number1=int(input("enter number1:"))
number2=int(input("enter number2:"))
print(greatest_common_divisor(number1,number2))
