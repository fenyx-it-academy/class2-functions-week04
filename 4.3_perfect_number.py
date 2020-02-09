def perfect_numbers_to_the_1000():
    """Perfect number: Perfect number, a positive integer that is equal to the sum of its proper divisors.
    This function finds the perfect numbers between 1 and 1000"""
    perfect_numbers_list = []
    for i in range(1, 1001):
        exact_divisors_list = [j for j in range(1, i) if i % j == 0]
        if sum(exact_divisors_list) == i:
            perfect_numbers_list.append(i)
    return perfect_numbers_list


print(perfect_numbers_to_the_1000())
