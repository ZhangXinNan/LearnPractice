
# 一、依赖关系(Dependence)

依赖关系（Dependence）：假设A类的变化引起了B类的变化，则说名B类依赖于A类。

# 二、泛化关系（Generalization）

泛化关系（Generalization）：A是B和C的父类，B,C具有公共类（父类）A，说明A是B,C的一般化（概括，也称泛化）

# 三、关联关系（Association）

关联关系（Association）:类之间的联系，如客户和订单，每个订单对应特定的客户，每个客户对应一些特定的订单，再如篮球队员与球队之间的关联（下图所示）。

# 四、聚合关系（Aggregation）

聚合关系（Aggregation）:表示的是整体和部分的关系，整体与部分 可以分开.

# 五、组合关系（Composition）

组合关系（Composition）:也是整体与部分的关系，但是整体与部分不可以分开.


# 六、实现关系（Implementation)

实现关系（Implementation）：是用来规定接口和实线接口的类或者构建结构的关系，接口是操作的集合，而这些操作就用于规定类或者构建的一种服务。


# 分析
1. 泛化与实现：相当于继承类与实现接口
2. 聚合与组合：可分开与不可分开
3. 依赖与关联：A变化引起B变化，和，A与B有关系。

# 参考


[UML图中类之间的关系:依赖,泛化,关联,聚合,组合,实现](https://blog.csdn.net/hguisu/article/details/7609483)