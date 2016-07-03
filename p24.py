inNum1 = eval(input())
inNum2 = eval(input())
for j in range(inNum1):
    for i in range(inNum2):
        ans = (i+1)*(j+1)
        print(j+1, '*', i+1, '=%2.d'%ans, sep='', end=' ')
    print()
