def reading_number(num):
    "The function that gives the reading of entered any two-digit number."
    units_digit = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven",
                   "8": "eight", "9": "nine", "0":"" }
    tens_digit = {"2": "twenty", "3": "thirty", "4": "forty", "5": "fifty", "6": "sixty", "7": "seventy",
                     "8": "eighty", "9": "ninety"}
    from_10_to_20= {"10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen", "15": "fifteen",
                     "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen"}

    if 10 <= num <= 19:
        num = str(num)
        return f"{num} ---> {from_10_to_20[num]}"

    elif 20 <= num <= 99:
        num = str(num)
        return f"{num} ---> {tens_digit[num[0]]} {units_digit[num[1]]}"

print(reading_number(28))