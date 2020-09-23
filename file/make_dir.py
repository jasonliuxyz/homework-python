import os

try:
	os.mkdir('/data/test')
	print(os.listdir('/data/test'))
# python3有FileExistsError
except FileExistsError as e:
	print(e)
