inNum = eval(input())
for row in range(inNum):
    for column in range(inNum):
        if row < inNum/2:
            print(' '*int((inNum-(2*row+1))/2), '*'*(2*row+1), sep='', end='')
            break
        else:
            print(' '*int((inNum-(2*(inNum-row)+1))/2), '*'*(2*(inNum-row)-1), end='')
            break
    print()
