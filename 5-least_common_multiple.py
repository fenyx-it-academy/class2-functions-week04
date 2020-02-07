#least_common_multiple
def least_common_multiple():
    a = int(input('Enter any number :'))
    b = int(input('Enter any number : '))
    set_a =set()
    set_b =set()
    for i in range(1,a+1):
        if a % i == 0 :
            set_a.add(i)

    for j in range(1,b+1):
        if b % j == 0 :
            set_b.add(j)

    r = list(set_a.intersection(set_b))
    #print(r)
    result = 1
    for k in r:
        result = result * k
    print(a*b/k)
#print(a*b/k)
least_common_multiple()















