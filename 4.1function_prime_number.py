def prime_number(number):
    """Checks whether the entered number is prime or not."""
    k = sum(True for i in range(2, number) if number % i == 0)
    if (k != 0) or (number == 0) or (number == 1):
        return 'Number is not prime =(('
    return 'Number is prime =))'


print(prime_number(number=int(input('\nNUMBER: '))))
