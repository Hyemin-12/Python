id_number = input('주민등록번호 앞 6자리 입력 : ')

print(id_number[:2])
print(id_number[2:])
print('{}'.format(int(id_number[:2]) * int(id_number[2:])))