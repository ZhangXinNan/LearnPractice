
- 1 Rust基础知识
  - 1.1 安装&&更新
  - 1.2 编译器与包管理工具以及开发环境搭建
  - 1.3 获取Rust库、国内源以及Windows、Linux、Mac的不同
- 2 变量与常见数据类型
  - 2.1 变量与不可变性
  - 2.2 常量const与静态变量static
  - 2.3 Rust基础数据类型
  - 2.4 元组与数组
- 3 Ownership与结构体、枚举
  - 3.1 Rust的内存管理模型
  - 3.2 String与&str
  - 3.3 枚举与匹配模式
  - 3.4 结构体、方法、关联函数、关联变量
  - 3.5 Ownership与结构体
  - 3.6 堆与栈、Copy与Move
- 4 流程控制与函数
  - 4.1 if 流程控制与match模式匹配
  - 4.2 循环与break/continue以及迭代的区别
  - 4.3 函数基础与Copy值参数传递
  - 4.4 函数值参数传递、不可变借用参数传递、可变借用参数传递
  - 4.5 函数返回值与所有权机制
  - 4.6 高阶函数、函数作为参数与返回值
- 5 Error错误处理
  - 5.1 Result/Option/panic!宏
  - 5.2 unwrap()与'?'
  - 5.3 自定义一个Error类型
- 6 Borrowing借用与lifetime生命周期
  - 6.1 Borrowing&&Borrow Checker&&lifetime
  - 6.2 Lifetime与函数
  - 6.3 lifetime与Struct
- 7 泛型
  - 7.1 Generic Structures
  - 7.2 Generic Function
- 8 特质
  - 8.1 Trait 特质
  - 8.2 Trait Object与Box
  - 8.3 Trait Object与泛型
  - 8.4 重载操作符Operator
  - 8.5 Trait 与多态、继承
  - 8.6 常用的Trait
- 9 迭代器
  - 9.1 迭代与循环
  - 9.2 Intolterator/Iterator和Iter之间的关系
  - 9.3 获取迭代器的三种方法iter()、iter_mut()和Into_iter()
  - 9.4 自定义类型实现iter()/iter_mut()/into_iter()
- 10 闭包
  - 10.1 闭包基础概念
  - 10.2 闭包获取参数by reference 与by value
  - 10.3 闭包是怎么工作的
  - 10.4 闭包类型FnOnce、FnMut与Fn做函数参数的实例




Rust特点：
1. 安全。独一元二的所有权机制。
2. 性能。
3. 零成本抽象。
4. 完备的函数式编程。

