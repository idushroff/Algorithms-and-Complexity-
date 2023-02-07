# an array of lists
G = [[1, 3],
     [0, 3],
     [3],
     [0, 1, 2]]


def each_edge(G):
    # G is a graph (adjacency list)
    for u in range(len(G)):  # u indexes nodes of G
        for v in G[u]:  # v indexes nodes of G
            msg = "There is an edge from node {} to node {}".format(u, v)
            # snapshot()
            print(msg)


# clear_frames()
each_edge(G)
# show_animation(size=[12, 7])


def degree_of_node(G, u):
    return len(G[u])


# complexity O(|V|)
def has_edge(G, u, v):
    for w in G[u]:
        if w == v:
            return True
    return False


# complexity O(|path|*|V|)
def is_path(G, path):
    # G is a graph (adjacency list)
    if len(path) > 1:
        s = path[0]  # s indexes nodes of G
        d = path[1]  # d indexes nodes of G
        # snapshot()
        return has_edge(G, s, d) and is_path(G, path[1:])
    else:
        return True


# clear_frames()
print(is_path(G, [1, 0, 3, 2]))
# show_animation(size=[14, 8])
