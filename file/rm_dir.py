import os

try:
	os.rmdir('/data/test/01/02')
except OSError as e:
	print(e)
