def ClosestPair(nodes):
    min = float("inf")
    n = len(nodes)
    for i in range(0, n - 1):
        xi, yi = nodes[i]
        for j in range(i + 1, n):
            xj, yj = nodes[j]
            d = ((xi - xj) ** 2 + (yi - yj) ** 2) ** 0.5
            # snapshot()
            if d < min:
                min = d
                pi = i
                pj = j
    # snapshot()
    return pi, pj

# clear_frames()
N = [(1, 3), (5, 8), (-2, 7), (-9, 0), (-4, -6)]
print(ClosestPair(N))
# show_animation(size=[18,5])