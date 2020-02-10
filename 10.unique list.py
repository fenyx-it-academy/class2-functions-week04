def unique_list(list1): #function to get unique values
  list_set=set(list1)  #insert the list to the set,Since the number cannot be repeatedly written to the set
  list2=(list(list_set)) #convert the set to the list
  print(list2)

list1 = [1,2,3,3,3,3,4,5,5]# driver code
print("unique list is")
unique_list(list1)

