# The function computes GCD of two integer values using Euclid's fomula
def EuclidGCD(m,n):
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
print(EuclidGCD(m,n))
# show_animation(size=[8,3])


"""NOTE: the Bruteforce GCD takes longer than Euclids GCD. 
This is according to the code in 01.ipynb."""