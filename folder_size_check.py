import os
import os.path
from os.path import join, getsize, isfile

target_dir = r'C:\Program Files (x86)\Common Files'	
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
		print(join(target_dir,f),':',filesize/1024/1024,'M')

