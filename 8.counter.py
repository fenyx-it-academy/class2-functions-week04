def counter(writing):
    """The function that takes an input from user and than gives
    the number of upper case letters and smaller case letters of it."""
    upper_case=[i for i in writing if i.isupper()]
    lower_case=[i for i in writing if i.islower()]

    return f"smaller letter: {len(lower_case)}\n" \
           f"upper letter: {len(upper_case)}"

story=input("write something that includes upper case letters and smaller case letters: ")
print(counter(story))
