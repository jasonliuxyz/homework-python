import os

try:
	os.remove('/data/test/some_directory/tests.py')
except OSError as e:
	print(e)
