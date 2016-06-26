import functools
import operator

def product(seq):
    """Product of a sequence."""
    return functools.reduce(operator.mul, seq, 1)

int1 = eval(input())
int2 = eval(input())
int3 = eval(input())
list1 = [int1, int2, int3]

print ('sum is', sum(list1))
print ('average is', '%.2f' %round(sum(list1)/len(list1)))
print ('product is', product(list1))
print ('smallest is', min(list1))
print ('largest is', max(list1))