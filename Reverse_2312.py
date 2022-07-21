# 2312 최혜민

str = input("영문자 입력 : ")

li = list(str)

for i in range(0, len(str)//2):
    li[i], li[-i-1] = li[-i-1], li[i]
    print(li)

print("거꾸로 출력 :", "".join(li))