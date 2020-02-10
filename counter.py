'''
Write a function that takes an input from user and than gives the number of upper case letters and smaller case letters of it.
	For example :
		function call: counter("asdASD")
		output: smaller letter : 3
		upper letter : 3
'''
def string_test(s):
    upper_list=[]
    smaller_list=[]
    for i in s:
        if i.isupper():
           upper_list.append(i)
        elif i.islower():
           smaller_list.append(i)
        else :
           pass
    print("Smaller Letter : ",len(smaller_list))
    print("Upper Letter :",len(upper_list))
s = input("Enter a word : ")
string_test(s)