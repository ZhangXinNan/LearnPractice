[FastDFS分布式文件系统安装与使用（单节点）](https://blog.csdn.net/xyang81/article/details/52837974)

# FastDFS文件上传流程：

1、client询问tracker上传到的storage，不需要附加参数； 
2、tracker返回一台可用的storage； 
3、client直接和storage通讯完成文件上传。

# FastDFS文件下载流程：

1、client询问tracker下载文件的storage，参数为文件标识（组名和文件名）； 
2、tracker返回一台可用的storage； 
3、client直接和storage通讯完成文件下载。