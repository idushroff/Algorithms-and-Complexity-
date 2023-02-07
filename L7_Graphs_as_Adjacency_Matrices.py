G = [[0, 1, 0, 1],
     [1, 0, 0, 1],
     [0, 0, 0, 1],
     [1, 1, 1, 0]]


def each_edge(G):
    # G is a matrix, G is a graph (adjacency matrix)
    for u in range(len(G)): # u indexes rows of G, u indexes nodes of G
        for v in range(len(G)): # v indexes cols of G, v indexes nodes of G
            # snapshot()
            if G[u][v] != 0:
                print("There is an edge from node {} to node {}".format(u,v))

# clear_frames()
each_edge(G)
# show_animation(size=[10,10])


def degree_of_node(G,u):
    # G is a graph (adjacency matrix), G is a matrix
    # u indexes nodes of G, u indexes rows of G
    degree = 0
    for v in range(len(G)): # v indexes nodes of G, v indexes cols of G
        # snapshot()
        if G[u][v] != 0:
            degree += 1
    return degree

# clear_frames()
print(degree_of_node(G,3))
# show_animation(size=[10,8])


from collections import deque


def is_path(G,path):
    # G is a graph (adjacency matrix)
    if len(path) > 1:
        s = path[0] # s indexes rows of G, s indexes nodes of G
        d = path[1] # d indexes cols of G, d indexes nodes of G
        # snapshot()
        return G[s][d] != 0 and is_path(G,path[1:])
    else:
        return True

# clear_frames()
print(is_path(G,[1,0,3,2]))
# show_animation(size=[14,8])