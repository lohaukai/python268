str = input()
userIn = input()
strIndex = str.find(userIn, 0)
while strIndex != -1:
    print(strIndex)
    strIndex = str.find(userIn, strIndex+1)
