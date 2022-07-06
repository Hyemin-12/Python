# 2312 최혜민

def intersect(str1, str2):
    str1Lower = str(str1).lower()
    str2Lower = str(str2).lower()

    str1List = list(str1Lower)    
    str2List = list(str1Lower)

    res = []

    for i in range (0, len(str1)):
        for j in range(0, len(str2)):
            if(str1Lower[i] == str2Lower[j]):
                if(not(str1Lower[i] in res)):
                    res.append(str1[i])

    return res
                

str1 = input("첫 번째 문자열 입력 : ")
str2 = input("두 번째 문자열 입력 : ")

result = intersect(str1, str2)

result.sort()

print(result)