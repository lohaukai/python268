numIn = eval(input())
list1 = []

for i in range(numIn):
    list1.append(numIn-i)
    print('data %d' % (numIn-i))

print()

for i in range(numIn):
    print('data %d' % list1.pop())
