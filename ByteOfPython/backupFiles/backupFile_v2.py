import os
import time

target_dir = '/Users/ray/Desktop/backup'  # 备份主目录
source_dir = ['/Users/ray/Desktop/test']  # 源文件目录

if not os.path.exists(target_dir):  # 不存在备份目录，就创建
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime(
    '%Y%m%d')  # 在目标目录下生成以时间为命名的目录，例如在/Users/ray/Desktop/backup目录下生成一个名为20170217的目录名
now = time.strftime('%H%M%S')  # 生成当前时间串
target = today + os.sep + now + '.zip'  # 在今天的目录下生成目标文件名，如：111410.zip

if not os.path.exists(today):
    os.mkdir(today)
    print('Success mkdir:', today)  # /Users/ray/Desktop/backup/20170217

zip_command = 'zip -r {0} {1}'.format(target, ''.join(
    source_dir))  # zip -r /Users/ray/Desktop/backup/20170217/111059.zip /Users/ray/Desktop/test

print('Zip command is:')
print(zip_command)

if os.system(zip_command) == 0:
    print('Success Ziped')

else:
    print('Zip Failed')
