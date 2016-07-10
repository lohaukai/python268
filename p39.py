strIn = input()
userIn = input()
strIndex = strIn.find(userIn, 0)
while strIndex != -1:
    print(strIndex)
    strIndex = strIn.find(userIn, strIndex + 1)
