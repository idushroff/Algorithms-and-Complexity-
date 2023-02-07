def BruteForceGCD(m, n):
    r = min(m, n)
    # snapshot()
    while r != 0:
        if m % r == 0 and n % r == 0:
            return r
        r = r - 1
        # snapshot()


# clear_frames()
m = 24
n = 60
print(BruteForceGCD(m, n))
# show_animation(size=[8, 3])

