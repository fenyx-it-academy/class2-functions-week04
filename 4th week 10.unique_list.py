"""Write a function that filters unique(unrepeated) all elements of a given list.
For example :
		function call: unique_list([1,2,3,3,3,3,4,5,5])
		output : [1, 2, 3, 4, 5]"""
t=[1, 3, 5, 6, 3, 5, 6, 1,5,6,3,3,8]  # We have a list and we will filter this list
print ("The original list is:"+str(t))  # We print original list for seeing differences
unique=[]                                    #And we define list unique for using for loop
def unique_list(t):                          #We define function unique_list
    for i in t:                              #We set for loop for scanning list
        if i not in unique:                  #If it is not in list,We will add the number to unique list
            unique.append(i)
    return "The list after removing repeated numbers:"+str(unique)  #And finally we print our new list
print(unique_list(t))