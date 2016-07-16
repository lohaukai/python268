def lev(in_num):
    mul = 1
    for i in range(1, in_num+1):
        mul *= i
    return mul


def P(n, m):
    return lev(n)/lev(n-m)

n=eval(input())
m=eval(input())
print(int(P(n, m)))
