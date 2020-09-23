#-*- encoding: utf-8 -*-
import datetime, os

def timestamp2datetime(timestamp, convert_to_local=True, utc=8, is_remove_ms=True):
	if is_remove_ms:
		timestamp = int(timestamp)
	# timestamp转换为datetime
	dt = datetime.datetime.utcfromtimestamp(timestamp)
	if convert_to_local:
		dt = dt + datetime.timedelta(hours=utc)
	return dt

basepath = '/data/code/file'
with os.scandir(basepath) as entries:
	for entry in entries:
		if entry.is_file():
			info = entry.stat()
			print('{} 上次修改时间 {}'.format(entry.name, timestamp2datetime(info.st_mtime)))
