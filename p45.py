list1 = []
userIn = eval(input())
while userIn != -1:
    list1.append(userIn)
    userIn = eval(input())

list1.sort()
print(list1)
list1.insert(3, 10)
print(list1)
print(list1.count(10))
list1.sort()
list1.reverse()
print(list1)