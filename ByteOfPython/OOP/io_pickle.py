# 使用pickly模块转存文件
import pickle

shopListFile = 'shopList.data'

shopList = ['apple', 'banana', 'orange']

f = open(shopListFile, 'wb')

pickle.dump(shopList, f)

f.close()

del shopList

f = open(shopListFile, 'rb')

storedList = pickle.load(f)

print(storedList)
