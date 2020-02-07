def prime_number():
    n = int(input(('Enter a number please: ')))
    if n==1:
        print('Not Prime')
    for i in range(2,n):
        if n % i == 0:
            print('Not Prime')
            break
    else:
        print('Prime')

prime_number()






