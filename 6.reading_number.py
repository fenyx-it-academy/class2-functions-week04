#We took our two-digit number from outside. We made number definitions. We recorded them as dictionary.
def reading_number(number):
    one_digit={"0":"","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}
    two_digit1={"10":"ten","11":"eleven","12":"twelve","13":"thirteen","14":"fourteen","15":"fifteen","16":"sixteen",
               "17":"seventeen","18":"eightteen","19":"nineteen",}
    #Since the numbers up to 20 are different, we made them in dictionary
    two_digit2={"2":"twenty","3":"thirty","4":"forty","5":"fifty","6":"sixty","7":"seventy","8":"eighty","9":"ninety"}
    if len(number)==2 and int(number)>19:
        reading=two_digit2[number[0]] + one_digit[number[1]]
        return reading
    else:
        reading=two_digit1[number]#Since the numbers up to 20 are named separately, it is sufficient to give the direct number without taking numbers index
        return reading
number=input("enter number:")
#we throw it into its variable.
print(reading_number(number))
