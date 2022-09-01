# 2312 최혜민

def intersect(str1, str2):

    res = []

    for ch1 in str1:
        for ch2 in str2:
            if(ch1 == ch2):
                if ch1 not in res:
                    res.append(ch1)

    return res
                

str1 = input("첫 번째 문자열 입력 : ")
str2 = input("두 번째 문자열 입력 : ")

result = intersect(str1, str2)

result.sort()

print(result)