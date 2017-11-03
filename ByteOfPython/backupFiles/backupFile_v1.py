import os
import time

source_dir = ['/Users/ray/Desktop/test']  # 源目录
target_dir = '/Users/ray/Desktop/test/backup'  # 目标目录

target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip'  # 生成的备份文件名,os.sep会根据系统的不同生成不同的分隔符，time.strftime会按照给定的参数生成时间串

if not os.path.exists(target_dir):  # 如果没有该目标目录
    os.mkdir(target_dir)  # 则创建一个新目录

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source_dir))  # 生成zip命令，其中的-r代表为递归的对目录进行工作

print('Zip command is:', zip_command)
print('Running')

if os.system(zip_command) == 0:  # os.system可以使命令可以像是从系统中shell工作一样的执行命令，如成功了则返回0，否则返回错误代码
    print('Success backup in:', target_dir)

else:
    print('Backup Failed')
