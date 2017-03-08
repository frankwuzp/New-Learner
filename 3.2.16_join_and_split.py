friends = ['Alice','Bob','Cathy']   #创建friends列表
separator = ' * '                   #定义分隔符号：*（为美观前后已加空格）
joined = separator.join(friends)    #将friends列表变成字符串
separated = separator.split(joined) #基于分隔符将字符串变成列表，即join的逆过程
separated == friends                #双等号测试逆运算是否成立