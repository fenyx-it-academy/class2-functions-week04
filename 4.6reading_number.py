def reading_number(x):
    """Writes readings of numbers between 10 and 100."""
    reading1 = ['', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    reading2 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    reading3 = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
                'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    if x.isnumeric() == False:
        return 'Wrong input'
    if int(x) not in range(10, 100):
        return 'Pay attention to the number you entered!!'
    for a in range(1, 10):
        if int(x)//10 == (a+1):
            for i in range(0, 10):
                if int(x) % 10 == i:
                    return reading1[a]+' '+reading2[i]
    for b in range(0, 10):
        if int(x) % 10 == b:
            return reading3[b]


print(reading_number(x=input('Enter a number ')))
