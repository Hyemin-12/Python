# # 매개변수 1개
# import random
# #인자 값 = 주사위 눈 수 조정, pip: 주사위의 눈을 의미
# def rolling_dice(pip):
#     n = random.randint(1, pip)
#     print(pip, "면 주사위 굴린 결과 : ", n)

# rolling_dice(4)
# rolling_dice(6)
# rolling_dice(10)

# # 매개변수를 여러 개 줄 수 있음
# import random
# #인자 값 = 주사위 눈 수 조정, pip: 주사위의 눈을 의미
# def rolling_dice(pip, repeat):
#     for r in range(1, repeat+1):
#         n = random.randint(1, pip)
#         print(pip, "면 주사위 굴린 결과", r, " : ", n)

# rolling_dice(4, 3)
# rolling_dice(6, 2)
# rolling_dice(10, 4)

# def func_sum(in_list):
#     sum = 0
#     li = in_list.split()
#     for i in li:
#         sum += int(i)
#     return sum

# in_list = input("데이타 입력 : ")
# print("합 : ", func_sum(in_list))

# # 가변 인수는 *으로 받는다
# def p(*args):
#     str = ""
#     for a in args:
#         str += a  
#     print(str)
# p("🧡")
# p("🧡", "💛")
# p("🧡", "💛", "💚")
# p("🧡", "💛", "💚", "💙")
# p("🧡", "💛", "💚", "💙", "💜")

# # 가변 인수는 매개변수의 맨 마지막에 와야함
# def p (space, space_num, *args):
#     str = args[0]
#     for i in range(1, len(args)):
#         str += (space * space_num) + args[i]
#     print(str)

# p("!", 3, "🧡", "💛")
# p("~", 1, "🧡", "💛", "💚")
# p("_", 2, "🧡", "💛", "💚", "💙")

# def star(ch, *nums):
#     for i in nums:
#         print(ch*i)
# star("🧡", 3)
# star("💛", 1, 2, 3)

# def fn(a, b, c, *d):
#     print(a, b, c, d)
# # 셋 다 오류
# fn(c=3, b=2, a=1, 4, 5)
# fn(1, 2, c=3 4, 5)
# fn(4, 5, a=1, b=2, c=3)