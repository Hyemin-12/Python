# 모듈에서 특정 함수나 클래스만 가져올 때
# from 모듈이름 import 함수명
from sys import exit

while True:
    print("종료하려면 exit를 입력하세요")
    user_input = input("> ")
    if user_input == "exit":
        exit()