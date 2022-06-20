
Monocular, One-stage, Regression of Multiple 3D People

单目、一阶段、多个 3D 人物的回归

_____

# 0 Abstract 概要


This paper focuses on the regression of multiple 3D people from a single RGB image. Existing approaches predominantly follow a multi-stage pipeline that first detects people in bounding boxes and then independently regresses their 3D body meshes. In contrast, we propose to Regress all meshes in a One-stage fashion for Multiple 3D People (termed ROMP). The approach is conceptually simple, bounding box-free, and able to learn a per-pixel representation in an end-to-end manner. Our method simultaneously predicts a Body Center heatmap and a Mesh Parameter map, which can jointly describe the 3D body mesh on the pixel level. Through a body-center-guided sampling process, the body mesh parameters of all people in the image are easily extracted from the Mesh Parameter map. Equipped with such a fine-grained representation, our one-stage framework is free of the complex multi-stage process and more robust to occlusion. Compared with state-of-the-art methods, ROMP achieves superior performance on the challenging multi-person benchmarks, including 3DPW and CMU Panoptic. Experiments on crowded/occluded datasets demonstrate the robustness under various types of occlusion. The released code is the first real-time implementation of monocular multi-person 3D mesh regression.



本文着重于从单个 RGB 图像中对多个 3D 人物进行回归。现有方法主要遵循多阶段管道，首先检测边界框中的人，然后独立地回归他们的 3D 身体网格。相比之下，我们建议对多个 3D 人物（称为 ROMP）以单阶段方式对所有网格进行回归。该方法在概念上很简单，无边界框，并且能够以端到端的方式学习每个像素的表示。我们的方法同时预测了一个身体中心热图和一个网格参数图，它们可以在像素级别上共同描述 3D 身体网格。通过身体中心引导的采样过程，图像中所有人的身体网格参数很容易从网格参数图中提取出来。配备了如此细粒度的表示，我们的单阶段框架摆脱了复杂的多阶段过程，并且对遮挡更加健壮。与最先进的方法相比，ROMP 在具有挑战性的多人基准测试（包括 3DPW 和 CMU Panoptic）上取得了卓越的性能。在拥挤/遮挡数据集上的实验证明了在各种遮挡下的鲁棒性。发布的代码是单目多人3D网格回归的第一个实时实现。



