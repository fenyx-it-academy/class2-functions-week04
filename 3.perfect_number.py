def perfect_number(limit=1000):
    "The function that finds perfect numbers between 1 and 1000."
    num=1
    numbers = []
    while 1<= num < limit:
        divisors = [i for i in range(1,num) if num%i ==0]
        if sum(divisors)==num:
            numbers.append(num)
        num += 1
    return numbers
print(perfect_number())