def greatest_common_divisor(num1, num2):
    "The function that gives the greatest common divisor  of any entered 2 numbers."
    num1_divisors = [i for i in range(1, num1 +1) if num1 %i == 0]
    num2_divisors = [i for i in range(1, num2 +1) if num2 %i == 0]
    common_divisor = [i for i in num1_divisors if i in num2_divisors]
    return max(common_divisor)

print(greatest_common_divisor(15, 25))

