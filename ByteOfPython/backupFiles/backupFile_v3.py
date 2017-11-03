import os
import time

source_dir = ['/Users/q/Desktop/test']

target_dir = '/Users/q/Desktop/backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = input('Enter a comment:')

if len(comment) == 0:
    target = today + os.sep + now + '.zip'

else:
    target = today + os.sep + now + '_' + comment + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully create a directory', today)

zip_command = 'zip -r {0} {1}'.format(target, ''.join(source_dir))

print('Zip command is :')
print(zip_command)

print('Running:')
if os.system(zip_command) == 0:
    print('Successfully ziped!')

else:
    print('Zip failed!')