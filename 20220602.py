# 거짓
# 정수 계열의 0
# 실수 계열의 0.0
# 시퀀스 계열의 (), [], {}
# ""(공백 아님)
# None
# 이 외에는 모두 참
# print(bool(True))
# print(bool(False))
# print(bool(0))
# print(bool(3))
# print(bool(""))
# print(bool("test"))
# print(bool([]))
# print(bool([1, 2, 3]))

# 중첩 if문
x = int(input("숫자 입력 : "))

if x > 0:
    print("plus")
    if x % 2 == 0:
        print("even")
    else:
        print("odd")
else:
    print("minus")
    if x % 2 == 0:
        print("even")
    else:
        print("odd")
