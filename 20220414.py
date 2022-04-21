# # 튜플(Tuple)
# # 순서가 존재
# # 값 변경 불가(읽기 전용)
# # ( )로 묶어서 표현함
# # 데이터를 묶어서 한번에 전달하거나 여러개의 값을 묶어서 반환할 경우에 사용함
# from cgi import print_arguments


# t = (1, 2, 3)
# print(type(t))

# # 튜플이 주로 사용되는 경우
# # -함수에서 하나 이상의 값을 리턴하는 경우
# def calc(a, b):
#     return a+b, a*b # 파이썬은 하나 이상 리턴이 가능하다
# x, y = calc(5, 4) # 리턴 값이 하나 이상일 경우에는 ,를 이용하여 변수에 저장한다
# print(x, y)

# # -문자열 포매팅
# print("id : %s, name : %s" % ("kim", "김유신")) # %를 이용하여 튜플 사용

# # -튜플에 있는 값을 함수 인수로 사용하는 경우
# args = (3, 4)
# print(calc(*args)) # *는 포인터 같은 역할

# #세트(Set)
# # 유일한 값의 모임이며 순서는 없다
# a = {1, 2, 3, 4}
# b = {3, 4, 4, 5}
# print(a)
# print(b) # 중복된 값은 빼고 출력
# print(type(a))
# print(type(b))

# print(a.union(b)) # 합집합
# print(a.intersection(b)) #교집합
# print(a.difference(b)) #차집합

# # 이렇게 써도 결과는 똑같다
# print(a | b)
# print(a & b)
# print(a - b)

# #리스트, 세트, 튜플은 생성자 list(), set(), tuple()을 이용해 변환 가능

# a = set((1, 2, 3, 2)) # 튜플 -> 세트로 변환
# print(a)
# print(type(a))

# b = list(a) # 세트 -> 리스트
# print(b)
# print(type(b))

# c = tuple((b)) # 리스트 -> 튜플
# print(c)
# print(type(c))

# #딕셔너리
# # -임의의 객체 집합적 자료형식
# # -자료의 순서를 가지지 않음
# # -키를 통해 값을 찾음

# d = dict(a = 1, b = 2, c = 3) # 키 = 값
# print(d)
# print(type(d))

# colors = {"apple" : "red", "banana" : "yelllow"}
# print(colors)

# # 딕셔너리에 키, 값 추가할 때
# colors["cherry"] = "red" # 딕셔너리이름[키] = 값 
# print(colors)

# # 포문으로 딕셔너리 안의 값을 하나씩 출력가능
# for item in colors.items(): # 튜플 형태로 출력됨
#     print(item)

# for k, v in colors.items(): # 그냥...하나씩 출력됨
#     print(k, v)

# print(colors)
# del colors["cherry"] # 삭제
# print(colors)
# colors.clear() # 모두 삭제
# print(colors)

# device = {"아이폰" : 5, "아이패드" : 10, "윈도우 타블렛" : 20}
# device["아이맥"] = 15
# device["아이폰"] = 6
# print(device) # 동일한 키가 있으면 그 키의 값만 덮어씌움
# del device["아이폰"] # 아이폰을 삭제함
# print(device)

# phone = {"kim" : "1111", "lee" : "2222", "park" : 3333}
# print(phone.keys()) # key만 출력
# print(phone.values()) # value만 출력
# print("park" in phone) # phone 안에서 park의 존재 여부
# print("moon" in phone)
# p = phone
# print(p) 

# d = {"a" : 100, "b" : 200, "c" : 300}

# for key in d.keys(): # 딕셔너리 안의 키를 순회
#     print(key)
# for value in d.values(): # 딕셔너리 안의 값을 순회
#     print(value)

# # bool
# # 참과 거짓을 나타내는 자료형
# # True나 False만 가짐
# isRight = False
# print(type(isRight))
# print(1 < 2)
# print(1 != 2)
# print(1 == 2)
# print(True and True and False)
# print(True or False or False)

# # 수치를 논리연산자에 사용하는 경우
# # -0은 False로 간주
# # -음수를 포함한 다른 값은 모두 True로 간주
# #문자열을 논리연산자에 사용하는 경우에도 ''만 False로 간주
# # 값이 없는 상태를 나타내는 None도 False로 간주
# print(bool(0))
# print(bool(-1))
# print(bool("test"))
# print(bool(None))
# print(bool(""))
# print(bool(" ")) # 공백도 True
# print(bool(''))
# print(bool(' '))

# mutable, immutable 객체
# mutable : 변경되는 객체(객체의 상태 변경 가능)
#   종류 : list, set, dictionary
# immutable : 변경되지 않는 객체(객체의 상태 변경 불가)
#   종류 : int, float, str, bool, tuple
# => 얕은 복사(Shallow Copy), 깊은 복사(Deep Copy)를 이해하기 위해서 필요

# # immutable
# print("immutable 객체")
# a = 99
# b = 99
# c = 99
# d = 99
# e = 99
# # 하나의 값(99)에 대한 주소가 다 똑같음
# # 하나의 immutable 값에 여러 개의 참조가 붙게 됨 
# print(hex(id(a)))
# print(hex(id(b)))
# print(hex(id(c)))
# print(hex(id(d)))
# print(hex(id(e)))

