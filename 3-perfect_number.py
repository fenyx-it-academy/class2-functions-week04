
def perfect_number():
    Minimum = int(input("Please enter any minimum number: "))
    Maximum = int(input("Please enter any maximum number: "))
    for i in range(Minimum, Maximum - 1):
        Sum = 0
        for n in range(1, i - 1):
            if (i % n == 0):
                Sum = Sum + n

        if (Sum == i):
            print(i)

perfect_number()