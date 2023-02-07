# the recursive version below is approximately equivalent to this iterative version
def FAC2(n):
    result = 1
    while n > 0:
        result = result * n
        n = n - 1
    return result

def FAC(n):
    # snapshot(printstack=True)
    if n == 0:
        return 1
    # this is equivalent to return FAC(n - 1) * n but allows us
    # to insert a snapshot call after the recursive call returns
    r = FAC(n-1)
    # snapshot(printstack=True)
    return r * n

# clear_frames()
FAC(5)
# show_animation(size=[10,5])