# # mutable 객체
# print("=" * 50)
# print("mutable 객체 요소로 존재하는 immutable, mutable")
# print("=" * 50)
# arr1 = [55, 66, [11, 22], 'a', 'b']
# arr2 = [55, 66, [11, 22], 'a', 'b']
# # 리스트(mutable) 객체의 주소 => 주소 다름
# print(f"arr1 : {arr1} \t 주소 : {hex(id(arr1))}")
# print(f"arr2 : {arr2} \t 주소 : {hex(id(arr2))}")
# # 리스트 내부의 immutable 요소 => 주소 같음
# print("-" * 50)
# print("리스트 내부의 immutable 요소들")
# print(f"arr1[0] : {arr1[0]} \t 주소 : {hex(id(arr1[0]))}")
# print(f"arr2[0] : {arr2[0]} \t 주소 : {hex(id(arr2[0]))}")
# print(f"arr1[1] : {arr1[1]} \t 주소 : {hex(id(arr1[1]))}")
# print(f"arr2[1] : {arr2[1]} \t 주소 : {hex(id(arr2[1]))}")
# print(f"arr1[3] : {arr1[3]} \t 주소 : {hex(id(arr1[3]))}")
# print(f"arr2[3] : {arr2[3]} \t 주소 : {hex(id(arr2[3]))}")
# print(f"arr1[4] : {arr1[4]} \t 주소 : {hex(id(arr1[4]))}")
# print(f"arr2[4] : {arr2[4]} \t 주소 : {hex(id(arr2[4]))}")
# # 리스트 내부의 mutable 요소 => 주소 다름
# print("-" * 50)
# print("리스트 내부의 mutable 요소들")
# print(f"arr1[2] : {arr1[2]} \t 주소 : {hex(id(arr1[2]))}")
# print(f"arr2[2] : {arr2[2]} \t 주소 : {hex(id(arr2[2]))}")

# # 얕은 복사 -> =
# 주소 동일
# arr1 = [1, 2, 3]
# arr2 = arr1
# print(f"arr1 : {arr1} \t 주소 : {hex(id(arr1))}")
# print(f"arr2 : {arr2} \t 주소 : {hex(id(arr2))}")
# # 주소(참조)만 복사한 것이기 때문에 원본의 내용이 바뀌면 같이 바뀜
# arr1.append(4)
# print(f"arr1 : {arr1} \t 주소 : {hex(id(arr1))}")
# print(f"arr2 : {arr2} \t 주소 : {hex(id(arr2))}")

# 얕은 복사 -> [:]
# 주소 다름, 내부 주소 동일
# [:] => mutable 안에 mutable이 들어 있을 때 그 mutable에 대해 얕은 복사 사용 
# => 그냥 얕은 복사로 치기로 했음
arr1 = [4, 5, 6, [2, 4, 8]]
arr2 = arr1[:]
print("1. 전체 출력")
print(f"arr1 : {arr1}, 주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2}, 주소 : {hex(id(arr2))}")
print("2. 리스트의 끝에 값 추가")
arr1.append(4)
arr2.append(22)
print(f"arr1 : {arr1}, 주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2}, 주소 : {hex(id(arr2))}")
# 리스트 안에 있는 리스트
print("3. 리스트 내부 리스트")
print(f"arr1[3] : {arr1[3]}, 주소 : {hex(id(arr1[3]))}")
print(f"arr2[3] : {arr2[3]}, 주소 : {hex(id(arr2[3]))}")
print("4. 리스트 내부 리스트에 값 추가")
arr1[3].append(99)
print(f"arr1[3] : {arr1[3]}, 주소 : {hex(id(arr1[3]))}")
print(f"arr2[3] : {arr2[3]}, 주소 : {hex(id(arr2[3]))}")
print("5. 리스트 전체 다시 확인")
print(f"arr1 : {arr1}, 주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2}, 주소 : {hex(id(arr2))}")