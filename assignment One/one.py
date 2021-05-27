str = input("Enter the string value ")

result = ''
first = ''
last = ''


if len(str) < 2:
    result = "Empty String"

else:
    first = str[0:2]
    last = str[-2:]

    result = first+last
print(result)
