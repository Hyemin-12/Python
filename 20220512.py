# # 얕은 복사 => copy 메서드 사용
# # 배열명.copy : 주소 다름, 내부 주소 동일
# arr1 = [4, 5, 6, [2, 4, 8]]
# arr2 = arr1.copy() # 여기서 복사 copy 메서드 사용
# print("1. 전체 출력")
# print(f"arr1 : {arr1}, 주소 : {hex(id(arr1))}")
# print(f"arr2 : {arr2}, 주소 : {hex(id(arr2))}") # 둘의 주소가 다르다 -> 콜론과 같음
# print("2. 리스트의 끝에 값 추가")
# arr2.append(22) # arr2에 값 추가
# print(f"arr1 : {arr1}, 주소 : {hex(id(arr1))}")
# print(f"arr2 : {arr2}, 주소 : {hex(id(arr2))}") # arr2에만 22가 추가됨 -> (내부 리스트가 없을 때는) 깊은 복사로 생각
# # 리스트 안에 있는 리스트
# print("3. 리스트 내부 리스트") 
# print(f"arr1[3] : {arr1[3]}, 주소 : {hex(id(arr1[3]))}")
# print(f"arr2[3] : {arr2[3]}, 주소 : {hex(id(arr2[3]))}") # 둘의 주소가 같음
# print("4. 리스트 내부 리스트에 값 추가")
# arr1[3].append(99)
# print(f"arr1[3] : {arr1[3]}, 주소 : {hex(id(arr1[3]))}")
# print(f"arr2[3] : {arr2[3]}, 주소 : {hex(id(arr2[3]))}") # 99가 둘 다 추가된 것처럼 보임(같은 메모리 참조) -> 콜론과 같음
# print("5. 리스트 전체 다시 확인")
# print(f"arr1 : {arr1}, 주소 : {hex(id(arr1))}")
# print(f"arr2 : {arr2}, 주소 : {hex(id(arr2))}")

# # 얕은 복사 -> copy 모듈의 copy 함수를 이용한 얕은 복사
# # copy.copy(배열명) : 주소 다름, 내부 주소 동일
# import copy
# arr1 = [4, 5, 6, [2, 4, 8]]
# arr2 = copy.copy(arr1) # 여기서 복사 copy 함수 사용
# print("1. 전체 출력")
# print(f"arr1 : {arr1}, 주소 : {hex(id(arr1))}")
# print(f"arr2 : {arr2}, 주소 : {hex(id(arr2))}")
# print("2. 리스트의 끝에 값 추가")
# arr2.append(22)
# print(f"arr1 : {arr1}, 주소 : {hex(id(arr1))}")
# print(f"arr2 : {arr2}, 주소 : {hex(id(arr2))}")
# # 리스트 안에 있는 리스트
# print("3. 리스트 내부 리스트")
# print(f"arr1[3] : {arr1[3]}, 주소 : {hex(id(arr1[3]))}")
# print(f"arr2[3] : {arr2[3]}, 주소 : {hex(id(arr2[3]))}")
# print("4. 리스트 내부 리스트에 값 추가")
# arr1[3].append(99)
# print(f"arr1[3] : {arr1[3]}, 주소 : {hex(id(arr1[3]))}")
# print(f"arr2[3] : {arr2[3]}, 주소 : {hex(id(arr2[3]))}") # 얘도 콜론이랑 똑같음
# print("5. 리스트 전체 다시 확인")
# print(f"arr1 : {arr1}, 주소 : {hex(id(arr1))}")
# print(f"arr2 : {arr2}, 주소 : {hex(id(arr2))}")

# # copy 함수를 이용하여 dictionary 얕은 복사
# # 주소 다름 내부 주소 동일
# import copy;
# d1 = {'a' : 'Mirim', 'b' : [1, 2, 3]}
# d2 = copy.copy(d1) # copy 모듈 얕은 복사
# print("1. 전체 출력")
# print(f"d1 : {d1}, address : {hex(id(d1))}")
# print(f"d2 : {d2}, address : {hex(id(d2))}")
# print("\n2. 딕셔너리에 새 key, value 추가")
# d2['c'] = 'kimchi'
# print("d2['c'] = 'kimchi'")
# print(f"d1 : {d1}, address : {hex(id(d1))}")
# print(f"d2 : {d2}, address : {hex(id(d2))}")
# #딕셔너리 내부 리스트 value
# print("\n3. 딕녀서리 내부 리스트")
# print(f"d1 : {d1['b']}, address : {hex(id(d1['b']))}")
# print(f"d2 : {d2['b']}, address : {hex(id(d2['b']))}")
# print("\n4. 딕셔너리 내부 리스트에 값 추가")
# d1['b'].append('NO')
# print("d1['b'].append('NO')")
# print(f"d1 : {d1['b']}, address : {hex(id(d1['b']))}")
# print(f"d2 : {d2['b']}, address : {hex(id(d2['b']))}")
# print("\n5. 딕셔너리 전체 다시 확인")
# print(f"d1 : {d1}, address : {hex(id(d1))}")
# print(f"d2 : {d2}, address : {hex(id(d2))}")

# 깊은 복사 : 값만 복사, 객체 공유X
import copy # copy 모듈 불러오기
arr1 = [1, 2, [99, 88, 77], 3]
arr2 = copy.deepcopy(arr1) # copy 모듈 깊은 복사
print("1. 전체 출력")
print(f"arr1 : {arr1}, address : {hex(id(arr1))}")
print(f"arr2 : {arr2}, address : {hex(id(arr2))}")
print("\n2. 리스트에 새 key, value 추가")
arr1.append(0)
print('arr1.append(0)')
print(f"arr1 : {arr1}, address : {hex(id(arr1))}")
print(f"arr2 : {arr2}, address : {hex(id(arr2))}")
# 리스트 내부에 리스트 추가
print("\n3. 리스트 내부 리스트")
print(f"arr1[2] : {arr1[2]}, address : {hex(id(arr1[2]))}")
print(f"arr2[2] : {arr2[2]}, address : {hex(id(arr2[2]))}") # 내부 리스트도 둘의 주소가 다르다(깊은 복사이기 때문에)
print("\n4. 리스트 내부 리스트에 값 추가")
arr1[2].append(10)
print(f"arr1[2] : {arr1[2]}, address : {hex(id(arr1[2]))}")
print(f"arr2[2] : {arr2[2]}, address : {hex(id(arr2[2]))}") # 위랑 주소 다름
print("\n5. 리스트 전체 다시 확인")
print(f"arr1 : {arr1}, 주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2}, 주소 : {hex(id(arr2))}")

# id = "881120-1068234"
# print("연월일 : ", id[0:6])
# print("숫자 : ", id[7:]) 
# print("성별 : ", id[7])

# li = [1, 3, 5, 4, 2]
# print("원본 : ", li)
# li.sort()
# li.reverse()
# print("결과 : ", li)

# li = ['Life', 'is', 'too', 'short']
# print(" ".join(li))

# t = (1, 2, 3)
# t += (4, )
# print(t)

# a = {'A' : 90, 'B' : 80, 'C': 70}
# b = a.pop('B')
# print("원본 딕셔너리 : ", a)
# print("'B' 추출 후 딕셔너리 : ", a)
# print("추출된 B의 값 : ", b)
