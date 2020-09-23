import os

dir = os.listdir('/data/code')
print(dir)

dir = os.scandir('/data/code')
with dir as entries:
	for entry in entries:
		print(type(entry))
		print(entry.name)
