# 2312 최혜민
group1 = list(map(int, input('첫 번째 그룹의 데이타 : ').split(' ')))
group2 = list(map(int, input('두 번째 그룹의 데이타 : ').split(' ')))

merge_group = []

for i in group1:
    merge_group.append(i)

for i in group2:
    merge_group.append(i)

merge_group_set = set(merge_group)
merge_group = list(merge_group_set)
merge_group.sort()

print('병합된 그룹의 데이타 : ', end="")
for i in merge_group:
    print(i, end=" ")