roll = eval(input())

if (roll == 1):
    score = eval(input())
    if (score > 100 or score < 0):
        print('score error')
    elif (score >= 60):
        print('pass')
    else:
        print('fail')
elif (roll == 2):
    score = eval(input())
    if (score > 100 or score < 0):
        print('score error')
    elif (score >= 70):
        print('pass')
    else:
        print('fail')
else:
    print('roll error')
