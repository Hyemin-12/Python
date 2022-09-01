# import as 문으로 모듈 이름 변경 가능
# 변경한 경우 원래 모듈 이름으로는 접근 불가능
import repeater as r

repeater = "반복"
print(repeater) # 반복

s = input("반복할 문자를 입력하세요 : ")
n = input("반복 횟수를 입력하세요 : ")

r.repeat(s, int(n))
r.repeat(s)
r.once(s)