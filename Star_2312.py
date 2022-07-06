# 2312 최혜민

scores = input("점수 입력 : ")

li = scores.strip().split(" ")

# 점수대 구하기
cnt = [0, 0, 0, 0, 0]

for score in li:
    if int(score) >=90: cnt[0] += 1
    elif int(score) >= 80: cnt[1] += 1
    elif int(score) >= 70: cnt[2] += 1
    elif int(score) >= 60: cnt[3] += 1
    else: cnt[4] += 1

print("90점 이상\t : ", "*"*cnt[0])
print("80점 대\t\t : ", "*"*cnt[1])
print("70점 대\t\t : ", "*"*cnt[2])
print("60점 대\t\t : ", "*"*cnt[3])
print("60점 미만\t : ", "*"*cnt[4])

# 최고, 최저점수 구하기
max = 0
min = li[0]

for score in li:
    if(int(score) > max):
        max = int(score)
    if(int(score) < int(min)):
        min = int(score)

print("최고점수 : ", max)
print("최저점수 : ", min)