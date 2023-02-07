# The function computes GCD of two integer values using Euclid's formula
def EuclidGCD(m, n):
    # snapshot()
    while n != 0:
        r = m % n
        m = n
        n = r
        # snapshot()
    return m

# clear_frames()
m=24
n=60
gcd = EuclidGCD(m, n)
print(gcd)
# show_animation(size=[3,3])