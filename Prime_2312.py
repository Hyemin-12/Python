# 2312 최혜민

print("1 ~ N 까지의 소수와 그 갯수를 구하는 프로그램")

def isPrimeNumber(num):
    cnt = 0
    li = []

    for i in range(2, num+1):
        li.append(i)

    print("소수 : ", end='') 
    for n in li:
        for i in range(2, n+1):
            if(n % i == 0):
                if(n == i): 
                    print(n, " ", end='')
                    cnt+=1
                    break
                else:
                    break

    print("\n1 ~ {0}까지 소수의 갯수 : {1}".format(num, cnt))

n = int(input("N 입력 : "))

isPrimeNumber(n)