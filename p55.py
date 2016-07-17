fileCsvOld = open('stores_old.csv', 'r', encoding='big5')
CsvOld = fileCsvOld.readlines()
fileCsvOld.close()

fileCsvNew = open('stores_new.csv', 'w+', encoding='big5')
for line in CsvOld:
    # print(line)
    line = line.strip()
    line = line.split(',')
    writeLine = [line[0], ',', line[3], ',', line[5], ',', line[6], ',', '\n']
    writeStr = ''.join(writeLine)
    print(writeStr)
    fileCsvNew.writelines(writeStr)
fileCsvNew.close()
