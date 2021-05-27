
str = "The lyrics is poor!"

notIndex = str.find('not')
porIndex = str.find('poor')


if notIndex < porIndex and notIndex > 0 and porIndex > 0:

    str = ''.join((str[:notIndex], "good"))


print(str)
