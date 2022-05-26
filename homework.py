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
#6
club = {
    "김비야" : "영화감상반", "김유진" : "코딩클리닉반", "박선주" : "도서반", "백선미" : "심리학연구반", 
    "안소영" : "금융경제반", "양혜원" : "피구반", "이혜령" : "교지편집반", "임재연" : "또래상담반", 
    "최윤영" : "사진반", "최혜민" : "코딩클리닉반", "하도연" : "배드민턴반", "하진" : "영화감상반"
    }
#7
print(club["안소영"])
#8
print(club[our_team[0]])

#대단원 종합 평가
#1.
print(331/17)
#2.
x = 37
print(x ** 2)
#3.
y = 10 ** 10
print(y)
#4.
a = 123 + 456j
print(a.conjugate())
#5. : 2
#6.
fun = "funny day"
#7. : 5
#8.
fun.replace("day", "Life")
#9. : 4
#10. 
mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#11. 
h = 3
m = 15
h, m = m, h