
有时使用虚拟机报错VT-x is not available，怎么回事？ 通常情况下，报错的原因有3个：
1. VT-x 在 BIOS 中未被启用
2. CPU 不支持 VT-x 技术
3. Hyper-V 虚拟化在 windows 中已经被启用


解决办法
1. 启用 BIOS 中的 VT-x；
2. 禁用 Hyper-V ，用管理员身份运行以下命令

```bash
dism.exe /Online /Disable-Feature:Microsoft-Hyper-V # 禁用
dism.exe /Online /Enable-Feature:Microsoft-Hyper-V # 启用
```

# 参考
[虚拟机报错 “VT-x is not available”](https://www.jianshu.com/p/91acb5637a41)