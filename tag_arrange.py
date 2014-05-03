import os
import os.path
import sys
import subprocess
from os.path import join, getsize, isfile

if len(sys.argv)!=4:
	print('usage:python tag_arrange.py tag_name(argv1) current_dir target_dir')
	exit(-1)
	
for f in os.listdir(sys.argv[2]):
	if f[0] == r'.':
		continue
	if os.path.isfile(join(sys.argv[2],f)):
		if sys.argv[1] in f:
			print('File '+join(sys.argv[2],f)+' matched!')
			ps = subprocess.Popen(["move",join(sys.argv[2],f),join(sys.argv[3],f)],  shell=True);
			ps.wait();
	if os.path.isdir(join(sys.argv[2],f)):
		for root, dirs, files in os.walk(join(sys.argv[2],f)):
			#print('root:',root,'dirs:',dirs,'files:',files)
			if root == sys.argv[3]:
				continue
			for cur_file in files:
				if sys.argv[1] in cur_file:
					print('File '+join(root,cur_file)+'matched in subdir!')
					#os.system("move "+join(root,cur_file)+" "+join(sys.argv[3],cur_file))
					ps = subprocess.Popen(["move",join(root,cur_file),join(sys.argv[3],cur_file)],  shell=True);
					ps.wait();
