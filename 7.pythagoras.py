def pythagoras(limit=100):
    "The function that gives any number combination forming the pythagoras triangle between 1 and 100"
    numbers=list(range(1,limit))
    pythagoras_list=[]
    for a in numbers:
        for b in numbers:
            for c in numbers:
                if a**2 + b**2 == c**2 and (b,a,c) not in pythagoras_list:
                    pythagoras_list += [(a,b,c)]
    return pythagoras_list

print(pythagoras())
