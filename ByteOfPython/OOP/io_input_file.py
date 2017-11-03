# 使用内置的open函数并指定名称来打开一个文件

poem = '''\
    编程使我快乐！
    程序是人类思想的映射
    哈哈1！
'''

f = open('peom.txt', 'w');

f.write(poem)

f.close()

f = open('peom.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break

    print(line, end='')
f.close()
