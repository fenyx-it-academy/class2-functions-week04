def pythagoras():
    """gives any number combination forming the pythagoras triangle between 1 and 100"""
    triangles = []
    for i in range(1, 100):
        for j in range(i, 100):
            for k in range(j, 100):
                if i**2+j**2 == k**2:
                    triangle = (i, j, k)
                    triangles.append(triangle)
    return tuple(triangles)


print(pythagoras())
