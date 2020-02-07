def unique_list(list1):
    "The function that filters unique(unrepeated) all elements of a given list."
    list2=set(list1)
    list3=list(list2)
    return list3

print(unique_list([1,2,3,3,3,3,4,5,5]))