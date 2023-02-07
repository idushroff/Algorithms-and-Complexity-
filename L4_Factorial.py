# The function finds the factorial of a number 'n' recursively
def fact(n):
    snapshot()
    if n == 0:
        return 1
    else:
        # the following is equivalent to doing return n*fact(n-1)
        # but we write it this way so we can insert a snapshot()
        # call after the recursive call to fact(n-1) has finished
        r = fact(n-1)
        # snapshot()
        return n*r

# clear_frames()
n = 5
res = fact(n)
print(res)
# show_animation(size=[5,4])