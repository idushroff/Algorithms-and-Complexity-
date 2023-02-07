class node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self):
        return "<a node whose val is %s>" % str(self.val)


# The find function finds the value in the LinkedList and returns corresponding pointer,
# returns None if not found
def find(head, value):
    # head is a linked list
    # p points into head
    p = head
    # snapshot()
    while p != None:
        if p.val == value:
            return p
        p = p.next
        # snapshot()
    return None


# Creation of Linked list
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
# show_animation(size=[10, 5])