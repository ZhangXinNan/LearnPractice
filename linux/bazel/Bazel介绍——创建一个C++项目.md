# 使用Bazel构建
## 设置工作区（workspace）

在构建项目之前，需要设置其工作区。 工作区是保存项目源文件和Bazel构建输出的目录。 它还包含Bazel认为特殊的文件：

* WORKSPACE文件将目录及其内容标识为Bazel工作区，并居住在项目目录结构的根目录，

* 一个或多个BUILD文件，它告诉Bazel如何构建项目的不同部分。 （工作空间中包含BUILD文件的目录是一个包，您将在本教程中稍后了解包。）

要将目录指定为Bazel工作区，请在该目录中创建一个名为WORKSPACE的空文件。

当Bazel构建项目时，所有输入和依赖项必须在同一个工作空间中。 驻留在不同工作空间中的文件彼此独立，除非已经链接，这超出了本教程的范围。

## 了解BUILD文件

BUILD文件包含Bazel的几种不同类型的说明。 最重要的类型是构建规则，它告诉Bazel如何构建所需的输出，如可执行二进制文件或库。 BUILD文件中的构建规则的每个实例都称为目标，并指向一组特定的源文件和依赖关系。 目标也可以指向其他目标。

看看cpp-tutorial / stage1 / main目录下的BUILD文件：
```
cc_binary(
    name = "hello-world",
    srcs = ["hello-world.cc"],
)
```

在我们的例子中，hello-world目标实例化了Bazel的内置cc_binary规则。 该规则告诉Bazel从没有依赖关系的hello-world.cc源文件构建一个自包含的可执行二进制文件。

目标中的属性显式声明其依赖关系和选项。 虽然name属性是必需的，但很多是可选的。 例如，在hello-greet目标中，name是不言自明的，srcs指定Bazel构建目标的源文件。

## 建设项目

我们来构建您的示例项目。 更改为cpp-tutorial / stage1目录并运行以下命令：
```
bazel build // main：hello-world
```
注意目标标签 - // main：part是我们的BUILD文件相对于工作空间根目录的位置，hello-world是我们在BUILD文件中命名的目标。 （本教程结尾将更详细地了解目标标签。）

Bazel产生的输出类似于以下内容：

```
INFO: Found 1 target...
Target //main:hello-world up-to-date:
  bazel-bin/main/hello-world
INFO: Elapsed time: 2.267s, Critical Path: 0.25s
```
恭喜，您刚刚建立了您的第一个Bazel目标！ Bazel将构建输出放在工作区根目录下的bazel-bin目录中。 浏览其内容，了解Bazel的输出结构。

现在测试你新建的二进制文件：
```
bazel-bin/main/hello-world
```