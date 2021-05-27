list = [100, 1, 22, 13, 100, 5, 2, 6, 7, 22, 5]


for i in list:
    if list.count(i) > 1:
        ind = list.index(i)
        list.pop(ind)

print(list)
