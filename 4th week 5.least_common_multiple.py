"""Write a function that gives the least common multiple  of entered 2 input numbers.
	For example :
		function call: least_common_multiple(3,4)
		output : 12"""

def least_common_multiple(x,y): #We define least_common_multiple function
    least_common=[]   #Empty list for for loop
    for i in range(1,int(x)*int(y)+1): #we scan from 1 to x*y.Because  l.c.d(x,y)*g.c.d(x,y)=x*y.Thus always l.c.d<=x*y
        if i%x==0 and i%y==0:          #If we dont use x*y ,It goes infinite.if they are prime among them l.c.d=x*y
            least_common+=[i]          #We add common multiplies to list
    return min(least_common)
print(least_common_multiple(3,4))




