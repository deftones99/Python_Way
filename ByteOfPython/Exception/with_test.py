# 通过使用with，它会获取由open语句返回的对象，它总会在代码块开始之前调用 thefile.__enter__ 函数，
# 并且总会在代码块执行完毕之后调用 thefile.__exit__ 。
# 因此，我们在 finally 代码块中编写的代码应该格外留心 __exit__ 方法的自动操作。这能
# 够帮助我们避免重复显式使用 try..finally 语句。
import sys
import time

with open('peom.txt') as f:
    for line in f:
        print(line, end='')
