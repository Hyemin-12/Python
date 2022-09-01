# s = "Life is too short."
# print(s[3])
# print(s[11])
# print(s[-1])
# print(s[-7])
# print(s[-18])

# s = "Life is too short, You need Python."
# print(s[3:7])
# print(s[-10:-7])
# print(s[3:-10])
# print(s[-10:30])
# print(s[3:2])
# print(s[30:])
# print(s[-7:])
# print(s[:4])
# print(s[:-17])
# print(s[:])

# h = "  Happy Programming! app"
# print(len(h)) # 길이
# print(h.count("p")) # p의 개수 세기 
# print(h.upper()) # 대문자로
# print(h.lower()) # 소문자로
# print(h.strip()) # 양쪽 공백 없애기
# print(h.replace("Happy", "Funny")) # 문자열 바꾸기
# print(h.find("app")) # app를 왼쪽부터 찾기
# print(h.rfind("app")) # app를 오른쪽부터 찾기
# print(h.find("zoo")) # 못찾으면 -1 리턴

# h = "  Happy Programming! "
# print("a" in h) # 문자열에 a가 있는지 확인하기
# print("amp" in h)
# x = "01::23::ab::&&"
# y = x.split("::") # 문자열을 :: 만큼 나눠서 리스트 만들기
# print(y)
# print(", ".join(y)) # 리스트를 , 로 이어서 문자열 만들기

# s = "name : {}, number : {}, soccer : {}"
# print(s.format("Ronaldo", 7, True)) # {}안에 넣을 값을 쓰기
# print("name : {name}, number : {num}".format(name = "Jordan", num = 23))

# print("{:d}".format(515)) # 정수를 넣는다
# print("{:5d}".format(515)) # 최소 5자리를 차지한다
# print("{:+5d}".format(515)) # 양수면 +를 표시한다
# print("{:=+5d}".format(515)) # +를 맨 앞자리에 표시한다
# print("{:05d}".format(515)) # 빈자리는 0으로 채운다
# print("{:+05d}".format(515)) # 빈자리를 0으로 채우고, 양수면 0앞에 +를 붙인다

# print("{:f}".format(11.17)) # 실수를 넣는다
# print("{:12f}".format(11.17)) # 최소 12자리를 차지한다
# print("{:12.1f}".format(11.17)) # 소수점 1자리까지 반올림한다

# print("{:=+6.1f}".format(11.17))

# #문자열 포매팅 => 문자열을 이쁘게 출력하는 것
# a = 2
# b = 3
# s = '구구단 {0} x {1} = {2}'.format(a, b, a * b) #문자열.format()
# print(s)

# 함수와 메서드의 차이
# 메서드는 .앞 객체에 누가 하는 지가 나온다
# 함수는 혼자 돌아다닌다

# # 직접 대입
# s1 = 'name : {0}'.format('BlockDMask')
# print(s1)
# # 변수로 대입
# age = 55
# s2 = 'age : {0}'.format(age)
# print(s2)
# # 이름으로 대입
# s3 = 'number : {num}, gender : {gen}'.format(num = 1234, gen = '남')
# print(s3)
# # 인덱스를 입력하지 않으면 -> 차례대로 들어감
# s4 = 'name : {}, city : {}'.format('BlockDMask', 'seoul')
# print(s4)
# # 인덱스 순서가 바뀌면 -> 바뀐대로 들어감
# s5 = 'song1 : {1}, song2 : {0}'.format('nunu nana', 'ice cream')
# print(s5)
# # 인덱스를 중복해서 입력하면 -> 중복해서 들어감
# s6 = 'test1 : {0}, test2 : {1}, test3 : {0}'.format('인덱스0', '인덱스1')
# print(s6)
# # 중괄호를 출력하고 싶으면 -> 중괄호를 두 번 쓴다
# s7 = 'Format example.{{}}, {}'.format('test')
# print(s7)
# # 중괄호 안에 글씨를 넣고 싶으면 -> 중괄호를 세 번 쓴다
# s8 = 'This is value {{{0}}}'.format(1212)
# print(s8)

# #문자열을 공백으로 채우기
# # 왼쪽 정렬 <
# s9 = 'this is {0:<10} | done {1:<5} |'.format('left', 'a')
# print(s9)
# # 오른쪽 정렬 >
# s10 = 'this is {0:>10} | done {1:>5} |'.format('right', 'b')
# print(s10)
# # 가운데 정렬 ^
# s11 = 'this is {0:^10} | done {1:^5} |'.format('center', 'c')
# print(s11)

# #문자열을 공백이 아닌 값으로 채우기
# # 왼쪽 정렬 <
# s12 = 'this is {0:-<10} | done {1:O<5} |'.format('left', 'a')
# print(s12)
# # 오른쪽 정렬 
# s13 = 'this is {0:+>10} | done {1:0>5} |'.format('right', 'b')
# print(s13)
# # 가운데 정렬 
# s14 = 'this is {0:.^10} | done {1:@^5} |'.format('center', 'c')
# print(s14)

# # 자리수와 소수점 표현하기
# # 정수 n자리(자리수가 부족하면 0으로 채워짐)
# s15 = '정수 3자리 : {0:03d}, {1:03d}'.format(12345, 12)
# print(s15)
# # 소수 n자리(자리수가 부족하면 0으로 채워짐)
# s16 = '아래 2자리 : {0:0.2f}, 아래 5자리 : {1:0.5f}'.format(123.1254567, 3.14)
# print(s16)

a = 2
b = 1
s = '구구단 {0} x {1} = {2}'.format(a, b, a * b) #문자열.format()
print(s) 