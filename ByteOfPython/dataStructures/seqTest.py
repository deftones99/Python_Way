shopList = ['banana', 'pear', 'mongo', 'apple']
name = 'deftones'

# 索引或者下标
print('Item 0 is:', shopList[0])
print('Item 1 is:', shopList[1])
print('Item 2 is:', shopList[2])
print('Item 3 is:', shopList[3])
print('Item -1 is:', shopList[-1])  # apple,从后至前
print('Item -2 is:', shopList[-2])  # mongo
print('Character 0 is:', name[0])  # 输出第一个字母

print()
# 切片
print('Item 1 to 2 is:', shopList[1:2])  # ['pear']
print('Item 2 to end is:', shopList[2:])  # ['mongo', 'apple']
print('Item 1 to -1 is:', shopList[1:-1])  # ['pear', 'mongo']
print('Item start to end is:', shopList[:])  # ['banana', 'pear', 'mongo', 'apple']

print()

print('Character 1 to 3 is:', name[1:3])  # ef
print('Character 2 to end is', name[2:])  # ftones
print('Character 1 to -1 is', name[1:-1])  # eftone
print('Character start to end', name[:])  # deftones

# 切片可指定第三个参数，步长
print(shopList[::1])
print(shopList[1::2])  # ['pear', 'apple'] 从1开始到结束，然后每2个取一个，shopList = ['banana', 'pear', 'mongo', 'apple']
# 从1开始是['pear', 'mongo', 'apple'],每两个为['pear','apple']
print(shopList[::-1]) #相当于倒序排列