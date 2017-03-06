time_plus = 60*60
print(time_plus)               #一小时有多少秒
seconds_per_hour = time_plus   #赋值给变量seconds_per_hour
print(seconds_per_hour * 24)   #一天有多少秒
seconds_per_day = 24*60*60     #再次计算一天有多少秒，并赋值变量
a = seconds_per_day / seconds_per_hour
print(a)                       #浮点除法
b = seconds_per_day // seconds_per_hour
print(b)                       #整数除法