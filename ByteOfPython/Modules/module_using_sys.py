# 打印出Python的环境变量
import sys

print('The commond line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

# 查看当前程序所在的目录
import os

print(os.getcwd())