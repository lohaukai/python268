inNum = eval(input())
for row in range(inNum):
    for column in range(inNum):
        if column+1 == inNum-row:
            print('*'*(2*row+1), end='')
        else:
            print(' ', end='')
    print()
