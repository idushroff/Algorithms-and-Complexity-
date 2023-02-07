def Fib3(n):
    a = 1
    b = 0
    while n > 0:
        # snapshot()
        a = a + b
        b = a - b
        n = n - 1
    # snapshot()
    return a

# clear_frames()
print(Fib3(6))
# show_animation(size=[4,4])


# We can phrase the linear version using recursion.

def Fib2(n, a=1, b=0):
    # snapshot(printstack=True)
    if n == 0:
        return a
    # equivalent to   return Fib2(n - 1, a + b, a)
    # (Not examinable: note how Python doesn't do tail call optimisation.
    #  To see, try replacing the three lines below with the commented-out
    #  return statement above. Notice how the stack grows on each recursive
    #  call. Tail-call optimisation avoids growing the stack in this way.)
    r = Fib2(n - 1, a + b, a)
    # snapshot(printstack=True)
    return r

# clear_frames()
print(Fib2(4))
# show_animation(size=[10,5])