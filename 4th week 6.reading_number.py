"""Write a function that gives the reading of entered any two-digit number.
	For example: 28---------------->Twenty Eight"""
first_digit=["","one","two","thre","four","five","six","seven","eight","nine"]
second_digit=["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
def read(a): #We define read function.And we define empty string in first_digit ,if we dont use first digit
    x=a %10  #And we define 2 emties string in second_digit,if we dont use from 1 to 9 numbers and from 11 to 19
    y=a//10  # Variable x is for first digit number and variable y is for seconf digit number
    if a==11:         #We define contion seperately  from 11 to 19
        return "eleven"
    if a==12:
        return "twelve"
    if a==13:
        return "thirteen"
    if a==14:
        return "forteen"
    if a==15:
        return "fifteen"
    if a==16:
        return "sixteen"
    if a==17:
        return "seventeen"
    if a==18:
        return "eighteen"
    if a==19:
        return "nineteen"
    return second_digit[y]+" "+first_digit[x]  #We print firstly seconddigit then firstdigit
print(read(28))







