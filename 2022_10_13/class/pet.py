# [1] : 클래스 생성
class Pet:
    # 클래스의 모든 메소드는 첫 번째 파라미터로 self 값을 받는다.
    # 짖다
    def bark_dog(self):
        print('멍멍~')
    def bark_cat(self):
        print('야옹~ 야옹~')
    def bark_hamster(self):
        print('찍찍~')

# [2] : 클래스 사용

p1 = Pet()
# self 값은 자동으로 전달되기 때문에 직접 넘겨줄 필요 X
p1.bark_dog()

p2 = Pet()
p2.bark_cat()
p2.bark_dog()

p3 = Pet()
p3.bark_hamster()