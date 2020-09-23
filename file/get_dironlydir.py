import os

basedir = '/data/code'
for entry in os.listdir(basedir):
	if os.path.isdir(os.path.join(basedir, entry)):
		print(entry)

# python3
with os.scandir(basedir) as entries:
	for entry in entries:
		if entry.is_dir():
			print(entry.name)
