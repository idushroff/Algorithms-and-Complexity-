# simulate a queue using Python lists
class Queue:
    def __init__(self):
        self._items = []

    def empty(self):
        return (len(self._items) == 0)

    def enqueue(self, v):
        self._items.append(v)

    def dequeue(self):
        h = self._items[0]
        self._items = self._items[1:]
        return h

    def __str__(self):
        return str(self._items)


def BFS(G):
    # G is a matrix, G is a graph (adjacency matrix)
    mark = [0] * len(G)
    count = 0
    Q = Queue()
    for v in range(len(G)):  # v indexes rows of G, v indexes nodes of G
        # snapshot()
        if mark[v] == 0:
            count = count + 1
            mark[v] = count
            Q.enqueue(v)
            while not Q.empty():
                # snapshot()
                u = Q.dequeue()
                # u indexes rows of G, u indexes nodes of G
                for w in range(len(G)):
                    # w indexes cols of G, w indexes nodes of G
                    # snapshot()
                    if G[u][w] != 0:
                        if mark[w] == 0:
                            count = count + 1
                            mark[w] = count
                            Q.enqueue(w)


# clear_frames()
print(BFS(G))
# show_animation(size=[15, 20])