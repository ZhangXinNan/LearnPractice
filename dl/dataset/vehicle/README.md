

# The Comprehensive Cars 汽车图像数据
The Comprehensive Cars 是一个汽车图像数据集，图像有两个来源，一是网络图像，二是监控设备。网络图像包括 163个 汽车制造商，1716款 车型，136726幅 汽车图像，27618个 汽车零部件局部图像，同时具有汽车轮廓的标注，以及每个车型的 最大速度、偏移、门数、座数、汽车类型五个属性。另一类是来自监控设备拍摄的汽车正面图片，共 50000张。

数据结构：车辆数据结构为树形结构，包括三层，即车辆品牌，模型和出厂时间，不同年份生产的车辆只有细微差别，

车辆属性：每个型号的车辆使用五个属性标记，即最大速度，排量，车门数目，座位数目以及车型。定义了十二个车型，包括MPV, SUV, hatchback, sedan, minibus, fastback, estate, pickup, sports,crossover, convertible, and hardtop convertible,

视角：包含5个视角，即front (F), rear (R), side (S), front-side(FS), and rear-side (RS).

车辆局部：收集了每个型号车辆的8个局部图片，包括4个外部局部图片(i.e. headlight, taillight, fog light, and air intake)和4个内部局部图片(i.e. console, steering wheel, dashboard, and gear lever)


地址：[The Comprehensive Cars (CompCars) dataset](http://mmlab.ie.cuhk.edu.hk/datasets/comp_cars/index.html)
blog: [车型识别“A Large-Scale Car Dataset for Fine-Grained Categorization and Verification”](https://blog.csdn.net/cv_family_z/article/details/48136521)


