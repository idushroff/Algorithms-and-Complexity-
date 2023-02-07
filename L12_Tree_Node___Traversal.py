from queue import Queue

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def Height(T):
    if T is None:
        return -1
    else:
        return max(Height(T.left), Height(T.right)) + 1


T = Node(17)
T.left = Node(33)
T.left.left = Node(19)
T.left.right = Node(16)
T.left.right.left = Node(38)
T.left.right.right = Node(31)
T.right = Node(48)
T.right.left = Node(11)
T.right.right = Node(14)


def PreorderTraverse(T):
    # T is a tree
    if T is not None:
        # node is currently being traversed
        node = T.val
        # snapshot(printstack=True)
        PreorderTraverse(T.left)
        # snapshot(printstack=True)
        PreorderTraverse(T.right)
        # snapshot(printstack=True)

# clear_frames()
PreorderTraverse(T)
# show_animation(size=[12,10])


def InorderTraverse(T):
    if T is not None:
        InorderTraverse(T.left)
        node = T.val
        # snapshot()
        InorderTraverse(T.right)

# clear_frames()
PreorderTraverse(T)
# show_animation(size=[12,10])


def PostorderTraverse(T):
    if T is not None:
        PostorderTraverse(T.left)
        PostorderTraverse(T.right)
        node = T.val
        snapshot()

# clear_frames()
PreorderTraverse(T)
# show_animation(size=[12,10])


def LevelorderTraverse(T):
    Q = Queue()
    Q.put(T)
    while not Q.empty():
        # X is a tree
        X = Q.get()
        # node is currently being traversed
        node = X.val
        snapshot()
        if X.left is not None:
            Q.put(X.left)
        if X.right is not None:
            Q.put(X.right)


# clear_frames()
PreorderTraverse(T)
# show_animation(size=[12, 10])