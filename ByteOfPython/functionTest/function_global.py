x = 50


def func():
    global x  # 设置x为全局变量
    print("x is ", x)  # 使用主程序中的x的值，为50
    x = 2  # 将全局变量的值改变影响了主程序中的x的值
    print("x is change to ", x)


func()
print("value of x is", x)
