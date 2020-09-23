import os

try:
	os.makedirs('/data/test/01/02', mode=0o770)
except FileExistsError as e:
	print(e)
