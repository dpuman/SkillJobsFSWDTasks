list = [1, 2, 3]

list2 = [4, 5, 6, 1]
result = False
for i in list:
    for j in list2:
        if i == j:
            result = True

print(result)
