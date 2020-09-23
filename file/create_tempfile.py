# -*- encoding: utf-8 -*-

# 创建临时文件

import tempfile

fb = tempfile.TemporaryFile('w+t')
fb.write('test')
fb.seek(0)
data = fb.read()
print(data)
fb.close()
