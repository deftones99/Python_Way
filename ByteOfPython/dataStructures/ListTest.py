# 列表是一种用于保存一系列有序项目的集合，列表使用方括号
aList = ['a', 'b', 'c', 4]

print(aList)

aList.append('5')

print(aList)

bList = ['e','f','g']

aList.append(bList)
# aList.sort()

# ['a', 'b', 'c', 4, '5', ['e', 'f', 'g']]
print(aList)