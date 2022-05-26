# # 리스트(List)
# # 리스트는 여러 가지 자료형을 한꺼번에 넣을 수 있다.
# l = []
# print(l)
# player = ["Messi", 10, True]
# print(player)
# print(list("Happy"))
# print(list((1125, 2436)))
# print(list({"menu" : "pizza", "price" : 10000}))
# print(list({"사과", "배"}))
# nums = list(range(3))
# print(nums)

# nums + [10, 11] # nums에다가 [10, 11]을 추가만 함
# print(nums + [10, 11]) # 이렇게 하면 나옴
# print(nums)
# nums += [10, 11] # 추가한 값을 저장까지 함
# print(nums)

# append : 기존 위치에 값을 추가
# nums.append(20) # 리스트에 20을 추가한다
# print(nums)
# nums.append([30, 31]) # 리스트에 [30, 31]이라는 리스트를 추가한다
# print(nums)
# insert : 원하는 위치에 값을 추가
# nums.insert(2, 40) # 리스트의 두번째 자리에 40을 추가한다
# print(nums)
# nums.extend([50, 51]) # [50, 51]을 리스트 안에 값으로 넣는다 => [0, 1, 40, 2, 10, 11, 20, [30, 31], 50, 51]
# print(nums)

# print(nums[7]) # nums[7] 값 출력
# nums[7] = 60 # nums[7] 값을 60으로 변경
# print(nums)

# del nums[2] # nums[2]를 삭제
# print(nums)
# nums.remove(20) # nums 안에서 20을 찾아 삭제
# print(nums)
# print(nums.pop()) # 맨 끝에 있는 값을 삭제
# print(nums.pop(5)) # 5번째 값을 삭제
# nums.append(10)
# print(nums)
# nums.remove(10) # 앞에 있는 10부터 지워짐
# print(nums)
# nums.clear()
# print(nums)

# nums = list(range(3))
# nums += [100, 10]
# print(nums[3])
# print(3 in nums) # nums 안에 3이 있는지 검색(if문의 조건을 쓸 때 자주 사용)
# print(10 in nums)

# print(len(nums))
# nums.sort()
# print(nums) # 오름차순 정렬
# nums.reverse() # sort 후 reverse : 내림차순 정렬
# print(nums)

#튜플(Tuple)
# t = ()
# print(t)
# xy = (2560, 1440)
# print(xy)
# color = 129, 247, 216
# print(color)
# print(xy + color)
# print(xy * 2)

# color = 129, 247, 216 # 패킹
# red, green, blue = color # 언패킹 color안에 있는 애들을 red, green, blue에 저장
# print(red)
# print(green)
# print(blue)

# x, y = 1920, 1080
# print(x)
# print(y)

# x = 2560
# y = 1440
# x, y = y, x # 값을 이렇게 바꿀 수 있음
# print(x)
# print(y)
# a = (123, "abc", True, 123)
# print(a[1])
# print(a[2:])
# print(a[:2])
# # a[1] = 2
# print(a.index("abc"))
# print(a.count(123))

# t = (1, 2, 3)
# t += (4,) # 굳이 값을 추가하고 싶으면 ,를 쓰면 추가 가능
# print(t)

# 딕셔너리(Dictionary)
# d = {}
# print(d)
# urls = {"google" : "google.com", 18 : "unesco.org"}
# print(urls)

# urls["x"] = 2560 # 딕셔너리에 x가 없으면 추가
# print(urls)

# urls["x"] = 1920 # 딕셔너리에 x가 있으면 수정
# print(urls)

# del urls["x"] # x 삭제
# print(urls)
# urls.pop(18) # 18 삭제
# print(urls)
# urls.clear()
# print(urls)

# urls = {"google" : "google.com", 18 : "unesco.org"}
# print(urls["google"]) # 키를 가져옴
# print(urls.get("google")) # 키를 가져옴
# print("google" in  urls) # 키가 있는지 확인함 => True
# print("google.com" in urls) # 값은 확인하지 않음 => False
# print("google.com" in urls.values()) # 값이 있는지/ 확인함 => True

#셋(set)
# game = {"LOL", "OverWatch", "Tetris", 1942, 2048}
# print(game)
# print(set("Funny"))
# print(set([2048, "Tetris", "Cube"]))
# print(set((2560, 1440)))
# print(set({"google" : "google.com", 18:"unesco.org"}))
# print(set(range(3)))

# print(game.add("Fifa")) # 하나만 추가할 때는 add
# print(game.update(("NBA", "MLB"))) # 여러 개를 추가할 떄는 update

# print(game.remove("LOL")) # 제거

# s3 = {3, 6, 9, 12}
# s4 = {4, 8, 12, 16}
# # 교집합
# print(s3 & s4)
# print(s3.intersection(s4))
# # 합집합
# print(s3 | s4)
# print(s3.union(s4))
# # 차집합
# print(s3 - s4)
# print(s3.difference(s4))
# # 대칭 차집합(교집합 반대)
# print(s3 ^ s4)
# print(s3.symmetric_difference(s4))

