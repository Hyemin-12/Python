# [1] 클래스 생성
class Person:
    # 클래스 변수
    count_class_var = 0

    # 생성자
    def __init__(self, name, age, power):
        self.name = name
        self.age = age
        self.power = power
        self.increase_obj() # increase_obj 메서드 호출

    def increase_obj(self): # 클래스 변수 값 1 증가
        Person.count_class_var += 1

# [2] 클래스 사용
print('현재까지 생성된 인스턴스 객체의 갯수 : ', Person.count_class_var)
p1 = Person('홍길동', 20, 100)
print('현재까지 생성된 인스턴스 객체의 갯수 : ', Person.count_class_var)
p2 = Person('강감찬', 40, 200)
print('현재까지 생성된 인스턴스 객체의 갯수 : ', Person.count_class_var)
p3 = Person('을지문덕', 30, 300)
print('현재까지 생성된 인스턴스 객체의 갯수 : ', Person.count_class_var)