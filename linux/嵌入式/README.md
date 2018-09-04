[搞懂单片机、ARM、MUC、DSP、FPGA、嵌入式的关系](https://forum.mianbaoban.cn/topic/62762_1_1.html)

# 嵌入式（Embedded）
区别于PC通用的系统，嵌入式是个专用系统，结构精简，在硬件和软件上只保留需要的部分。具有便携、低功耗、性能单一等特性

# MCU(微控制单元(Micro Control Unit))
俗称单片机，必须顺序执行。
ARM是一家专门设计MCU的公司，ARM的单片机有很多种类，从低端M0（小家电）到高端A8/A9（手机平板电脑）。

# DSP(数字信号处理器（digital signal processor）)
数字信号处理器，结构与MCU不同，加快了运算速度，可以看成一个超级快的MCU。
- 低端DSP主要用的电机控制上，TI称为DSC（数字信号控制器）一个介于MCU和DSP之间的东西。
- 高端的DSP，是做视频图像处理和通信设备这类大量运算的地方。

# FPGA(Field Programmable Gate Array现场可编程逻辑闸阵列)
现场可编程逻辑阵列，本身没什么功能，完全靠编程人员设计。
由于MCU和DSP的内部结构是设计好的，只能通过软件编程来进行顺序处理，而FPGA可以并行处理和顺序处理，速度最快。



