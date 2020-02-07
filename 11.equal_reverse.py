def equal_reverse(*args):
    "The function that controls the given inputs whether they are equal with their reverse writing or not."
    result=""
    for i in args:
        if i == i[::-1]:
            result += f"{i} ---> True\n"
        else:
            result += f"{i} ---> False\n"

    return result

print(equal_reverse("madam", "tacocat", "utrecht", "ey edip adanada pide ye"))