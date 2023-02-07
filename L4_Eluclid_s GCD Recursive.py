# The function computes GCD of two integer values using Euclid's formula
def EuclidGCDRecur(m,n):
    # snapshot()
    if n == 0:
        return m
    return EuclidGCDRecur(n,m % n)

# clear_frames()
m=24
n=60
gcd = EuclidGCDRecur(m,n)
print(gcd)
# show_animation(size=[5,3])