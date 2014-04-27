import os
import os.path
import sys
from os.path import join, getsize, isfile

if len(sys.argv)<=1:
	print('请于调用时输入目标文件夹名')
	exit(-1)
for index in range(1,len(sys.argv)):
	target_dir = sys.argv[index]
	print('***********************************')
	print('文件夹'+target_dir+'使用情况统计')
	for f in os.listdir(target_dir):
		if f[0] == r'.':
			continue
		if os.path.isfile(join(target_dir,f)):
			print(join(target_dir,f),':',getsize(join(target_dir,f))/1024/1024,'M')
		if os.path.isdir(join(target_dir,f)):
			filesize = 0
			for root, dirs, files in os.walk(join(target_dir,f)):
				for name in files:
					filesize+=getsize(join(root,name))
		print('%s:%.1fMByte'%(join(target_dir,f),filesize/1024/1024))
print('***********************************')	
