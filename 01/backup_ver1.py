import os
import time


source = ['/Users/ios3/Desktop/test_backup/source']
target_dir = '/Users/ios3/Desktop/test_backup'

# os.sep 分隔符
targe = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command = 'zip -r {0} {1}'.format(targe, ''.join(source))

print('zip command is')
print(zip_command)
print('Runing')

if os.system(zip_command) == 0:
    print('Successful backup to', targe)
else:
    print('backup Failed')