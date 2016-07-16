mathPass = {'柯南', '灰原', '步美', '美環', '光彦'}
engPass = {'柯南', '灰原', '丸尾', '野口', '步美'}
allPass = mathPass.intersection(engPass)

listOnlyMathPass = list(mathPass - allPass)
listOnlyMathPass.sort()
listOnlyEngPass = list(engPass - allPass)
listOnlyEngPass.sort()
listAllPass = list(allPass)
listAllPass.sort()

print(listOnlyMathPass)
print(listOnlyEngPass)
print(listAllPass)
