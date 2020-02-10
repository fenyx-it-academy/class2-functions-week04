'''
Write a function that controls the given inputs wheter they are equal with their reverse writing or not.
	Ex: madam, tacocat, utrecht
Result: True, True, False
'''
def reverse(s):

    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
s = input("Enter a Word : ")
back = reverse(s)
if s == back:
    print( True)
else:
    print(False)

