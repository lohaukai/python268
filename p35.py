inNum = eval(input())
for j in range(inNum):
    for i in range(inNum):
        if i+1 < inNum-j:
            print(' ', end='')
        else:
            if i == inNum-1:
                print('*', end='')
            else:
                print('* ', end='')
    print()