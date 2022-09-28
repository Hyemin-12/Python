import random

origin = [0, 0, 0]

# 데이터 생성
for i in range(0, 3):
    origin[i] = random.randint(0, 9)

    for j in range(0, i):
        while origin[i] == origin[j]:
            origin[i] = random.randint(0, 9)

cnt = 0

while True:
    # user 데이터 입력
    myData = list(map(int, input(f'{cnt+1}회 숫자 입력 : ').split(' ')))
    cnt += 1

    # 판정
    # strike
    strike = 0

    for i in range(0, 3):
        if origin[i] == myData[i]:
            strike += 1
    print(strike, "strike")

    # ball
    ball = 0

    for i in range(0, 3): # origin
        for j in range(0, 3): # myData
                if i != j: # ball 처리, i == j strike에서 처리됨
                    if origin[i] == myData[j]:
                        ball += 1

    print(ball, "ball")
    print()

    if strike == 3:
        print(f"축하합니다. {cnt}회 만에 맞추었습니다!")
        break
    elif cnt == 10:
        print(f"실패입니다. {cnt}회가 되었습니다..")
        break