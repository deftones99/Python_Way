# 通过def定义函数
def say_hello():
    print("Hello 你好！")


# 调用函数
say_hello()


def compared(a, b):
    if a > b:
        print(a, "is bigger")
    elif a == b:
        print(a, "equal", b)
    else:
        print(a, "is small")


# 直接传递字面值
compared(3, 4)

# 通过参数传递
x = 4
y = 5

compared(x, y)
