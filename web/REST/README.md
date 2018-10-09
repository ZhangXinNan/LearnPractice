[理解RESTful架构](http://www.ruanyifeng.com/blog/2011/09/restful.html)
[RESTful API 设计指南](http://www.ruanyifeng.com/blog/2014/05/restful_api.html)


REST，即Representational State Transfer的缩写。我对这个词组的翻译是"表现层状态转化"。

如果一个架构符合REST原则，就称它为RESTful架构。

# 资源（Resources）
　所谓"资源"，就是网络上的一个实体，或者说是网络上的一个具体信息。

# 表现层（Representation）
"资源"是一种信息实体，它可以有多种外在表现形式。我们把"资源"具体呈现出来的形式，叫做它的"表现层"（Representation）。

# 状态转化（State Transfer）
互联网通信协议HTTP协议，是一个无状态协议。这意味着，所有的状态都保存在服务器端。因此，如果客户端想要操作服务器，必须通过某种手段，让服务器端发生"状态转化"（State Transfer）。而这种转化是建立在表现层之上的，所以就是"表现层状态转化"。

# 综述

综合上面的解释，我们总结一下什么是RESTful架构：

　　（1）每一个URI代表一种资源；

　　（2）客户端和服务器之间，传递这种资源的某种表现层；

　　（3）客户端通过四个HTTP动词，对服务器端资源进行操作，实现"表现层状态转化"。