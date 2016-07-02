inNum = eval(input())

for j in range(2, inNum+1):
    counter = 0
    for i in range(1, j+1):
        if(j%i==0):
            counter+=1
    if counter == 2:
        print(j, "is prime")
    # else:
    #     print(j, "is not prime")