# 2312 최혜민

print("1 ~ N 까지의 소수와 그 갯수를 구하는 프로그램")

def isPrimeNumber(num):
    cnt = 0

    print("소수 : ", end='') 

    for i in range(2, num+1):
        for j in range(2, num+1):
            if(i % j == 0):
                if(i == j): 
                    print(i, " ", end='')
                    cnt+=1
                else:
                    break

    print("\n1 ~ {0}까지 소수의 갯수 : {1}".format(num, cnt))

n = int(input("N 입력 : "))

isPrimeNumber(n)