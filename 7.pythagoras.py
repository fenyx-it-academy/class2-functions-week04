"""
Write a function that gives any number combination forming the pythagoras triangle between 1 and 100.
        For example (between 1-20) -----> (3,4,5),(5,12,13),(6,8,10),(9,12,15),(8,17,15)

A Pythagorean triple consists of three positive integers a, b, and c, such that a2 + b2 = c2.
 Such a triple is commonly written (a, b, c), and a well-known example is (3, 4, 5)
"""


# define a function named pythagoras_triangle
def pythagoras_triangle(first_int,second_int):
    """ This function gives any number combination forming the pythagoras triangle between 1 and 100. """

    # define edges of the triangle
    a_tri, b_tri, c_tri = 0, 0, 0 

    # define a the pythagoras triangles list 
    pythagor_list= []

    # given numbers have to be between 1 and 100.
    if 1 <= first_int <= 100 and 1 <= second_int <= 100 and first_int < second_int:
        for a_tri in range(first_int,second_int):
            for b_tri in range(first_int,second_int):
                c_tri = (a_tri** 2 + b_tri ** 2) ** 0.5

                # c edge have to be integer and between first and second given numbers
                if c_tri == int(c_tri) and first_int <= int(c_tri) < second_int:
                    # we add triangels with set, because we dont need repeated items
                    pythagor_list.append({a_tri, b_tri, int(c_tri)})
                    
        # return set Comprehension, we can add tuple to sets
        return {tuple(x) for x in pythagor_list}
    return "Please enter between 1 and 100."


# invoke the function with two arguments
result = pythagoras_triangle(1,20)
print(result)

# The End