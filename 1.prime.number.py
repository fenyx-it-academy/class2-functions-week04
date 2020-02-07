def prime_number(num):
    "The function that checks if any given number is a prime number or not."
    if num <= 1:
        return f"{num} is not prime number."
    for i in range(2,num):
        if num%i == 0:
            return f"{num} is not prime number."
    return f"{num} is a prime number."

print(prime_number(123))