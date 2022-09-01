# strA = "Hello Python"
# x = 5
# y = 3.14
# print(type(strA))
# print(type(x))
# print(type(y))

# import keyword
# print(keyword.kwlist)

# print("py""thon")
# print("py"+"thon")
# print("py"*3)

# strA = "python"
# print(strA[0:1])
# print(strA[1:3])
# print(strA[:2])
# print(strA[-2:])
# print(strA[:])

# strB = "python is powerful"
# print(strB[-1])
# print(strB[-2])
# print(strB[-3:])
# print(strB[-8:])

# strB = "python is powerful"
# print(strB[7:18])
# print(strB[:])
# print(strB[::2]) # 한칸씩 건너뛰어서 출력
# print(strB[-11:-9])
# print(strB[-18:-11])

# 리스트(List)
# colors = ["red", "green", "blue"]
# print(colors)
# print(type(colors))

# print(colors)
# colors.append("blue") # append => 맨 뒤에 값을 추가
# print(colors)

# print(colors)
# colors.insert(1, "black") # insert => 원하는 위치에 값을 추가
# print(colors)

# print(colors)
# print(colors.index("red")) # 처음부터 찾는다
# colors+=["red"] # colors 뒤에 red를 붙인다(append와 비슷)
# print(colors)
# print(colors.index("red", 1)) # 1번방부터 찾는다
# colors+="red" # [] => 없으면 글자가 하나하나 따로 출력된다
# print(colors)

# print(colors)
# print(colors.count("red")) # red 개수를 샌다
# print(colors.pop()) # 마지막 d를 없애고 반환
# print(colors.pop()) # 마지막 e를 없애고 반환
# print(colors.pop(1)) # 1번방인 black 반환
# print(colors)
# print()

# print(colors)
# colors.remove("blue") # 값을 없애기만 함
# print(colors)

# print(colors)
# colors.extend(["blue", "yellow", "white"]) # 리스트를 추가함
# print(colors)

# print(colors)
# colors.sort() # 오름차순 정렬
# print(colors)
# colors.reverse() # 내림차순 정렬
# print(colors)

# 튜플(Tuple)
# 순서가 존재
# 값 변경 불가(읽기 전용)
# ( )로 묶어서 표현함

#세트(Set)
a = {1, 2, 3, 4}
b = {3, 4, 4, 5}
print(a)
print(b) # 중복된 값은 빼고 출력
print(type(a))
print(type(b))

print(a.union(b)) # 합집합
print(a.intersection(b)) #교집합
print(a.difference(b)) #차집합
