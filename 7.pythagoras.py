def pythagors():
    pythagors_list=[]
    for i in range(1,101):
        for j in range(1,101):
            k=(i**2+j**2)**0.5#The Pythagoras method is k ** 2 = i ** 2 + j ** 2.
            if k==int(k):#If k is not taken as integer, the result cannot be achieved.
               pythagors_list.append((i,j,int(k)))#The second parenthesis was used because the append method can take a single value
    return pythagors_list
for k in pythagors():#if we write j or i instead of k here we would get the same result
#I used the for loop for the bottom and bottom results. If I print directly, there will be a long result side by side
    print(k)