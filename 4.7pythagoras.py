def pythagoras():
    """finds the pythagoras triangles between 1 and 100."""
    pythagoras_list = []
    for a in range(1, 101):
        for b in range(a, 101):
            for c in range(b, 101):
                if a**2+b**2 == c**2:
                    triangle = (a, b, c)
                    pythagoras_list.append(triangle)
    return tuple(pythagoras_list)


print(pythagoras())
