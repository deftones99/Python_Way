# 可以通过在函数定义时附加一个赋值运算符（=）来为参数指定默认的参数值，注意默认参数值通常应为常量，更准确的说默认参数值应该是不可改变的
# 注意，只有那些位于参数列表末尾的参数才能被赋予默认参数值，def say(a,b,5)有效，def say2(a=2,b)是无效的

def defalut_funcation(message, times=1):
    print(message * times)


defalut_funcation("Hello")
defalut_funcation("Hello", 3)


