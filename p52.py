def mul_add(in_num):
    mul = 1
    add = 0
    for i in range(1, in_num+1):
        mul *= i
        add += i
    return mul, add

ans = mul_add(eval(input()))
print(ans[0], ans[1], sep='\n')
