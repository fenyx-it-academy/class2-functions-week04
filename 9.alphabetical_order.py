def alphabetical_order(words):
    """ The function that takes an input form user which separates the words hyphen icon(-) and sort the words
    alphabetical order and then adds hyphen icon (-) between them and gives the output of it. """
    words_list=words.split("-")
    words_list.sort()
    words_new=""
    for i in words_list:
        words_new += i + "-"

    return words_new.rstrip("-")

something=input("Write a few words that you want to order alphabetically:")
print(alphabetical_order(something))
