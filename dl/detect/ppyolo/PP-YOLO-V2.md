
PP-YOLOv2: A Practical Object Detector

PP-YOLOv2：实用的物体检测器

____


# 0 Abstract

Being effective and efficient is essential to an object detector for practical use. To meet these two concerns, we comprehensively evaluate a collection of existing refinements to improve the performance of PP-YOLO while almost keep the infer time unchanged. This paper will analyze a collection of refinements and empirically evaluate their impact on the final model performance through incremental ablation study. Things we tried that didn’t work will also be discussed. By combining multiple effective refinements, we boost PP-YOLO’s performance from 45.9% mAP to 49.5% mAP on COCO2017 test-dev. Since a significant margin of performance has been made, we present PP-YOLOv2. In terms of speed, PP-YOLOv2 runs in 68.9FPS at 640x640 input size. Paddle inference engine with TensorRT, FP16-precision and batch size = 1 further improves PP-YOLOv2’s infer speed, which achieves 106.5 FPS. Such a performance surpasses existing object detectors with roughly the same amount of parameters (i.e., YOLOv4-CSP, YOLOv5l). Besides, PP-YOLOv2 with ResNet101 achieves 50.3% mAP on COCO2017 test-dev. Source code is at https://github.com/PaddlePaddle/PaddleDetection.

有效和高效对于实际使用的对象检测器至关重要。为了解决这两个问题，我们综合评估了一系列现有改进，以提高 PP-YOLO 的性能，同时几乎保持推断时间不变。本文将分析一系列改进，并通过增量消融研究实证评估它们对最终模型性能的影响。我们尝试过但不起作用的事情也会被讨论。通过结合多种有效的改进，我们将 PP-YOLO 在 COCO2017 test-dev 上的性能从 45.9% mAP 提升到 49.5% mAP。由于已经取得了很大的性能优势，我们提出了 PP-YOLOv2。在速度方面，PP-YOLOv2 在 640x640 输入尺寸下以 68.9FPS 运行。具有 TensorRT、FP16-precision 和 batch size = 1 的 Paddle 推理引擎进一步提高了 PP-YOLOv2 的推理速度，达到 106.5 FPS。这样的性能超过了具有大致相同数量参数的现有对象检测器（即 YOLOv4-CSP、YOLOv5l）。此外，带有 ResNet101 的 PP-YOLOv2 在 COCO2017 test-dev 上实现了 50.3% 的 mAP。源代码位于 https://github.com/PaddlePaddle/PaddleDetection。