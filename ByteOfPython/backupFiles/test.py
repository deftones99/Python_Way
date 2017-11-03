import os
import time

source_dir = '/Users/ray/Desktop/test'


target_dir = '/Users/ray/Desktop/test/backup'

target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = 'zip -r {0} {1}'.format(target,source_dir)

print(zip_command)