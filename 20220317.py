# # 네 개 다 쓸 수 있음
# print('Python start!')
# print("Python start!")
# print("""Python start!""")
# print('''Python start!''')

# # sep => 문자열 사이를 연결 시켜줌
# print('P', 'Y', 'T', 'H', 'O', 'N', sep = "")
# print('010', '7777', '7777', sep = "-")
# print('python', 'google.com', sep = "@")

# # end => 한번에 다 찍고 싶을 때(원래는 자동 줄바꿈)
# print('Welcom To', end = ' ')
# print('IT News', end = ' ')
# print('Web Site', end = ' ')

# import sys
# print('learn Python', file = sys.stdout)

# print(8 + 5)
# print(8 - 5)
# print(8 * 5)
# print(8 / 5)
# print(8 // 5)
# print(8 % 5)

# age = 18
# print(age)
# after_2 = 2
# print(age + after_2)
# result = age - after_2
# print(result)

# age = 18
# print(age)
# age += 2
# print(age)
# age -= 1
# print(age)
# age *= 2
# print(age)
# # age /= 2
# # print(age)
# age //= 2
# print(age)
# age %= 6
# print(age)
# age **= 3
# print(age)

# # 파이썬은 값이 변하면 타입도 변함
# age = 18
# print(age)
# print(type(age)) #int
# pi = 3.14
# print(pi)
# print(type(pi)) #float
# age /= 2
# print(age)
# print(type(age)) #float
# x = 10 + 3.14
# print(x)
# print(type(x)) #float

# print(0b1100111000) #2진수
# print(type(0b1100111000))
# print(0o130) #8진수
# print(type(0o130))
# print(0xD7A) #16진수
# print(type(0xD7A))

# print(10e3)
# print(type(10e3))
# print(1.23456E2)
# print(type(1.23456E2))
# print(1.23456e-2)
# print(type(1.23456e-2))
# print(1.23456e22)
# print(type(1.23456e22))

#print(8 + 24j)
#c = 1.2 + 3.4J
#print(c)
#print(type(c))
#print(c.real) #실수
#print(c.imag) #허수
#print(c.conjugate()) #켤레복소수
#d = 1j
#print(d * d.conjugate())

#print(int(12.7))
#print(int('321'))
#print(float(456))
#print(float('65.4'))
#print(float('123e4'))
#print(complex(1.23))
#print(complex('1.23+45.6j'))
#print(str(1.23))

greeting = 'Hello'
to = 'world!'
print(greeting)
print(type(greeting))
say_hello = greeting + ", " + to
print(say_hello)
print("Hello" * 5)
print("\"Hello\"\n" + to)
multiline = """Happy 
Programming""" #따옴표 세 개 => 변수에 여러 줄을 저장함
print(multiline)
