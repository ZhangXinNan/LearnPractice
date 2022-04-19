PP-YOLO: An Effective and Efficient Implementation of Object Detector

PP-YOLO：一种有效且高效的目标检测器实现

____


# 0 Abstract

Object detection is one of the most important areas in computer vision, which plays a key role in various practical scenarios. Due to limitation of hardware, it is often necessary to sacrifice accuracy to ensure the infer speed of the detector in practice. Therefore, the balance between effectiveness and efficiency of object detector must be considered. The goal of this paper is to implement an object detector with relatively balanced effectiveness and efficiency that can be directly applied in actual application scenarios, rather than propose a novel detection model. Considering that YOLOv3 has been widely used in practice, we develop a new object detector based on YOLOv3. We mainly try to combine various existing tricks that almost not increase the number of model parameters and FLOPs, to achieve the goal of improving the accuracy of detector as much as possible while ensuring that the speed is almost unchanged. Since all experiments in this paper are conducted based on PaddlePaddle, we call it PPYOLO. By combining multiple tricks, PP-YOLO can achieve a better balance between effectiveness (45.2% mAP) and efficiency (72.9 FPS), surpassing the existing state-of-the-art detectors such as EfficientDet and YOLOv4. Source code is at https://github.com/PaddlePaddle/PaddleDetection.


目标检测是计算机视觉中最重要的领域之一，在各种实际场景中发挥着关键作用。由于硬件的限制，实际中往往需要牺牲精度来保证检测器的推断速度。因此，必须考虑目标检测器的有效性和效率之间的平衡。本文的目标是实现一种有效性和效率相对平衡的目标检测器，可以直接应用于实际应用场景，而不是提出一种新颖的检测模型。考虑到 YOLOv3 已在实践中得到广泛应用，我们基于 YOLOv3 开发了一种新的目标检测器。我们主要尝试结合现有的各种几乎不增加模型参数数量和FLOPs的技巧，以达到在保证速度几乎不变的同时尽可能提高检测器精度的目标。由于本文所有的实验都是基于 PaddlePaddle 进行的，我们称之为 PPYOLO。通过结合多种技巧，PP-YOLO 可以在有效性（45.2% mAP）和效率（72.9 FPS）之间取得更好的平衡，超过了现有的最先进的检测器，例如 EfficientDet 和 YOLOv4。源代码位于 https://github.com/PaddlePaddle/PaddleDetection。
