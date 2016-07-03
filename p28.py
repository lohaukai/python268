import random

#Ans = random.randint(1,99)
minNum = 1
maxNum = 100
print(minNum, "< ? <", maxNum)

Ans = eval(input())
userAns = eval(input())
while Ans != userAns:
    if userAns > Ans:
        maxNum = userAns
        print("wrong answer, guess smaller")
        print(minNum, "< ? <", maxNum)
        userAns = eval(input())
    else:
        minNum = userAns
        print("wrong answer, guess larger")
        print(minNum, "< ? <", maxNum)
        userAns = eval(input())
        
print("bingo answer is", Ans)
