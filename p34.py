userIn = 'y'
while userIn == 'y':
    numIn = eval(input())
    if numIn < 60:
        print('fail')
    else:
        print('pass')
    userIn = input()
