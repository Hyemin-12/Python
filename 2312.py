# 001. 화면에 Hello World 문자열을 출력하세요.
from ast import arg
from audioop import reverse
from posixpath import split


print('Hello World!')

# 002. 화면에 Mirim’s 
# Computer 문자열을 출력하세요.
print('Mirim\'s\nComputer')

# 003. 화면에 다음 문자열을 출력하세요.
# 신씨가 소리질렀다. "도둑이야".
print('신씨가 소리질렀다. "도둑이야".')

# 004. 화면에 ”C:\Windows” 문자열을 출력하세요.
print('"C:\\Windows"')

# 005. print 함수를 한 번만 사용하여 다음과 같이 출력하세요.
print('안녕하세요.\n만나서\t\t반갑습니다.')

# 006. print 함수를 한 번만 사용하여 “오늘은”과 “목요일”이라는 단어를 출력하세요.
print('오늘은', '목요일', sep=" ")

# 007. print 함수를 한 번만 사용하여 다음과 같이 3 단어를 출력하세요.
print('naver', 'kakao', 'samsung', sep=";")

# 008. print 함수를 한 번만 사용하여 다음과 같이 3 단어를 출력하세요.
print('naver', 'kakao', 'samsung', sep="/")

# 009. 다음 코드를 수정하여 줄바꿈이 없이 출력하세요.
print("first", end=""); 
print("second")

# 010. 5/3의 결과를 화면에 출력하세요.
print(5 / 3)

# 011. 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
삼성전자 = 50000
print('총 평가금액 : ', 삼성전자 * 10)

# 012. 다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩한 후 값과 변수의 타입을 출력하세요.
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print('시가총액 : ', 시가총액)
print(type(시가총액))
print('현재가 : ', 현재가)
print(type(현재가))
print('PER : ', PER)
print(type(PER))

# 013. 변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.
# s = "hello"
# t = "python“
# 두 변수를 이용하여 아래와 같이 출력해보세요.
s = "hello"
t = "python"
print('{}! {}'.format(s, t))

# 014. 아래 코드의 실행 결과를 예상해보세요.
# 2 + 2 * 3
# print 함수를 이용하여 출력하세요.
print(2 + 2 * 3)

# 015. 아래 변수에 바인딩된 값의 타입을 판별해보세요.
a = "132"
print(type(a))

# 016. 문자열 '720'를 정수형으로 변환해보세요.
num_str = "720"
print(type(num_str))

num_int = int(num_str)
print(type(num_int))

# 017. 정수 100을 문자열 '100'으로 변환해보세요.
num = 100
print(type(num))

num_str = str(num)
print(type(num_str))

# 018. 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
num_str = "15.79"
print(type(num_str))

num_float = float(num_str)
print(type(num_float))

# 019. year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
year = "2020"
year_int = int(year)
print('{}\n{}\n{}'.format(year_int-3, year_int-2, year_int-1))

# 020. 에어컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액을 계산한 후 이를 화면에 출력해보세요. (변수사용하기)
price = 48584
interest = 36

print('총 금액 : ', price * interest)

# 021. letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
letters = "python"
print(letters[0], letters[2])

# 022. 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
license_plate = "24가 2210"
print(license_plate[4:])

# 023. 아래의 문자열에서 '홀' 만 출력하세요.
string = "홀짝홀짝홀짝"
print(string[::2])

# 024. 문자열을 거꾸로 뒤집어 출력하세요.
string = "PYTHON"
print(string[::-1])

# 025. 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
phone_number = "010-1111-2222"
print(phone_number.replace('-', ' '))

# 026. 다음 전화번호를 아래와 같이 모두 붙여 출력하세요.
phone_number = "010-1111-2222"
print(phone_number.replace('-', ''))

# 027. url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
url = "https://www.e-mirim.hs.kr"
url_split = url.split('.')
print(url_split[-1])

# 028. 아래 코드의 실행 결과를 예상해보세요.
# lang = 'pyhon'
# lang[0] = 'P'
# print(lang)
# # Traceback (most recent call last):
# #   File "e:\2312\Python\2312.py", line 137, in <module>
#     # lang[0] = 'P'
# # TypeError: 'str' object does not support item assignment

# 029. 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
string = 'abcdfe2a354a32a'
print(string.replace('a', 'A'))

# 030. 아래 코드의 실행 결과를 예상해보세요.
string = 'abcd'
string.replace('b', 'B')
print(string)

