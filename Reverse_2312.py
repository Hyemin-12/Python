# 2312 최혜민

str = input("영문자 입력 : ")

li = list(str)

for i in range(0, int(len(str)/2)):
    li[i], li[len(str) - 1 - i] = li[len(str) - 1 - i], li[i]

print("거꾸로 출력 : ", "".join(li))