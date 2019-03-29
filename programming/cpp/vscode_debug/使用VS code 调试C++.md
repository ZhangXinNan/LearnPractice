

# 1 下载安装VSCODE，安装C/C++插件
点击左侧扩展图标，安装C/C++插件（ms-vscode.cpptools）。

# 2 配置调试和编译文件
安装c/c++扩展后，打开一个包含C/C++代码的文件夹，VS Code 将放一个设置文件到 .vscode 文件夹内。

# 3 配置智能提示
略

# 4 构建你的代码
1. 打开命令板(ctrl+shift+P)
2. 选择Tasks: Configure Task命令，点击 Create tasks.json files from templates,  and you will see a list of task runner templates.
3. Select Others to create a task which runs an external command.
4. Change the command to the command line expression you use to build your application (for example g++).
5. Add any required args (for example -g to build for debugging).
6. You can also change the label to be more descriptive.

# 参考
[Ubuntu下安装并配置VS Code编译C++](http://www.cnblogs.com/liutongqing/p/7069091.html)
[C/C++ for Visual Studio Code (Preview)](https://code.visualstudio.com/docs/languages/cpp)