# 2312 최혜민
def min_in_list(li):
    min = li[0]
    for i in li:
        if i < min:
            min = i
    return min

print('수를 입력하세요 : ')
list = []
while(True):
    num = int(input(''))
    
    if num == 0:
        break

    list.append(num)

print("입력데이타 : ", end="")
for i in list:
    print(i, end=" ")

print()

print("가장 작은 수 : ", min_in_list(list))