shopList = ['apple', 'pear', 'banana', 'carrot', 'mongo']

# 使用end参数，可以通过一个空格来结束输出，而不是通常的换行
print('I have', len(shopList), ' items to buy')
print('These items are:', end=' ')
for i in shopList:
    print(i, end=' ')

print('\nI also want to buy rice')

shopList.append('rice')

print('Now my shopList is :', shopList)
print('I want to sort my shopList')
shopList.sort()
print('Now my shopList is sorted like:', shopList)
print('First i will to buy is:', shopList[0])
oldItem = shopList[0]
del shopList[0]
print('I bought the :', oldItem)
print('Now my shopList is:', shopList)
