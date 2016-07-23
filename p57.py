fd = open('input.txt', 'r', encoding='big5')
txtStr = fd.readlines()
fd.close()

for line in txtStr:
    print(line.strip())