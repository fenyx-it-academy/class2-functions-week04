def equal_reverse(word):
    if word[::]==word[::-1]:#In order to see if it is equal or not, it is taken from start to finish and reverse to back index.
        return True
    else:
        return False

while True:
    word=input("enter word:")
    if word=='q':
        break
    elif equal_reverse(word):
        print("True")
    else:
        print("False")

