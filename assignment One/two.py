
str = "The lyrics is not that poor!"

notIndex = str.find('not')
porIndex = str.find('poor')
print(notIndex)
print(porIndex)


if notIndex < porIndex and notIndex > 0 and porIndex > 0:

    str = ''.join((str[:notIndex], "good"))


print(str)
