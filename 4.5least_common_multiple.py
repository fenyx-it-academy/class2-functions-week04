def least_common_multiple(a, b):
    """This function finds least common multiple of two numbers"""
    def greatest_common_divisor(x, y):
        greatest_divisor = 0
        for i in range(1, min(x, y) + 1):
            if x % i == 0 and y % i == 0:
                greatest_divisor = i
        return greatest_divisor
    least_multiple = (a*b)//greatest_common_divisor(a, b)
    return least_multiple


print(least_common_multiple(a=int(input('first number')), b=int(input('second number'))))
