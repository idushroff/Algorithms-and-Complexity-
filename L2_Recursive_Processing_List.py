# The find function finds the value in the LinkedList and returns corresponding pointer,
# returns None if not found
def find(p, value):
    # p is a linked list
    # snapshot()
    if p == None:
        return p
    elif p.val == value:
        return p
    else:
        return find(p.next,value)

# Creation of the LinkedList
firstnode = node(2)
secondnode = node(3)
thirdnode = node(5)
forthnode = node(7)
firstnode.next = secondnode
secondnode.next = thirdnode
thirdnode.next = forthnode

# clear_frames()
a = find(firstnode, 5)
print(a)
# show_animation(size=[10,4])