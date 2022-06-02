# 2312 최혜민
# 1.
a = int(input("정수1 입력 : "))
b = int(input("정수2 입력 : "))
print("")

if a > b:
    a, b = b, a
for i in range(a, b+1):
    print("{}단".format(i))
    for j in range(1, 9+1):
        print("{0} * {1} = {2}".format(i, j, i*j))
    print("")

2.
li = []
sum = 0
for i in range(0, 5):
    li.append(int(input(f"점수{i+1} 입력 : ")))

print("입력된 점수 : ", end = '')

for i in range(0, 5):
    print(li[i], end = ' ')
    sum += li[i]

print(f"\n합계 : {sum}")
print("평균: {0:0.2f}".format(sum / 5))

if (sum / 5) >= 60:
    s = "합격"
else:
    s = "불합격"
print("{0:0.2f}점으로 {1}입니다.\n".format(sum / 5, s))

# 3.
d = {"메로나": [1000, 20], "비비빅": [700, 3], "바밤바": [850, 100]}

# 3-6
while(1):
    print("1. 신규 상품 등록")
    print("2. 상품 수정")
    print("3. 상품 삭제")
    print("4. 상품 조회")
    print("0. 종료")

    selectNum = int(input("메뉴 입력 : "))
    print("")
    # 3-5
    if selectNum == 0:
        print("프로그램을 종료합니다.")
        break
    elif selectNum == 1:
        # 3-2
        print("1. 신규 상품 등록")
        newName = input("상품명 입력 : ")
        newPrice = int(input("가격 입력 : "))
        newCount = int(input("수량 입력 : "))

        d[newName] = [newPrice, newCount]

        print("{0:>5}{1:>8}{2:>8}".format("상품명", "가격", "수량"))
        for key in d.keys():
            print("{0:<8}{1:>8}{2:>8}".format(key, d[key][0], d[key][1]))
        print("")
    elif selectNum == 2:
        # 3-3
        print("2. 상품 수정")
        name = input("상품명 입력 : ")

        if name in d:
            print("1. 가격 수정")
            print("2. 수량 수정")

            n = int((input("메뉴 입력 : ")))

            if n == 1:
                changePrice = int(input("가격 입력 : "))

                d[name][0] = changePrice

                print("{0:>5}{1:>8}{2:>8}".format("상품명", "가격", "수량"))
                for key in d.keys():
                    print("{0:<8}{1:>8}{2:>8}".format(key, d[key][0], d[key][1]))
                print("")
            elif n == 2:
                changeCount = int(input("수량 입력 : "))

                d[name][1] = changeCount

                print("{0:>5}{1:>8}{2:>8}".format("상품명", "가격", "수량"))
                for key in d.keys():
                    print("{0:<8}{1:>8}{2:>8}".format(key, d[key][0], d[key][1]))
                print("")
            else:
                print('입력 오류\n')
        else:
            print("상품이 없습니다.\n")
    elif selectNum == 3:
        # 3-4
        print("3. 상품 삭제")
        deleteName = input("상품명 입력 : ")

        if deleteName in d:
            del d[deleteName]
        else:
            print("상품이 존재하지 않습니다.\n")

        print("{0:>5}{1:>8}{2:>8}".format("상품명", "가격", "수량"))
        for key in d.keys():
            print("{0:<8}{1:>8}{2:>8}".format(key, d[key][0], d[key][1]))
        print("")
    elif selectNum == 4:
        # 3-1
        print("4. 상품 조회")
        print("{0:>5}{1:>8}{2:>8}".format("상품명", "가격", "수량"))
        for key in d.keys():
            print("{0:<8}{1:>8}{2:>8}".format(key, d[key][0], d[key][1]))
        print("")
    else:
        print("입력 오류\n")
