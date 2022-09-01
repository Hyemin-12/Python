# import한 모듈에 실행문과 함수가 같이 있으면 gugudan 모듈의 실행문이 동작한 후 main 모듈을 실행한다.
import gugudan

for i in range(2, 10):
    print("=" * 20)
    gugudan.gugudan(i)