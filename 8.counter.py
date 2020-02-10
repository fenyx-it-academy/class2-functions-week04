def counter(word):
    count1 = 0
    count2 = 0
    for i in word:
        if i.isupper():
           count1+=1 #we add +1 for every capital letter
    print("upper letter:",count1)#It is very important for total result to make our print at cycle level.
    for j in word:
        if j.islower():
            count2+=1
    print("smaller letter:",count2)


word = input("enter word:")
counter(word)#when we call our function, we reach the result

