人体关键点检测现在已经有比较清晰的"经典算法 → 高精度模型 → 实时工程模型 → 全身/手部/面部扩展”的演进路线。做项目时，不建议从零实现算法，更推荐直接基于成熟开源框架起步。

里程碑式算法与论文
阶段   代表算法   为什么重要
经典热图回归   Stacked Hourglass   确立“编码器-下采样 + 解码器-上采样 + 跳跃连接 + 热图回归”范式，是早期单人姿态估计的重要基线

实时多人检测   OpenPose   首次实现实时多人 2D 姿态估计，引入 Part Affinity Fields 关联关键点，支持身体、手、脸等多部位

高分辨率表示   HRNet   全程保持高分辨率表征，并通过多尺度融合提升关键点定位精度，后来被广泛用于姿态估计骨干网络

Transformer 基线   ViTPose / ViTPose+   把 Vision Transformer 引入姿态估计，在 COCO 上取得很高精度，成为高精度姿态估计的重要基线

实时工程化   RTMPose / RTMO   RTMPose 是 OpenMMLab 面向实时部署的姿态估计框架；RTMO 进一步做单阶段多人实时姿态估计，适合工程落地

全身关键点   DWPose / MediaPipe Pose   DWPose 针对全身、手部、面部关键点做了优化，常用于 ControlNet 姿态控制；MediaPipe Pose 适合端侧实时单人姿态追踪

多人高精度 + 跟踪   AlphaPose   早期高精度多人姿态估计与跟踪系统，适合遮挡、人群密集场景

值得看的代表性论文

Stacked Hourglass Networks：ECCV 2016，热图回归与多尺度特征融合的经典工作。
OpenPose：CVPR 2017，实时多人姿态估计与 PAF 关联方法。
HRNet：CVPR 2019，高分辨率表示学习，姿态估计骨干网络常用。
ViTPose：NeurIPS 2022，Vision Transformer 姿态估计基线。
ViTPose+：TPAMI 2023，扩展到更通用的身体姿态估计。
RTMPose：OpenMMLab 实时姿态估计工作，关注速度、精度与部署优化。
AlphaPose：多人姿态估计与跟踪系统，COCO/MPII 上早期表现突出。
DWPose：面向全身关键点检测，常用于 ControlNet OpenPose 预处理。

常用开源代码与框架
开源项目   特点   适合场景
MMPose   OpenMMLab 姿态估计工具箱，模型多，支持 2D/3D、单人/多人、训练/推理/部署   研究、定制训练、服务器部署

OpenPose   经典多人姿态估计库，支持身体/手/脸/脚关键点   学习经典方法、需要脚部关键点

MediaPipe Pose   Google 端侧实时方案，安装简单，支持 CPU/GPU   Web/移动端/实时交互

YOLO Pose   Ultralytics YOLO 生态内置姿态模型，单阶段推理快   快速落地、已有 YOLO 项目

RTMPose / RTMO   OpenMMLab 实时姿态模型，CPU/GPU/ONNX 部署友好   实时视频、边缘设备、产品化

DWPose   全身 133 点关键点，手/脸/脚更完整   AI 绘图、全身动作控制、细粒度姿态

AlphaPose   多人高精度姿态估计 + 跟踪   拥挤人群、体育分析、动作跟踪

ViTPose   高精度 Transformer 姿态基线   离线高精度分析、科研对比

如果要做项目，建议这样选

1. 最快上手：MediaPipe Pose / YOLO Pose

想 1 小时内跑通 demo，选 MediaPipe Pose。
想 多人实时检测，并且已经熟悉 YOLO，选 YOLOv8/YOLO11 Pose。
优点：安装简单、推理快、文档多。
缺点：MediaPipe 主要适合单人；YOLO Pose 关键点通常是 COCO 17 点，手脸细节有限。

2. 最稳妥通用：MMPose + RTMPose / RTMO

想 训练自己的数据、换骨干网络、做部署，优先选 MMPose。
需要实时多人检测，可以用 RTMO；需要更高精度 Top-Down 方案，可以用 RTMPose。
优点：模型库完整，支持 ONNX/TensorRT/OpenVINO 部署，社区活跃。
缺点：配置系统比 MediaPipe/YOLO 复杂一点。

3. 需要手/脸/全身细节：DWPose

做 ControlNet、虚拟人驱动、舞蹈/手势分析，选 DWPose。
它输出 COCO-WholeBody 133 点，手部关键点质量明显优于传统 OpenPose 方案。

4. 需要高精度离线分析：ViTPose / HRNet

做 医疗康复、动作评估、科研对比，可以用 ViTPose 或 HRNet。
精度高，但计算量大，通常需要 GPU。

我的推荐组合

如果只选几个快速入手：

入门 demo / 实时交互：MediaPipe Pose
多人实时项目：YOLO Pose 或 RTMO
想训练、定制、部署：MMPose + RTMPose
需要全身/手部/面部关键点：DWPose
做高精度离线分析或科研：ViTPose / HRNet

如果只有一个推荐：先用 MMPose。它既能直接调用 RTMPose、RTMO、HRNet、ViTPose 等模型，也方便后续替换骨干网络、训练自定义数据集和导出部署模型。

需要我为你提供一份基于MMPose的实战代码模板，帮你快速跑通第一个demo吗？