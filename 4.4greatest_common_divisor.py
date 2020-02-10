def greatest_common_divisor(x, y):
    """this function finds greatest common divisors of two numbers """
    greatest_divisor = 0
    for i in range(1, min(x, y)+1):
        if x % i == 0 and y % i == 0:
            greatest_divisor = i
    return greatest_divisor


print(greatest_common_divisor(x=int(input('first number')), y=int(input('second number'))))
