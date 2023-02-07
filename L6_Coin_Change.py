"""How many ways can you make (coin) change?"""

import random

def Ways(amount, denominations):
    snapshot(printstack=True)
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if len(denominations) == 0:
        return 0
    d = random.sample(denominations, 1)[0]
    # equivalent to     return Ways(amount - d, denominations) + Ways(amount, denominations.difference([d]))
    a = Ways(amount - d, denominations)
    b = Ways(amount, denominations.difference([d]))
    return a + b

# clear_frames()
# the animation can't handle this many steps so we use a smaller problem instead to animate
#print(Ways(400, set([5, 10, 20, 50, 100, 200])))
print(Ways(50, set([5, 10, 20])))
print("Ways calculated. Rendering the animation will take a while...")
# show_animation(size=[10,7])