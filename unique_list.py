'''
Write a function that filters unique(unrepeated) all elements of a given list.
For example :
		function call: unique_list([1,2,3,3,3,3,4,5,5])
		output : [1, 2, 3, 4, 5]
'''

def unique_list(list1):

    uniqueList = []
    for x in list1:
        if x not in uniqueList:
            uniqueList.append(x)
    for x in uniqueList:
        print (x)


list1 = [1,2,3,3,3,3,4,5,5]
unique_list(list1)


