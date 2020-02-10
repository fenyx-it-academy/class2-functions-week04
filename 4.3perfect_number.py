def perfect_number():
    """Perfect number: Perfect number, a positive integer that is equal to the sum of its proper divisors.
    This function gives perfect numbers between 1-1000 """
    perfect_number_list = []
    for i in range(1, 1001):
        sum_of_number = sum(a for a in range(1, i) if i % a == 0)
        if sum_of_number == i:
            perfect_number_list.append(i)
    return perfect_number_list


print(perfect_number())
