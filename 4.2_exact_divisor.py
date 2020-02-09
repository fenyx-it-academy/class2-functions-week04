def exact_divisor(number):
    """Finds the exact divisors of the number
    Returns a list"""
    exact_divisors_list = [i for i in range(1, number+1) if number % i == 0]
    return exact_divisors_list


print(exact_divisor(int(input('Give me a number then i find its exact divisors: '))))
