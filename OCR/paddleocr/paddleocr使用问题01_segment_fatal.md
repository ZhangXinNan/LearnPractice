# 1 问题

```
--------------------------------------
C++ Traceback (most recent call last):
--------------------------------------
0   paddle::framework::SignalHandle(char const*, int)
1   paddle::platform::GetCurrentTraceBackString[abi:cxx11]()

----------------------
Error Message Summary:
----------------------
FatalError: `Segmentation fault` is detected by the operating system.
  [TimeInfo: *** Aborted at 1636622690 (unix time) try "date -d @1636622690" if you are using GNU date ***]
  [SignalInfo: *** SIGSEGV (@0x0) received by PID 18581 (TID 0x7f103bc4a700) from PID 0 ***]

段错误

```


# 2 解决方法


cuda 10.2，cudnn由8.1.0换成7.6.5



# 3 参考资料
[paddlepaddle-gpu 2.0.0rc1报FatalError: Segmentation fault is detected by the operating system.](https://github.com/PaddlePaddle/PaddleOCR/issues/1637)



