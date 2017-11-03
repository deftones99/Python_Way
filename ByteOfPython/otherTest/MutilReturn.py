# 通过元祖进行多重返回；要注意到 a, b = <some expression> 的用法会将表达式的结果解释为具有两个值的一个元组。
def mutil_return():
    return (2, 'jack')


return1, return2 = mutil_return()

print(return1)
print(return2)
