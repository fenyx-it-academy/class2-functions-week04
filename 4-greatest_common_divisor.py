def greatest_common_divisor():
    a = int(input("Please Enter any number : "))
    b = int(input("Please Enter any number : "))
    set_a=set()#kume elemanlari tekrarlamaz
    set_b=set()
    for i in range (1,a+1):
        if a % i == 0 :
            set_a.add(i)
    #print(set_a)

    for j in range (1,b+1):
        if b % j == 0 :
            set_b.add(j)
    #print(set_b)

    r=list(set_a.intersection(set_b))#kesisim elemanlarini siralayabilmek icin listeye aldim
    print(r[-1])

greatest_common_divisor()