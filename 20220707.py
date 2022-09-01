
# g = 1
# def testScope(a):
#     # global g 
#     g = 2 # 이 g를 전역 영역의 변수로 사용하고 싶을 때 => global g
#     return g + a

# print(testScope(1))
# print(g)

# # 여러 개 리턴 가능
# def swap(x, y):
#     return y, x

# print(swap(1, 2)) # 여러 개 리턴 할 때 => 튜플 사용

# # 튜플을 빼고 출력하고 싶을 때
# retValue = swap(1, 2)
# print(retValue[0], retValue[1])

# # 매개변수를 모두 더하여 합을 리턴하는 함수
# def sum(*nums):
#     total = 0

#     for n in nums:
#         total += n 
    
#     return total

# result = sum(1, 3)
# print("1 + 3 = ", result)
# print("1 + 3 + 5 + 7 = ", sum(1, 3, 5, 7))

# # 매개변수 중 가장 작은 값 하나만 리턴하는 함수
# def min(*nums):
#     minValue = nums[0]

#     for n in nums:
#         if n < minValue:
#             minValue = n

#     return minValue

# result = min(1, 3)
# print("min(1, 3) = ", result)
# print("min(0, 3, -11) = ", min(0, 3, -11))

# # 리스트 사용 => 여러 값 하나로 묶어 리턴 가능
# def multi_num(multi, start, end):
#     result = []
#     for n in range(start, end):
#         if n % multi == 0:
#             result.append(n)
#     return result

# multi2 = multi_num(17, 1, 200)
# print("multi_num(17, 1, 200) : ", multi2)

# multi3 = multi_num(3, 1, 100)
# print("multi_num(3, 1, 100) : ", multi3)

# # 튜플 사용 => 여러 값 여러 개 리턴 가능
# def min_max(*args):
#     min = args[0]
#     max = args[0]
#     for arg in args:
#         if min > arg:
#             min = arg
#         if max < arg:
#             max = arg
#     return min, max

# # 튜플 형태로 출력
# print(min_max(52, -3, 23, 89, -21))
# # 그냥 출력
# min_value, max_value = min_max(52, -3, 23, 89, -21)
# print("최젓값 : ", min_value)
# print("최곳값 : ", max_value)

# 이름을 입력받아 성과 이름을 나누어 리턴
def div_name(n):
    return n[0], n[1:]

surname, name = div_name("최혜민")
print("성 : ", surname)
print("이름 : ", name)