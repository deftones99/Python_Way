# 字符串的用法
name = 'Deftones'
if name.startswith('Def'):
    print('Yes')

if 'on' in name:
    print('Yes')

if name.find('es'):
    print('Yes')

if name.find('es') != -1:
    print('Yes')

delimiter = '_&_&_*'

myBookList = ['jack', 'roes', 'john']
print(delimiter.join(myBookList))  # jack_&_&_*roes_&_&_*john
