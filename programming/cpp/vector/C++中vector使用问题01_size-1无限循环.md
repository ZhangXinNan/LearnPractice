

# 1 问题
在对一个vector进行循环处理时，例如排序，会经常这么写：
```c++
for (size_t i = 0; i < vec.size() - 1; i++) {
    for (size_t j = i + 1; j < vec.size(); j++) {
        // do something
    }
}
```

这里会出现无限循环。


# 2 分析
如果vec的元素数量为0，那么size_t类型的`i=0-1`，在计算里就变成了最大值，所以导致出现进入死循环的情况。

切记，不要犯这种低级错误。

# 3 解决办法
去掉减1即可。或者加个判断。
```bash
for (size_t i = 0; i < vec.size(); i++) {
    for (size_t j = i + 1; j < vec.size(); j++) {
        // do something
    }
}
```