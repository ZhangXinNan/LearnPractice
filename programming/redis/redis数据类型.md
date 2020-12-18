
Redis支持五种数据类型：string（字符串），hash（哈希），list（列表），set（集合）及zset(sorted set：有序集合)。

# 1 string
string 类型的值最大能存储 512MB。
```bash
127.0.0.1:6379> set name "zhangxin"
# OK
127.0.0.1:6379> get name
# "zhangxin"
```

# 2 hash
Redis hash 是一个键值(key=>value)对集合。
Redis hash 是一个 string 类型的 field 和 value 的映射表，hash 特别适合用于存储对象。
```bash
127.0.0.1:6379> hmset p name "zhangxin" age 33
# OK
127.0.0.1:6379> hget p name 
# "zhangxin"
127.0.0.1:6379> hget p age
# "33"
```

实例中我们使用了 Redis HMSET, HGET 命令，HMSET 设置了两个 field=>value 对, HGET 获取对应 field 对应的 value。

每个 hash 可以存储 $2^{32}-1$ 键值对（40多亿）。

# 3 list
Redis 列表是简单的字符串列表，按照插入顺序排序。你可以添加一个元素到列表的头部（左边）或者尾部（右边）。
```bash
127.0.0.1:6379> lpush arr 5
# (integer) 1
127.0.0.1:6379> lpush arr 33
# (integer) 2
127.0.0.1:6379> lpush arr zhangxin
(integer) 3
127.0.0.1:6379> lrange arr 0 10
# 1) "zhangxin"
# 2) "33"
# 3) "5"
```


# 4 set
Redis 的 Set 是 string 类型的无序集合。

集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是 O(1)。
```bash
127.0.0.1:6379> sadd nums 1
# (integer) 1
127.0.0.1:6379> sadd nums 2
# (integer) 1
127.0.0.1:6379> sadd nums 3
# (integer) 1
127.0.0.1:6379> smembers nums
# 1) "1"
# 2) "2"
# 3) "3"
```

# 5 zset

```bash
127.0.0.1:6379> zadd money 0 zhangxin
# (integer) 1
127.0.0.1:6379> zadd money 0 cat
# (integer) 1
127.0.0.1:6379> zadd money 99 mayun
# (integer) 1
127.0.0.1:6379> zadd money 99 wang
# (integer) 1
127.0.0.1:6379> zrangebyscore money 0 1000
# 1) "cat"
# 2) "zhangxin"
# 3) "mayun"
# 4) "wang"
```

# 6 总结

类型 | 添加命令 | 查询命令
--|--|--
string（字符串）| set   | get
hash（哈希）    | hmset | hget
list（列表）    | lpush | lrange
set（集合）     | sadd  | smembers
zset(有序集合)  | zadd  | zrangebyscore





