def least_common_multiple(num1,num2):
    "The function that gives the least common multiple  of entered 2 input numbers."
    common_multiple=[i for i in list(range(1, num1*num2+1)) if i%num1==0 and i%num2==0]
    return min(common_multiple)

print(least_common_multiple(3,4))





