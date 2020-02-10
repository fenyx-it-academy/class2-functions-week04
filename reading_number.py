'''
Write a function that gives the reading of entered any two-digit number.
	For example: 28---------------->Twenty Eight

'''
small_numbers = ["One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
big_numbers = ["Ten","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninety"]

def reading_number(number) :
    first = number % 10
    second = number // 10

    return big_numbers[second] + " " + small_numbers[first]

number = int(input("Enter a Two Digit Number : "))

print(reading_number(number))