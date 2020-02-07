n= int(input(('Enter a number please: ')))
list=[]
def exact_divisor(n):
    for i in range(1,n):
        if n % i == 0 :
            list.append(i)
    list.append(n)
    print(list)

exact_divisor(n)
