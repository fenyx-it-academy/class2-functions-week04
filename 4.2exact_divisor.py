def exact_divisor(x):
    """This function  finds exact divisors of a number"""
    divisors_list = [i for i in range(1, x+1) if x % i == 0]
    return divisors_list


print(exact_divisor(x=int(input('Please enter a number!'))))
