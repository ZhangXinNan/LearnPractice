## 问题
命令行下运行python脚本出现 
```
ImportError: No module named '_tkinter'
```

## 解决方法
添加如下代码：
```
import matplotlib as mpl
mpl.use('Agg')
```
