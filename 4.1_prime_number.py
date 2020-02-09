def prime_number(number):
    """Checks the number is prime or not"""
    if number < 2:
        return 'The smallest prime number is 2'
    for i in range(2, number):
        if number % i == 0:
            return '{} is not a prime number'.format(number)
    return '{} is a prime number'.format(number)


print(prime_number(int(input('Which number do you want to check?: '))))
