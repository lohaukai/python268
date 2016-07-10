strIn1 = input()
strIn2 = input()
if len(strIn1) < len(strIn2):
    print('1<2')
elif len(strIn1) > len(strIn2):
    print('1>2')
else:
    print('1==2')

print(strIn1 + strIn2)
print(len((strIn1 + strIn2)))
