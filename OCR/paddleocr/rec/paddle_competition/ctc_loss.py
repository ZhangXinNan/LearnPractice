
import paddle
from cfg import cfg



class CTCLoss(paddle.nn.Layer):
    def __init__(self):
        """
        定义CTCLoss
        """
        super().__init__()

    def forward(self, ipt, label):
        input_lengths = paddle.tensor.creation.fill_constant([ipt.shape[0]], "int64", ipt.shape[1])
        # 指定label中未padding的长度
        label_lengths = list()
        for i in range(label.shape[0]):
            idx = 0
            while label[i][idx] != cfg["classify_num"]-1:
                idx += 1
            label_lengths.append(idx)
        label_lengths = paddle.to_tensor(label_lengths, dtype="int64")
        # 按文档要求进行转换dim顺序
        ipt = paddle.tensor.transpose(ipt, [1, 0, 2])
        # 计算loss
        loss = paddle.nn.functional.ctc_loss(ipt, label, input_lengths, label_lengths, blank=cfg["classify_num"]-1)
        return loss