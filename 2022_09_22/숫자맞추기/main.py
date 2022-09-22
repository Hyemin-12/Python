import random

random_number = random.randint(1, 100)
cnt = 1

while True:
    try:
        my_number = int(input('1 ~ 100 사이의 수 입력 : '))
        
        if (my_number > random_number):
            print('DOWN!')
        elif (my_number < random_number):
            print('UP!')
        else:
            print(f'축하합니다. {cnt}회 만에 맞췄습니다!')
            break
        
        cnt += 1
    except:
        print('에러가 발생했습니다. 1 ~ 100 사이의 수를 입력하세요.')