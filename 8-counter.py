def counter():
    letter = input( "Please enter a word:" )
    count1 = 0
    count2 = 0
    for i in letter:
        if (i.islower()):
            count1 = count1 + 1
        elif (i.isupper()):
            count2 = count2 + 1

    print("smaller letter:",count1)
    print("upper letter:",count2)
counter()
