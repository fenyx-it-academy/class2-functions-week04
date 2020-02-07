def exact_divisor(num):
    """The function that finds the exact divisors of a given number."""
    divisors_list=[i for i in range(1,num+1) if num%i == 0]
    return divisors_list
print(exact_divisor(12))
