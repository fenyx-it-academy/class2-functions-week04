def greatest_common_divisor(number1, number2):
    """finds the greatest common divisor of two numbers"""
    common_divisors_list = [i for i in range(1, min(number1, number2)+1) if number1 % i == 0 and number2 % i == 0]
    return max(common_divisors_list)


print(greatest_common_divisor(number1=int(input('First number: ')), number2=int(input('Second number: '))))
