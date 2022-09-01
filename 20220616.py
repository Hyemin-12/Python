# # 입력받은 양의 정수가 3, 5, 8의 배수인지 알려주는 프로그램(공배수 포함)
# n = int(input("수 입력 : "))

# if n % 3 == 0 or n % 5 == 0 or n % 8 == 0:
#     if n % 3 == 0:
#         print("{}은(는) 3의 배수이다.".format(n))
#     if n % 5 == 0:
#         print("{}은(는) 5의 배수이다.".format(n))
#     if n % 8 == 0:
#         print("{}은(는) 8의 배수이다.".format(n))
# else:
#     print("{}은(는) 어느 배수도 아니다.".format(n))

# # 연간 근로소득에 대한 소득세 계산 프로그램
# money = int(input("근로소득 입력 : "))

# if money <= 20000000:
#     percent = 0.05
# elif money <= 40000000:
#     percent = 0.15
# elif money <= 80000000:
#     percent = 0.25
# else:
#     percent = 0.4

# print("소득세 : {}".format(int(money * percent)))

# # 연봉과 근무평가등급을 입력받아 연봉 인상액과 새 연봉을 계산하는 프로그램
# money = int(input("현 연봉을 입력하세요 : "))
# rank = input("근무평가등급을 입력하세요 : ")

# if rank == "우수":
#     plus = 0.06
# elif rank == "보통":
#     plus = 0.04
# elif rank == "불량":
#     plus = 0.02
# else:
#     print("입력 오류") 
#     exit()

# print("연봉인상액 : {}".format(int(money * plus)))
# print("새 연봉 : {}".format(int(money + (money * plus))))

# 입력 받은 수가 소수인지 판별하는 프로그램
# n을 2~n까지 수와 나눔 -> 나머지가 0인 숫자-> 그 숫자가 n이랑 다르면 소수 아님, n이랑 같으면 소수
n= int(input("수 입력 : "))

if n > 1: # n이 1보다 클 때
    for i in range(2, n+1): # n을 2~n까지의 수와 나누기
        if(n % i == 0): # 나머지가 0일 때
            if(n == i): # i가 n과 같으면
                print("{}은(는) 소수입니다.".format(n))
                break # 멈추기
            else: # i가 n과 다르면
                print("{}은(는) 소수가 아닙니다.".format(n))
                break # 멈추기
else: print("{}은(는) 소수가 아닙니다.".format(n))  

# # 함수
# def times(a, b):
#     return a * b
# print(times) # 함수의 주소 출력(파이썬은 함수도 일종의 객체로 봄)
# print(times(10, 5)) # 함수 호출

# # 파이썬은 함수를 객체 취급하기 때문에 = 복사 가능
# myTimes = times
# print(times)
# print(times(10, 5))
# print(myTimes) # times와 주소 같음
# print(myTimes(10, 5)) # 호출 가능(times와 똑같은 기능 수행)

# # 절댓값
# print(10, "의 절댓값 : ", abs(10))
# print(-10, "의 절댓값 : ", abs(-10))

# # 10진수 -> 2진수 변환
# print(128, "의 2진수 : ", bin(128))
# print(255, "의 2진수 : ", bin(255))
# # 10진수 -> 8진수 변환
# print(7, "의 8진수 : ", oct(7))
# print(8, "의 8진수 : ", oct(8))
# # 10진수 -> 16진수 변환
# print(15, "의 16진수 : ", hex(15))
# print(16, "의 16진수 : ", hex(16))

# # 연산
# numbers = [1, 5, -2, 0, 6]
# print(numbers, "중 가장 큰 값은 ", max(numbers))
# print(numbers, "중 가장 작은 값은 ", min(numbers))
# print(numbers, "합계는 ", sum(numbers))
# print("2의 10승은 ", pow(2, 10))

# # 반올림
# pi = 3.56789
# print(pi, "의 소수점 1자리 반올림은 ", round(pi))
# print(pi, "의 소수점 1자리 반올림은 ", round(pi, 0))
# print(pi, "의 소수점 2자리 반올림은 ", round(pi, 1))
# print(pi, "의 소수점 3자리 반올림은 ", round(pi, 2))
# print(pi, "의 소수점 4자리 반올림은 ", round(pi, 3))

# # 문자열 관련 내장 함수
# user_name = input("이름은? ")
# user_age = input("나이는? ")
# print(user_name + "님! 나이는 " + str(user_age) + "세군요!")
# say = "{0}님! 나이는 {1}세군요! {1}세라니 놀라워요!"
# print((say.format(user_name, user_age)))

# pi = "3.14159"
# print("문자열 출력 : ", pi)
# print("실수 변환 출력 : ", float(pi))
# print(float(pi) + 100)
# year = "2018"
# print("올해 연도 : ", year)
# print("100년 뒤는 ", int(year) + 100, "년입니다.")
# print("숫자를 문자열로 변환하려면 str()을 이용합니다.")
# print("올해는 " + str(year) + "년입니다.")

# 리스트 관련 내장 함수
# list = ['d', 'c', 'a', 'b']
# list.reverse() # 해당 리스트 자체를 변경
# # print("리스트 항목 순서 뒤집기", list)
# # list.sort() # 해당 리스트 자체를 변경
# print("리스트 항목 정렬하기", list)
# list.sort(reverse=True) # 역정렬(해당 리스트 자체를 변경)
# print("리스트 항목 역정렬하기", list)
# for index, value in enumerate(list): # enumerate => 인덱스 값(0부터 시작)과 항목을 튜플 형태로 리턴
#     print("인덱스", index, "위치의 값은 ", value)

# str = "나는 문자열"
# print(str)
# n = 3
# # 내장 함수명과 똑같은 이름의 변수를 만들면 -> 해당 함수는 변수로 처리됨 -> 사용 불가
# print(str(n))

# # random 함수
# import random

# # 처음 시작
# n = random.randint(1, 6) # 1에서 6까지 정수 중 하나를 뽑는다
# print("결과 : ", n)
# n = random.randint(1, 6)
# print("결과 : ", n)
# n = random.randint(1, 6)
# print("결과 : ", n)

# # 함수 작성
# import random


# def rolling_dice():
#     n = random.randint(1, 6)
#     print("6면 주사위 굴린 결과 : ", n)

# rolling_dice()
# rolling_dice()
# rolling_dice()