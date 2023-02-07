def DFS(G):
    # G is a graph (adjacency matrix), G is a matrix
    global count
    mark = [0] * len(G)
    count = 0
    for v in range(len(G)): # v indexes nodes of G, v indexes rows of G
        # snapshot(printstack=True)
        if mark[v] == 0:
            DFSExplore(v, G, mark)


def DFSExplore(v, G, mark):
    global count
    # G is a graph (adjacency matrix), G is a matrix
    # v indexes nodes of G, v indexes rows of G
    count = count + 1
    mark[v] = count
    for w in range(len(G)): # w indexes nodes of G, w indexes cols of G
        # snapshot(printstack=True)
        if G[v][w] != 0:
            if mark[w] == 0:
                DFSExplore(w, G, mark)


# clear_frames()
G = [[0, 1, 0, 1],
     [1, 0, 0, 1],
     [0, 0, 0, 1],
     [1, 1, 1, 0]]
print(DFS(G))
# show_animation(size=[14,14])