import time

"""
#!/bin/bash
zip -e --password=`python -c "print(__import__('time').time())"` flag.zip flag
用Unix时间戳做密码给压缩包加密，得知道时间戳。
"""
# 2019-05-17 08:00:00 转换为Unix时间戳是 1558051200.0
# 2019-05-17 23:00:00 转换为Unix时间戳是 1558105200.0
struct_time1 = time.strptime("2019-05-17 08:00:00", "%Y-%m-%d %H:%M:%S")
time_stamp1 = time.mktime(struct_time1)
print(time_stamp1)
struct_time2 = time.strptime("2019-05-17 23:00:00", "%Y-%m-%d %H:%M:%S")
time_stamp2 = time.mktime(struct_time2)
print(time_stamp2)

local_time = time.localtime()
local_time_format = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print(local_time_format)
