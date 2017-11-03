# 通过__name__属性确定该模块是否被导入运行，如果它与__main__属性相同，代表着该模块由用户独立运行，否则是从其他模块导入而来
if __name__ == '__main__':
    print('This program is being run by itself')

else:
    print('This program is imported from another module')