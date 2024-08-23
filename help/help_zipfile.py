import zipfile

"""
zipfile模块实现zip文件压缩和解压缩
"""

# 压缩2个py文件到compress.zip文件
zf = zipfile.ZipFile('compress.zip', 'w')
zf.write('help_mysql.py')
zf.write('help_pymysql.py')
zf.close()

# 解压缩compress.zip到文件夹decompress
zfd = zipfile.ZipFile('compress.zip', 'r')
zfd.extractall('decompress')
zfd.close()
