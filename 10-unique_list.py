def unique():
    unique_list=list(input('Please enter list items: '))
    #unique_list=[1, 2, 3, 3, 3, 3, 4, 5, 5]
    new_list=[]
    for i in unique_list:
        if i not in new_list:
            new_list.append(i)
    print(new_list)
unique()
