import os, fnmatch, glob

basepath='/data/test/some_directory'

#for f in os.listdir(basepath):
	#if f.endswith('.txt'):
	#	print(f)
	
	#if fnmatch.fnmatch(f, 'data_*_backup.txt'):
	#	print(f)

# 类似linux中find命令，glob返回的是列表	
for name in glob.glob('/data/test/some_directory/admin.py'):
	print(name)

