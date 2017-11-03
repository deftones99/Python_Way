address = {
    'jack': 'jack@126.com',
    'rose': 'rose@gmail.com',
    'john': 'john99@163.com'
}

print(address)
print('There are {} contacts in the address book'.format(len(address)))
print('jack\'s address is:', address['jack'])

# 删除一堆键值
del address['john']

print(address)

print('There are {} contacts in the address book'.format(len(address)))

# 循环打印出address里的信息
for name, email in address.items():
    print('Contact {} at {}'.format(name, email))

# 添加一对键值
address['matt'] = 'mattStar*@122.com'
print(address)
if 'matt' in address:
    print('matt\'s email is {}'.format(address['matt']))

#print(address[2])
