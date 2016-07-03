# string 基本組成
str1 = 'Hello, World'
print(str1)
print(str1[2:])
print(str1[0:7]+'The Beautiful'+str1[6:12])
print(str1[::1])
print(str1[::2])
print(str1[::-1])
print(str1[-1:0:-2])
# string split 切割
str2 = 'apple is a kind of fruit'
print(str2)
print(str2.split(sep=' '))
print(str2.split())
print(str2.split(sep=None))
print(str2.split(maxsplit=0))
print(str2.split(maxsplit=2))
print(str2.split(sep=None, maxsplit=4))
# string count 計數
str3 = 'A clear conscience laughs at false accusation.'
print(str3)
print(str3.count('a'))
print(str3.count('a',6))
print(str3.count('a',0,36))
# string find 搜尋
str4 = 'A friend in need is a friend indeed.'
print(str4)
print(str4.find('friend'))
print(str4.find('friend',3))
print(str4.find('friend',3,22)) #-1 代表找不到
# string replace 替代
str5 = 'A penny saved is a penny earned.'
print(str5)
print(str5.replace('n','l'))
print(str5.replace('penny','dollar'))
print(str5.replace('penny','dollar',1))
