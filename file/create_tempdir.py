# -*- encoding: utf-8 -*-
#创建临时目录

import tempfile

dir = tempfile.TemporaryDirectory()
print('create temporary directory', dir)
print(os.path.exists(dir))
