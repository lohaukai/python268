inNum = eval(input())
for j in range(inNum):
    for i in range(inNum):
        if i < j:
            print(' ', end='')
        else:
            print('*', end='')
    print()
