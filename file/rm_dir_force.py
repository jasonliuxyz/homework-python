import shutil

basepath='/data/test/01/02'

try:
	shutil.rmtree(basepath)
except OSError as e:
	print('Error:{basepath}:{}'.format(e.strerror))

