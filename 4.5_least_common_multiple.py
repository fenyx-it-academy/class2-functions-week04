def least_common_multiple(number1, number2):
    """finds the least common multiple of two numbers"""
    common_divisors_list = [i for i in range(1, min(number1, number2) + 1) if number1 % i == 0 and number2 % i == 0]
    return number1 * number2 // max(common_divisors_list)


print(least_common_multiple(24, 12))
