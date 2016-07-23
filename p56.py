# fd = open('../app/stores_old.csv', 'r', encoding='big5')
fd = open('stores_old.csv', 'r', encoding='big5')
csvStr = fd.readlines()
fd.close()

for line in csvStr:
    print(line.strip())
