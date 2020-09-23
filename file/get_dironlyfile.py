import os

basedir = '/data/code/file'
for entry in os.listdir(basedir):
	if os.path.isfile(os.path.join(basedir, entry)):
		print(entry)

with os.scandir(basedir) as entries:
	for entry in entries:
		if entry.is_file():
			print(entry.name)
