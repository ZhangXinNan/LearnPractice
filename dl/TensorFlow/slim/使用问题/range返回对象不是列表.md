

# 问题
shuffled_index = range(len(filenames))


# 说明
python3 中range返回的是一个可迭代对象，所以要用list转成列表。

# 解决方法
shuffled_index = list(range(len(filenames)))