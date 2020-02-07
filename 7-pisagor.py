def pisagor():
    delta=[]
    #a= int(input('Enter number please: '))
    #b = int(input('Enter number please: '))

    for a in range(1,100):
        for b in range(1, 100):
            for c in range(1, 100):
                if c**2==(a**2+b**2):
                    list_2=[a,b,c]
                    delta.append(list_2)

    print(delta)

pisagor()