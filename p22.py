inNum = eval(input())
outNum=0
for j in range(inNum):
    for i in range(j+1):
        outNum+=1
        print(outNum, end=' ')
    print()
