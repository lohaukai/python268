import random

#Ans = random.randint(1,5)
Ans = eval(input())
userAns = eval(input())

if Ans == userAns:
    print('你猜對了 答案正是', Ans)
else:
    print('猜錯了了喔 其實是', Ans)

