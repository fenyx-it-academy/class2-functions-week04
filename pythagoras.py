'''
Write a function that gives any number combination forming the pythagoras triangle between 1 and 100.
	For example (between 1-20) -----> (3,4,5),(5,12,13),(6,8,10),(9,12,15),(8,17,15)
'''


# a2 + b2 = c2
def pythagorean(limit):
    c = 0
    m = 2 # for range(1,m --> m-1)

    while c < limit:
        for n in range(1, m):
            a = (m * m) -(n * n)
            b = (2 * m * n)
            c = (m * m) + (n * n)
            if c > limit:
                break
            print(a, b, c)

        m = m + 1
limit = int(input("Enter a Limit : ")) # until limit it will write pythagorean tringles
pythagorean(limit)