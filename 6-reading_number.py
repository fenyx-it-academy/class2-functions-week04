def reading_number():
    dict_number={1:'one', 2:'two' , 3:'three' , 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven' , 12:'twelf'}
    a=input(int('please enter a number'))
    if a in dict_number.keys():
        print(dict_number.values[a])
reading_number()