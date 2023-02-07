def Fib(n):
    # snapshot(printstack=True)
    if n == 0:
        return 1
    if n == 1:
        return 1
    # equivalent to     return Fib(n - 1) + Fib(n - 2)
    a = Fib(n - 1)
    # snapshot(printstack=True)
    b = Fib(n - 2)
    # snapshot(printstack=True)
    return a + b

# clear_frames()
print(Fib(21-1))
# show_animation(size=[10,6])

"""
Rosalind Problem: 
The Fibonacci numbers 0,1,1,2,3,5,8,13,21,34,..
are generated by the following simple rule
*note: the index position of 6 corresponds to 8 in that list of fibonacci numbers
"""