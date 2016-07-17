def input_num(argv1, argv2):
    print(argv1, argv2)
    return max(argv1)

list1 = []
list2 = []
for i in range(3):
    list1.append(eval(input()))
for i in range(3):
    list2.append(eval(input()))
print(input_num(list1, list2))

