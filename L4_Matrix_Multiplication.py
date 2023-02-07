# The function multiplies matrix A and matrix B and return the result matrix C
def matrix_mul(A, B, n):
    # A is a matrix, B is a matrix, C is a matrix
    C = [ [ 0 for i in range(n) ] for j in range(n) ]
    # snapshot()

    # iterate through rows of A
    for i in range(len(A)):  # i indexes rows of A, i indexes rows of C
        # iterate through columns of B
        for j in range(len(B[0])):  # j indexes cols of B, j indexes cols of C
            # iterate through cols of A
            for k in range(len(B)): # k indexes cols of A, k indexes rows of B
                C[i][j] += A[i][k] * B[k][j]
                # snapshot()
    return C


# clear_frames()

# The 2x2 matrix
# |    5    7  |
# |    3    4  |
A = [[5, 7], [3, 4]]

B = [[8, 2], [9, 6]]
n = 2
res = matrix_mul(A, B, n)
# show_animation(size=[10,7])