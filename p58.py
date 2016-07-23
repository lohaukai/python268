# fd = open('../app/stores_old.csv', 'r', encoding='big5')
fd = open('stores_old.csv', 'r', encoding='big5')
csvStr = fd.readlines()
fd.close()

for line in csvStr:
    line = line.strip()
    line = line.split(',')
    if line[3] == '公館門市':
        print(','.join(line))
