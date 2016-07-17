def g1(n):
    for i in range(1, n+1):
        print(i)
        yield i

print(g1(10))
print(list(g1(10)))
