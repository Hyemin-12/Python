# a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# print("원본 : ", a)
# b = set(a)
# c = list(b)
# print("중복제거 후 : ", c)

# a = b = [1, 2, 3] # 얕은 복사(같은 주소 참조)
# print(hex(id(a)))
# print(hex(id(b)))
# a[1] = 4
# print(a) # [1, 4, 3]
# print(b) # [1, 4, 3]
# print(hex(id(a)))
# print(hex(id(b)))

# # bin() : 이진수로 표현하는 함수
# # 2진수로 표현
# print(bin(0b1010))
# print(bin(0b1010 & 0b0110))
# print(bin(0b1010 | 0b0110))
# print(bin(0b1010 ^ 0b0110))
# print(bin(~0b1010)) 
# # 10진수로 표현
# print(0b1010)
# print(0b1010 & 0b0110)
# print(0b1010 | 0b0110)
# print(0b1010 ^ 0b0110)
# print(~0b1010)

# print(bin(0b1010 << 2)) # *2의 n승
# print(0b1010 << 2)
# print(bin(0b1010 >> 2)) # /2의 n승
# print(0b1010 >> 2)


# a = 3
# if a > 5:
#     print("테스트입니다.")
#     print("a는 10입니다.")
# else:
#     print("else문입니다.")

# # input("입력하라고 설명하는 문장") 입력 함수 -> 문자열 입력
# x = int(input("숫자 입력 : ")) # 문자열형이므로 int로 변환
# # print(x)
# # print(type(x))
# if x % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")


# password = input("문자 입력 : ")
# if password == "암호": # 문자열 비교
#     print("암호이다.")
# else:
#     print("암호가 아니다.")

# money = 1
# if money:
#     print("택시를")
# print("타고")
# print("가자")

# money = 2000
# if money >= 3000:
#     print("택시를 타고 가라")
# else:
#     print("걸어 가라")

# pocket = ['paper', 'cellphone', 'money', 'card']
# if 'money' in pocket: # in 연산자로 값이 들어있는지 확인
#     print("택시를 타고 가라")
# else:
#     print("걸어 가라")

# pocket = ['paper', 'cellphone', 'money', 'card']
# if 'money' in pocket:
#     pass # 안에 쓸 내용이 없을 때
# else:
#     print("카드를 꺼내라")
# print("수행 완료")

# pocket = ['paper', 'cellphone', 'money', 'card']
# if 'money' not in pocket:
#     print("카드를 꺼내라")
# print("수행 완료")

# pocket = ['paper', 'cellphone', 'money', 'card']
# if 'money' in pocket or 'card' in pocket:
#     print("택시를 타라")
# else:
#     print("걸어 가라")

saying = "Life is too short, you need python"

if "wife" in saying : print("wife")
elif "python" in saying and "you" not in saying : print("python")
elif "shirt" not in saying : print("shirt")
elif "need" in saying : print("need")
else : print("none")