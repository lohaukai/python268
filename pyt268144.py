#a = eval(input())
#b = eval(input())

a = 10
b = 20
print('1:%d, 2:%d' %(a, b))

dict1 = {'na': a, 'nb' : b}
print('1:%(nb)d, 2:%(na)d' %dict1)

# dict2 = {a:88, b:99} 字典會用數字10與20為索引
# print('1:%(a)d, 2:%(b)d' %dict2) 索引為數字無法執行
dict2 = {str(a):88, str(b):99}
print('1:%(10)d, 2:%(20)d' %dict2)

eval(input())