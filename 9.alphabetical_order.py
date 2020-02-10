word_list = []
def alphabetical_order(word):
    word_list.append(word)  # I added the words I entered to my list with the append method
    word_list.sort(  )  # We put them in letter order with the sort method
    return word_list

while True:
    word = input("enter word:")
    if wor d= ='q':
        break
    elif alphabetical_order(word):
        print(*word_list ,sep="-")  # I left the list with the star.I put icon(-) between sep.
