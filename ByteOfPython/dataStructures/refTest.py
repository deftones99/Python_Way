# 对引用的测试
shopList = ['apple', 'bucket', 'pencil']

myList = shopList

shopList.append('car')

print(myList)  # ['apple', 'bucket', 'pencil', 'car']
print(shopList)  # ['apple', 'bucket', 'pencil', 'car']
print(myList == shopList)  # True

# 如果要创建一份序列的副本，必须要用切片操作来制作副本，如果仅将一个变量赋值给一个名称，那么他们是引用关系
myList = shopList[:]  # 制作完整的切片

del shopList[0]

print(shopList)  # ['bucket', 'pencil', 'car']
print(myList)  # ['apple', 'bucket', 'pencil', 'car']

print(myList == shopList)  # False
