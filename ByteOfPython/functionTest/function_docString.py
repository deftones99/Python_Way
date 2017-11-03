# 测试使用函数的__doc__属性
def print_max(x, y):
    '''Print the maximum of two numbers,The two numbers must be integer.哈哈'''
    #'''Print shit'''
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')


#print_max(3, 4)
print(print_max.__doc__)

help(print_max)