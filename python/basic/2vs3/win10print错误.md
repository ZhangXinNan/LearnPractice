[在python中使用print（）时，raw write（）返回无效的长度：OSError: raw write() returned invalid length 254 (should have been between 0 and 127)](https://www.cnblogs.com/yanjj/p/8275995.html)


事先要看你是否
```pip install win_unicode_console```,没有，就赶快动手
```
import win_unicode_console
win_unicode_console.enable()
```