import hello_func
import greeting_func

def main():
    print('insa 모듈입니다.')
    print('__name : ', __name__) # __name__ : 현재 모듈의 이름
    # import한 파일 안의 함수 호출 가능
    hello_func.hello()
    greeting_func.greeting()

main()