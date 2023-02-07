# Push function adds the value 'x' at the top 't' of the Stack 'A' and returns the updated top 't'
def push(A, t, x):
    # A is an array
    # t indexes A
    # snapshot()
    A[t] = x
    t += 1
    # snapshot()
    return t


A = [6, 9, 2, 3, 7, -1, -1, -1]     # Represents the stack
top = 5     # Represents the top of the stack
# clear_frames()
top = push(A, top, 5)     # Adding 5 at the top of stack
top = push(A, top, 12)     # Adding 12 at the top of stack
# show_animation(size=[6,5])