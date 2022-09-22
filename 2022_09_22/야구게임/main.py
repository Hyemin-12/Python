import random

origin = [0, 0, 0]

# 데이터 생성
for i in range(0, 3):
    origin[i] = random.randint(0, 9)

    for j in range(0, i):
        while origin[i] == origin[j]:
            origin[i] = random.randint(0, 9)
            
    print(origin[i], end='\t')
print()

# user 데이터 입력
myData = [0, 0, 0]
for i in range(0, 3):
    myData[i] = int(input()) # 숫자 옆으로 입력

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
