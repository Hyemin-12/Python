# # 반복문
# for a in range(2, 10): # 변수 a의 범위 => 2 <= x < 10
#     print('{0}단'.format(a)) # 문장이 여러개라도 중괄호로 구분X, 들여쓰기로 구분함
#     for b in range(1, 10): # 반복문, IF문 뒤에는 콜론(:)을 붙임
#         print('{0} x {1} = {2:2}'.format(a, b, a * b)) #{2:2} => 두자리로 맞춰줌

# # 서식문자
# # %s(문자열), %d(정수), %f(실수), %o(8진수), %x(16진수), %%(문자 %표현)
# # 이렇게 씀
# num = 50
# s = 'My age %d' %num
# print(s)

# # %기호로 문자열 출력
# names = ['Kim', 'Park', 'Lee']
# for name in names: # 대충..이렇게 리스트를 돌림
#     print('My name is %s' %name)
# # %기호로 정수 출력
# money = 10000
# s2 = 'give me %d won' %money
# print(s2)
# # %기호로 실수 출력
# d = 3.141592
# print('value %f' %d)

# #포매팅 해야 할 값이 두 개 이상인 경우 => ()를 이용함
# from turtle import left


# s1 = 'My name is %s. Age : %d' %('mirim', 100)
# print(s1)
# #출력해야 할 값이 점점 많아질수록
# age = 78
# money = 20000
# name = 'Jang'
# weight = 63.12
# etc = 'abcde'
# s2 = 'My name is %s, Age : %d, weight : %f, money : %d, ect : %s' %(name, age, weight, money, etc)
# print(s2)

# # 문자열 포매팅
# # f-string => f'문자열 {변수} 문자열'
# month = 1
# while month <= 12:
#     print(f'2022년 {month}월') # 걍 냅다 변수를 집어넣음
#     month = month + 1

# s = 'coffee'
# n = 5
# result1 = f'저는 {s}를 좋아합니다. 하루 {n}잔 마셔요.'
# print(result1)

# # f-string 왼쪽 정렬
# s1 = 'left'
# result1 = f'|{s1:<10}|' # 10칸 안에서 왼쪽으로 정렬
# print(result1)
# #f-string 가운데 정렬
# s2 = 'mid'
# result2 = f'|{s2:^10}|' # ||는 그냥 정렬 맞춰줬는지 확인하는 용도(굳이 쓸 필요X)
# print(result2)
# #f-string 오른쪽 정렬
# s3 = 'right'
# result3 = f'|{s3:>10}|'
# print(result3)

# #f-string으로 중괄호 출력
# num = 10
# result = f'my age{{{num}}}, {{num}}' # 중괄호 세 개 => {10}, 중괄호 두 개 => {num} 
# print(result)

# f-string과 딕셔너리
d = {'name':'Mirim', 'gender':'female', 'age':18} # 키와 값을 저장 
result = f'my name {d["name"]}, gendet{d["gender"]}, age {d["age"]}' # d => 키과 값을 쌍으로 출력 가능
print(result)

#f-string과 리스트
n = [100, 200, 300] # 배열과 비슷, 값만 저장
print(f'list : {n[0]}, {n[1]}, {n[2]}')

for v in n: # 리스트 n을 순회
    print(f'list with for : {v}')

# len() => 문자열의 길이 리턴
strB = "파이썬 연습"
print(len(strB)) # 한글도 한글자씩 쳐줌(아스키 코드는 두개씩 쳐줌;;)

