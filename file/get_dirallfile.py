# -*- encoding: utf-8 -*-
import os

# 遍历目录
for dirpath, dirname, files in os.walk('/data/', topdown=False):
	print('Found directory: {}'.format(dirpath))
	for file in files:
		print(file)
