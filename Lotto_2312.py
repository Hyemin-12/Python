# 2312 최혜민

import random


def func_lotto():
    se = set()
    cnt = 0

    while True:
        se.add(random.randint(1, 45))
        
        if len(se) == cnt+1:
            cnt+=1

        if cnt == 6:
            break
        
    return list(se)


for i in range(1, 10+1):
    result = func_lotto()

    result.sort()

    print("당첨번호 : ", end='')

    for num in result:
        print(num, "", end='')
        
    print()

