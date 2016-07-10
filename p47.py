# 這是第一個集合
itemsA = {"蘋果", "香蕉", "鳳梨", "芭樂"}
# 這是第二個集合
itemsB = {"鳳梨", "蘋果", "水梨", "蓮霧"}
list1 = list(itemsA.union(itemsB)-itemsA.intersection(itemsB))
list1.sort()
print(list1)