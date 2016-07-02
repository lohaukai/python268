inNum = eval(input())
sumNum = 0

for i in range(1, inNum + 1):
    sumNum += i
    print(i, end="")
    if i < inNum:
        print("+", end="")
print(" =", sumNum)
