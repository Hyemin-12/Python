# 2312 최혜민
import random

class Bank:
    account_num = 0
    balance = 0
    def __init__(self):
        Bank.account_num = random.randrange(999999999)

    def inMoney(money):
        Bank.balance += money
        return Bank.balance

    def outMoney(money):
        Bank.balance -= money
        return Bank.balance

while(True):
    print("="*20)
    print("계좌관리")
    print("="*20)
    print("1. 계좌생성\t2. 입금\t3. 출금\t4. 잔액조회\t5. 종료")
    print("="*20)

    menu = int(input('메뉴 선택 : '))
    if menu == 1:
        b = Bank()
        print(f'계좌번호 {Bank.account_num}인 계좌가 생성되었습니다.')
    
    elif menu == 2:
        while(True):
            input_account = int(input('계좌번호 입력 : '))
            if input_account == Bank.account_num:
                in_money = int(input('입금 금액 : '))
                print(f'{Bank.account_num}에 {in_money}원이 입금되었습니다.')
                print(f'현재 잔액은 {Bank.inMoney(in_money)}원입니다.')
                break
            else:
                print(f'계좌번호 {input_account}가 존재하지 않습니다.')
                
    elif menu == 3:
        while(True):
            input_account = int(input('계좌번호 입력 : '))
            if input_account == Bank.account_num:
                out_money = int(input('출금 금액 : '))
                if out_money > Bank.balance:
                    print('잔액이 출금액보다 적습니다.')
                    print(f'현재 잔액은 {Bank.balance}원입니다.')
                else:
                    print(f'{Bank.account_num}에 {out_money}원이 출금되었습니다.')
                    print(f'현재 잔액은 {Bank.outMoney(out_money)}원입니다.')
                    break
            else:
                print(f'계좌번호 {input_account}가 존재하지 않습니다.')
    
    elif menu == 4:
        print("="*20)
        print("계좌번호\t잔액")
        print("="*20)
        print(Bank.account_num, Bank.balance)
        print("="*20)

    elif menu == 0:
        break
    
    else:
        print("올바른 메뉴를 선택해주세요.")