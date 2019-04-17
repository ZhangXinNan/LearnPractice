CMake-Demo
=====


> 注：使用cmake时会生成很多临时文件，然而 cmake并没有像make clean一样好用的方法。常用的作法是在根目录下执行 
```bash
mkdir build && cd build
```
，创建build目录，然后切换到此目录下，执行cmake
```bash
cmake ..
```
 ，这样所有的临时文件都生成在了build下，这样只要删除build就干净了。

在 linux 平台下使用 CMake 生成 Makefile 并编译的流程如下：

1. 编写 CMake 配置文件 CMakeLists.txt 。
2. 执行命令 cmake PATH 或者 ccmake PATH 生成 Makefile。其中， PATH 是 CMakeLists.txt 所在的目录。
3. 使用 make 命令进行编译。
[注]ccmake 和 cmake 的区别在于前者提供了一个交互式的界面。

# 1 单个源文件
```bash
# CMake 最低版本要求
cmake_minimum_required (VERSION 2.8)

# 项目信息
project (Demo1)

# 指定生成目标。将名为 main.cc 的源文件编译成一个名称为 Demo 的可执行文件。
add_executable(Demo main.cc)
```

# 2 同一目录，多个源文件
```bash
# CMake 最低版本要求
cmake_minimum_required (VERSION 2.8)

# 项目信息
project (Demo2)

# 指定生成目标
# add_executable(Demo main.cc MathFunctions.cc)

# 查找当前目录下的所有源文件，并将名称保存到 DIR_SRCS 变量
aux_source_directory(. DIR_SRCS)

# 指定生成目标 
add_executable(Demo ${DIR_SRCS})

```

# 3 多个目录，多个源文件
将 MathFunctions.h 和 MathFunctions.cc 文件移动到 math 目录下。
## 3.1 主目录下CMakeLists.txt
```bash
# CMake 最低版本号要求
cmake_minimum_required (VERSION 2.8)

# 项目信息
project (Demo3)

# 查找目录下的所有源文件
# 并将名称保存到 DIR_SRCS 变量
aux_source_directory(. DIR_SRCS)

# 添加 math 子目录
add_subdirectory(math)

# 指定生成目标
add_executable(Demo ${DIR_SRCS})

# 添加链接库
target_link_libraries(Demo MathFunctions)
```
指明可执行文件main需要链接一个名为MathFunctions的链接库。


## 3.2 子目录下CMakeLists.txt
```
# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_LIB_SRCS 变量
aux_source_directory(. DIR_LIB_SRCS)

# 指定生成 MathFunctions 链接库
add_library (MathFunctions ${DIR_LIB_SRCS})

```
使用add_library 将src目录下的源文件编译为静态链接库

# 4 自定义编译选项
CMake 允许为项目增加编译选项，从而可以根据用户的环境和需求选择最合适的编译方案。
例如，可以将 MathFunctions 库设为一个可选的库，如果该选项为 ON ，就使用该库定义的数学函数来进行运算。否则就调用标准库中的数学函数库。

## 4.1 修改CMakeLists文件
```
# CMake 最低版本号要求
cmake_minimum_required (VERSION 2.8)

# 项目信息
project (Demo4)

# 加入一个配置头文件，用于处理 CMake 对源码的设置
configure_file (
  "${PROJECT_SOURCE_DIR}/config.h.in"
  "${PROJECT_BINARY_DIR}/config.h"
  )

# 是否使用自己的 MathFunctions 库
option (USE_MYMATH
	   "Use provided math implementation" ON)

# 是否加入 MathFunctions 库
if (USE_MYMATH)
  include_directories ("${PROJECT_SOURCE_DIR}/math")
  add_subdirectory (math)
  set (EXTRA_LIBS ${EXTRA_LIBS} MathFunctions )
endif (USE_MYMATH)

# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_SRCS 变量
aux_source_directory(. DIR_SRCS)

# 指定生成目标
add_executable (Demo ${DIR_SRCS})
target_link_libraries (Demo  ${EXTRA_LIBS})

```

其中：
1. 第7行的 configure_file 命令用于加入一个配置头文件 config.h ，这个文件由 CMake 从 config.h.in 生成，通过这样的机制，将可以通过预定义一些参数和变量来控制代码的生成。
2. 第13行的 option 命令添加了一个 USE_MYMATH 选项，并且默认值为 ON 。
3. 第17行根据 USE_MYMATH 变量的值来决定是否使用我们自己编写的 MathFunctions 库。

## 4.2 修改main.cc文件

## 4.3 编写 config.h.in 文件
```
#cmakedefine USE_MYMATH
```

## 4.4 编译项目
可以使用 ccmake 命令来编译，便于交互式的选择该变量的值

从中可以找到刚刚定义的 USE_MYMATH 选项，按键盘的方向键可以在不同的选项窗口间跳转，按下 enter 键可以修改该选项。修改完成后可以按下 c 选项完成配置，之后再按 g 键确认生成 Makefile 。ccmake 的其他操作可以参考窗口下方给出的指令提示。

# 5 安装与测试

CMake 也可以指定安装规则，以及添加测试。这两个功能分别可以通过在产生 Makefile 后使用 make install 和 make test 来执行。在以前的 GNU Makefile 里，你可能需要为此编写 install 和 test 两个伪目标和相应的规则，但在 CMake 里，这样的工作同样只需要简单的调用几条命令。

## 5.1 定制安装规则
## 5.2 为工程添加测试
## 5.3 添加环境检查

# 6 添加环境检查
## 6.1 添加 CheckFunctionExists 宏

## 6.2 预定义相关宏变量

## 6.3 在代码中使用宏和函数


# 7 添加版本号

# 8 生成安装包








# 参考
* [CMake 入门实战](https://www.hahack.com/codes/cmake/)
* [CMake 入门实战](http://hahack.com/codes/cmake) 的源代码。
此项目原地址为：https://coding.net/u/wzpan/p/cmake-demo/git
我将此库从coding.net搬过来，在此基础上增加了博客中内容到README.md文件中，便于阅读。
