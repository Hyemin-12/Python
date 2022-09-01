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

# # 중첩 if문
# x = int(input("숫자 입력 : "))

# if x > 0:
#     print("plus")
#     if x % 2 == 0:
#         print("even")
#     else:
#         print("odd")
# else:
#     print("minus")
#     if x % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# # 리스트 안의 리스트 출력(2차원 배열과 유사)
# table = [["월", "화", "수"], [100, 200, 300]]
# for row in table:
#     for col in row:
#         print(str(col) + " ") # 공백과 연결 시키기 위해 문자열로 바꿔주는 str 사용(int형 col -> str형 col)
#     print()

lst = ["apple", 100, 3.14]

for item in lst:
    print(item, type(item))