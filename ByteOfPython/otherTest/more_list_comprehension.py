#  列表推导
#  当满足了某些条件时( if i > 2 )，我们进行指定的操作( 2*i )，以此来获 得一份新的列表。要注意到原始列表依旧保持不变。


listone = [2, 3, 4]

listtwo = [2 * i for i in listone if i > 2]

print(listtwo)


# pow函数接受两到三个参数，接收两个参数时：x**y，是x的y次方，三个参数时：x**y%z，x的y次方对z取余
def powersum(power, *args):
    total = 0
    for i in args:
        total += pow(i, power)
    return total


print(powersum(2, 3, 4))
print(pow(3, 4))
print(pow(3, 4, 5))  # 3的4次方对5取余为1
