def test():
	r = ''
	while True:
		n = yield r
		if not n:
			return
		print('consumer {} '.format(n))
		r = 'ok'	

t = test()
print(next(t))
