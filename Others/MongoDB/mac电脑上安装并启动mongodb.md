在 macOS 上安装并启动 MongoDB 的完整步骤如下，假设你使用的是 **Intel 或 Apple Silicon 的 Mac** 且安装了 **Homebrew**。

---

## ✅ 一、安装 MongoDB（使用 Homebrew）

1. **更新 Homebrew**

```bash
brew update
```

2. **添加 MongoDB 官方源**

```bash
brew tap mongodb/brew
```

3. **安装 MongoDB 社区版**

```bash
brew install mongodb-community@7.0
```

> 注：你也可以安装其他版本，如 `@6.0` 或 `@5.0`，根据需要修改版本号。

---

```bash
mongod --version
db version v8.0.12
Build Info: {
    "version": "8.0.12",
    "gitVersion": "b60fc6875b5fb4b63cc0dbbd8dda0d6d6277921a",
    "modules": [],
    "allocator": "system",
    "environment": {
        "distarch": "aarch64",
        "target_arch": "aarch64"
    }
}
```

## ✅ 二、启动 MongoDB 服务

### 方法一：使用 Homebrew 启动服务（推荐）

```bash
brew services start mongodb/brew/mongodb-community@7.0
```

> 这个命令会让 MongoDB 随系统启动自动运行。

### 方法二：手动启动

```bash
mongod --config /opt/homebrew/etc/mongod.conf
```

> 如果你使用的是 Intel Mac，可能路径是 `/usr/local/etc/mongod.conf`。

---

## ✅ 三、验证 MongoDB 是否启动成功

```bash
ps aux | grep mongod
```

或

```bash
lsof -i :27017
```

默认 MongoDB 使用端口 `27017`，如果你看到监听状态就是启动成功了。

---

## ✅ 四、连接 MongoDB

打开另一个终端窗口：

```bash
mongosh
```

如果一切正常，你会进入 MongoDB shell：

```
test> show dbs;
admin   40.00 KiB
config  12.00 KiB
local   40.00 KiB
```

---

## ✅ 五、停止 MongoDB

```bash
brew services stop mongodb/brew/mongodb-community@7.0
```

---

## ⚠️ 如果出错怎么办？

* 使用 `mongod --dbpath <your_path>` 指定数据库路径手动运行。

  ```bash
  mongod --dbpath /usr/local/var/mongodb
  ```
* 确保这个路径存在：

  ```bash
  mkdir -p /usr/local/var/mongodb
  ```
* 有权限问题的话加 `sudo`，或确保当前用户对该目录有读写权限。

---

需要我一步步指导安装、看报错，欢迎贴出你终端中的输出信息。


