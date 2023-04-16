lists = input().split('|')[::-1]
for row in range(len(lists)):
    for el in lists[row].split():
        print(el, end=' ')




# lists = input().split('|')[::-1]
# result = []
# for sub_list in lists:
#     result.extend(sub_list.split())
# print(*result)
