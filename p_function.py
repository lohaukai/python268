def hi_python(times):
    print('Hi Python\n'*times)


def sum1(in_num):
    total = 0
    for i in range(in_num):
        total += i
    print('total =', total)
    return total

hi_python(eval(input()))
print('sum1 return:', sum1(eval(input())))



