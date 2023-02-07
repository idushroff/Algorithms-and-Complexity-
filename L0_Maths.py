
"""for questions where you have to find the minimum
height for a binary search tree containing x (in this case 619) nodes: """

# floor(log2(n)) = formula for finding the minimum height for a bst ...

import math
# the math.floor() method returns _
# the math.ceil() method returns _
# log(a, base)

ans = math.floor(math.log(619, 2))
print(ans)

# note % is the mod function in python
g = 60 % 11
b = (60 % 7)
h = 7 - b
print(g, b, h)

print(math.floor(9/2))