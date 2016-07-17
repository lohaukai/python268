# 以讀方式打開檔
f = open('text.txt', 'r')
# 讀取全部內容
print(f.read(), '\n')
# 關閉打開的文件
f.close()

f = open('text.txt', 'r')
for line in f.readlines():
    # 去掉每行頭尾空白
    line = line.strip()
    print(line)
# 關閉打開的文件
f.close()

# 打開一個檔
fo = open("write.txt", "w+")
fo.write("\nPython is a great language.\nYeah its great!!\n")
# 關閉打開的文件
fo.close()
# 執行完上面的程式碼，會在這個Python 檔案的路徑中新建一個write.txt
# 下面要再開啟這個檔，並且輸出這個檔的內容
fo = open("write.txt", "r")
for line in fo.readlines():
    line = line.strip()
    print(line)
fo.close()
