# 2312 최혜민

import random


def func_lotto():
    li = []
    for i in range(1, 6+1):
        li.append(str(random.randint(1, 45)))

    return li


for i in range(1, 10+1):
    result = func_lotto()
    result.sort

    print("당첨번호 : ", " ".join(result))
