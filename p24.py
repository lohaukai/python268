inNum1 = eval(input())
inNum2 = eval(input())
for j in range(inNum1):
    for i in range(inNum2):
        ans = (i+1)*(j+1)
        if ans < 10:
            print(j+1, '*', i+1, '= ', ans, sep='', end=' ')
        else:
            print(j+1, '*', i+1, '=', ans, sep='', end=' ')
    print()
