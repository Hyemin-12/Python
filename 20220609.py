# d = {"apple":100, "orange":200, "banana":300}
# for key in d:
#     print(key, d[key])
# # 이렇게 함수를 사용하여 한번에 키, 값 출력 가능(이 방법을 더 많이 사용)
# # for k, v in d.items():
# #     print(k, v)

# a = [(1, 2), (3, 4), (5, 6)]
# for (first, last) in a:
#     print(first + last)

# # 별찍기
# for i in range(1, 10+1):
#     for j in range(1, i+1):
#         print("*", end = '') 
#     print("")

# # 파이썬에서는 이렇게 하는게 가능
# # for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
# #     print("*" * i)

# # 완전 줄일 수 있음
# # for i in range(1, 11):
# #     print("*" * i)

# #구구단
# for dan in range(2, 5+1):
#     for i in range(1, 9+1):
#         print("{} x {} = {}".format(dan, i, dan*i))

#피라미드 별찍기
# for i in range(1, 10 + 1, 2):
#     print(" " * (9-i), end='')
#     print("* " * i)

# for i in range(1,  5+1):
#     print("  " * (5-i), end='')
#     print("* " * (i*2-1))

# 리스트 요소 출력
# table = [["월", "화", "수"], [100, 200, 300]]
# for row in table:
#     for col in row:
#         print(str(col) + " ")
#     print()

# # break 문
# for i in range(1, 9+1):
#     if i == 7:
#         break
#     print("2 x {} = {}".format(i, 2*i))

# # continue 문
# for i in range(1, 9+1):
#     if i % 2 == 0:
#         continue
#     print("2 x {} = {}".format(i, 2*i))

# while 문
# # 무한반복(Ctrl + C로 중지 가능)
# x = 3
# while x < 6:
#     print(x)

# x = 3
# while x < 6:
#     print(x)
#     x += 1

# echo = input()
# while echo != "exit":
#     print(echo)
#     echo = input()

# #이렇게 변경 가능
# echo = input()
# while True:
#     if echo == "exit":
#         break
#     print(echo)
#     echo = input()

# # range()
# print(list(range(10)))
# print(list(range(5, 10)))
# print(list(range(10, 0, -1))) # 감소는 이렇게 쓰면 됨
# print(list(range(10, 20, 2)))

# # 리스트 함축
# # for문을 사용하여 리스트 생성하기
# array = []
# for i in range(1, 10, 2):
#     array.append(i*i)
# print(array)

# # 줄여서 쓸 수 있음
# array = [i*i for i in range(1, 10, 2)]
# print(array)

# # 조건도 붙일 수 있음
# array = [i*i for i in range(1, 10, 2) if i*i > 30]
# print(array)

# # 리스트에 원래 있던 값을 수정 가능
# lst = [1, 2, 3, 4, 5]
# print(lst)
# lst = [i**2 for i in lst]
# print(lst)

# # 이렇게 사용 가능(문자열 길이 추출)
# test = ("apple", "banana", "orange")
# test_len = [len(i) for i in test]
# print(test_len)

# # 이렇게 대문자로 바꾸기 가능
# d = {100:"apple", 200:"banana", 300:"orange"}
# d_upper = [v.upper() for v in d.values()]
# print(d_upper)

# 반복문 작성 시 도움이 되는 함수
# filter(함수명(None),반복이 가능한 자료형)

# # 전달 받은 함수가 없을 때(None)
# lst = [10, 25, 30]
# iteL = filter(None, lst)
# for item in lst:
#     print("item:{0}".format(item))

# # 함수가 있을 때
# def getBiggerThan20(i):
#     return i > 20
# lst = [10, 25, 30]
# iteL = filter(getBiggerThan20, lst)
# for item in iteL:
#     print("item:{0}".format(item))

# #입력받은 양의 정수가 3, 5, 8의 배수인지 알려주는 프로그램
# n = int(input("수 입력 : "))

# if n % 3 == 0:
#     print("{}은(는) 3의 배수이다.".format(n))
# elif n % 5 == 0:
#     print("{}은(는) 5의 배수이다.".format(n))
# elif n % 8 == 0:
#     print("{}은(는) 8의 배수이다.".format(n))
# else:
#     print("{}은(는) 어느 배수도 아니다.".format(n))