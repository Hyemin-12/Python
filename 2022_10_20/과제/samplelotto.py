import random

def lotto():
    res = random.sample(range(1, 45), 6)
    res.sort()
    print(res)

lotto()
