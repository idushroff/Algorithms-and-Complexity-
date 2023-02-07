# Push function adds the value 'x' at the top 'st' of the Stack and returns the updated top 'st'
def push(st,x):
    # st is a linked list
    # elt is a linked list of single node
    elt = node(x)
    snapshot()
    elt.next = st
    st = elt
    elt = None
    snapshot()
    return st

# Creation of LinkedList, the LinkedList represents the stack,
# firstnode is the start 'st' or head of the linkedlist that works as the top of the stack
firstnode = node(2)
secondnode = node(3)
thirdnode = node(5)
forthnode = node(7)
firstnode.next = secondnode
secondnode.next = thirdnode
thirdnode.next = forthnode

clear_frames()
firstnode = push(firstnode,5) # Adding 5 at the top of stack
firstnode = push(firstnode,9) # Adding 9 at the top of stack
show_animation(size=[10,5])