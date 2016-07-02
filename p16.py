inNum = eval(input())
counter = 0

for i in range(1, inNum+1):
    if(inNum%i==0):
        counter+=1
if counter == 2:
    print(inNum, "is prime")
else:
    print(inNum, "is not prime")