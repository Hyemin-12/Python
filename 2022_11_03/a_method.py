# [1] 클래스 생성
class Person:
    def a_method(self):
        print("a_method가 호출되었습니다.")

    def b_method(self):
        self.a_method() # self를 사용해서 호출
        a_method()
    
def a_method():
    print('클래스 외부에 정의된 a_method 입니다.')

# [2] 클래스 사용
p1 = Person()
p1.a_method() # 바로 a_method 호출 가능
p1.b_method() # b_method를 통해 a_method 호출