# # mutable
# print("\nmutable 객체")
# arr1 = [1, 2, 3]
# arr2 = [1, 2, 3]
# arr3 = [1, 2, 3]
# arr4 = [1, 2, 3]
# # 값이 같아도 주소가 다 다름
# # mutable은 값이 바뀔 수 있기 때문에 각각의 메모리를 할당해주는 게 관리에 용이
# print(hex(id(arr1)))
# print(hex(id(arr2)))
# print(hex(id(arr3)))
# print(hex(id(arr4)))

# # immutable
# print("=" * 50)
# print("immutable 객체 예제")
# print("=" * 50)
# print("1. int 값이 변경되면?")
# num1 = 99
# num2 = 99
# num3 = 99
# num4 = 99
# print(f"num1 값 : {num1} \t 주소 : {hex(id(num1))}")
# print(f"num2 값 : {num2} \t 주소 : {hex(id(num2))}")
# print(f"num3 값 : {num3} \t 주소 : {hex(id(num3))}")
# print(f"num4 값 : {num4} \t 주소 : {hex(id(num4))}")
# num1 += 1 # num1 값 증가
# num3 += 1 # num3 값 증가
# num4 += 10 # num4 값 증가
# print(f"num1 값 : {num1} \t 주소 : {hex(id(num1))}")
# print(f"num2 값 : {num2} \t 주소 : {hex(id(num2))}")
# print(f"num3 값 : {num3} \t 주소 : {hex(id(num3))}") # num1, num3처럼 바뀐 값이 같아도 주소가 같음
# print(f"num4 값 : {num4} \t 주소 : {hex(id(num4))}")

# print("\n2. string 값이 변경되면?")
# s1 = "BlockDMask"
# s2 = "BlockDMask"
# s3 = "BlockDMask"
# s4 = "BlockDMask"
# print(f"s1 값 : {s1} \t 주소 : {hex(id(s1))}")
# print(f"s2 값 : {s2} \t 주소 : {hex(id(s2))}")
# print(f"s3 값 : {s3} \t 주소 : {hex(id(s3))}")
# print(f"s4 값 : {s4} \t 주소 : {hex(id(s4))}")
# s1 = s1.replace('D', 'ZZZ')
# s2 = "BlockZZZMask"
# s4 = s4.upper()
# print(f"s1 값 : {s1} \t 주소 : {hex(id(s1))}")
# print(f"s2 값 : {s2} \t 주소 : {hex(id(s2))}") # string에서는 바뀐 값이 같아도 주소가 다를 수도 있음
# print(f"s3 값 : {s3} \t 주소 : {hex(id(s3))}")
# print(f"s4 값 : {s4} \t 주소 : {hex(id(s4))}")
# # => immutable 객체는 거의 같은 값을 참조함

# #mutable
# print("=" * 50)
# print("mutable 객체 예제")
# print("=" * 50)
# print("1. list 값이 변경되면?")
# arr1 = ['a', 'b', 77]
# arr2 = ['a', 'b', 77]
# arr3 = ['a', 'b', 77]
# arr4 = ['a', 'b', 77]
# print(f"arr1 값 : {arr1} \t 주소 : {hex(id(arr1))}")
# print(f"arr2 값 : {arr2} \t 주소 : {hex(id(arr2))}")
# print(f"arr3 값 : {arr3} \t 주소 : {hex(id(arr3))}")
# print(f"arr4 값 : {arr4} \t 주소 : {hex(id(arr4))}")
# arr1.append(10)
# arr2.append(10)
# #처음 주소랑 같음(arr1 = arr1)
# print(f"arr1 값 : {arr1} \t 주소 : {hex(id(arr1))}")
# print(f"arr2 값 : {arr2} \t 주소 : {hex(id(arr2))}")
# print(f"arr3 값 : {arr3} \t 주소 : {hex(id(arr3))}")
# print(f"arr4 값 : {arr4} \t 주소 : {hex(id(arr4))}")

# print("\n2. dictionary 값이 변경되면?")
# d1 = {'a' : 11, 'b' : 22, 'c' : 33}
# d2 = {'a' : 11, 'b' : 22, 'c' : 33}
# d3 = {'a' : 11, 'b' : 22, 'c' : 33}
# print(f"d1 값 : {d1} \t 주소 : {hex(id(d1))}")
# print(f"d2 값 : {d2} \t 주소 : {hex(id(d2))}")
# print(f"d3 값 : {d3} \t 주소 : {hex(id(d3))}")
# d1['a'] = 99
# d2['d'] = 44
# # 처음 주소랑 같음(d1 = d1)
# print(f"d1 값 : {d1} \t 주소 : {hex(id(d1))}")
# print(f"d2 값 : {d2} \t 주소 : {hex(id(d2))}")
# print(f"d3 값 : {d3} \t 주소 : {hex(id(d3))}")

# ***과제***
#1.
student_grade = 2
student_class = 3
student_number = 12
student_name = "최혜민"
student_height = 171.7
print(f"{student_grade}학년 {student_class}반 {student_number}번")
print(f"이름 : {student_name}")
print(f"키 : {student_height}cm")
#2.
print(type(student_grade))
print(type(student_class))
print(type(student_number))
print(type(student_name))
print(type(student_height))
#3.
our_team = ["김비야", "김유진", "박선주", "백선미", "안소영", "양혜원", "이혜령", "임재연", "최윤영", "최혜민", "하도연", "하진"]
print(our_team)
#4
print(our_team[9])
#5
print(our_team[5:9])