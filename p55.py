# fd1 = open('../app/stores_old.csv', 'r', encoding='big5')
fd1 = open('stores_old.csv', 'r', encoding='big5')
csvStr = fd1.readlines()
fd1.close()

# fd2 = open('../app/stores_new.csv', 'w', encoding='big5')
fd2 = open('stores_new.csv', 'w', encoding='big5')
for line in csvStr:
    # print(line)
    line = line.strip()
    line = line.split(',')
    writeList = [line[0], ',', line[3], ',', line[5], ',', line[6], ',']
    print(''.join(writeList))
    fd2.write(''.join(writeList) + '\n')
fd2.close()
