import time

# 获取当前时间戳
current_time = time.time()
time_struct = time.localtime(current_time)
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time_struct)

# 打印只显示到秒的时间
print("当前时间（只显示到秒）:", formatted_time)
