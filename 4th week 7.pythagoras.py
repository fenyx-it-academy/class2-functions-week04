"""Write a function that gives any number combination forming the pythagoras triangle between 1 and 100.
	For example (between 1-20) -----> (3,4,5),(5,12,13),(6,8,10),(9,12,15),(8,17,15)"""


def pythagoras(n): #We define function pythagoras
    k=[]      #we use this empty list for for loop
    for x in range(1,n):  #We set 3 for loops for scanning alls values of edges.Firs for is for value of edge x
        for y in range(1,n):           #Second for loop is for edge y
            for z in range(1,n):       #Third for loop is for edge z
                if y<z and x*x==y*y+z*z:   # we define x as a pythagoras.We use pythagoras theorem.
                    k+=[(y, z, x)]         # If it provides pythagoras theorem,We add the edges of triangle to list k.
    return k                                # And finally we print list k.
print(*(pythagoras(100)))



