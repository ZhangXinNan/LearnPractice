---
comments: true
hide:
  - toc
---

### `config.yaml`的生成

```bash linenums="1"
rapidocr config
```

### `default_rapidocr.yaml`常用参数介绍

#### Global

该部分为全局配置。

```yaml linenums="1"
Global:
    text_score: 0.5

    use_det: true
    use_cls: true
    use_rec: true

    min_height: 30
    width_height_ratio: 8
    max_side_len: 2000
    min_side_len: 30

    return_word_box: false
    return_single_char_box: false

    font_path: null
    log_level: "info" # debug / info / warning / error / critical
```

`text_score (float)`: 文本识别结果置信度，值越大，把握越大。取值范围：`[0, 1]`, 默认值是0.5。

`use_det (bool)`: 是否使用文本检测。默认为`True`。

`use_cls (bool)`: 是否使用文本行方向分类。默认为`True`。

`use_rec (bool)`: 是否使用文本行识别。默认为`True`。

`min_height (int)` : 图像最小高度（单位是像素），低于这个值，会跳过文本检测阶段，直接进行后续识别。默认值为30。`min_height`是用来过滤只有一行文本的图像（如下图），这类图像不会进入文本检测模块，直接进入后续过程。

![](https://github.com/RapidAI/RapidOCR/releases/download/v1.1.0/single_line_text.jpg)

`width_height_ratio (float)`: 如果输入图像的宽高比大于`width_height_ratio`，则会跳过文本检测，直接进行后续识别，取值为-1时：不用这个参数. 默认值为8。

`max_side_len (int)`: 如果输入图像的最大边大于`max_side_len`，则会按宽高比，将最大边缩放到`max_side_len`。默认为2000px。

`min_side_len (int)`: 如果输入图像的最小边小于`min_side_len`，则会按宽高比，将最小边缩放到`min_side_len`。默认为30px。

`return_word_box (bool)`: 是否返回文字的单字坐标。默认为`False`。

> 在`rapidocr>=2.1.0`中，纯中文、中英文混合返回单字坐标，纯英文返回单词坐标。

> 在`rapidocr<=2.0.7`中，纯中文、中英文混合和纯英文均返回单字坐标。

> 在`rapidocr_onnxruntime>=1.4.1`中，汉字返回单字坐标，英语返回单字母坐标。

> 在`rapidocr_onnxruntime==1.4.0`中，汉字会返回单字坐标，英语返回单词坐标。

`return_single_char_box (bool)`: 文本内容只有英文和数字情况下，是否返回单字坐标。默认为`False`。

> 在`rapidocr>=3.1.0`中添加该参数，该参数只有在`return_word_box=True`时，才能生效。

```python
result = engine(img_url, return_word_box=True, return_single_char_box=True)
```

`font_path (str)`: 字体文件路径。如不提供，程序会自动下载预置的字体文件模型到本地。默认为`null`。

`log_level (str)`: 日志级别设置。可选择的有`debug / info / warning / error / critical`，默认为`info`，会打印加载模型等日志。如果设置`critical`，则不会打印任何日志。

> 在`rapidocr>=3.4.0`中，才添加此参数。

#### EngineConfig

该部分为相关推理引擎的配置文件，大家可按需配置。该部分后面可能会增删部分关键字，如果有需求，可以在文档下面评论区指出。

```yaml linenums="1"
EngineConfig:
    onnxruntime:
        intra_op_num_threads: -1
        inter_op_num_threads: -1
        enable_cpu_mem_arena: false

        cpu_ep_cfg:
            arena_extend_strategy: "kSameAsRequested"

        use_cuda: false
        cuda_ep_cfg:
            device_id: 0
            arena_extend_strategy: "kNextPowerOfTwo"
            cudnn_conv_algo_search: "EXHAUSTIVE"
            do_copy_in_default_stream: true

        use_dml: false
        dm_ep_cfg: null

        use_cann: false
        cann_ep_cfg:
            device_id: 0
            arena_extend_strategy: "kNextPowerOfTwo"
            npu_mem_limit:  21474836480 # 20 * 1024 * 1024 * 1024
            op_select_impl_mode: "high_performance"
            optypelist_for_implmode: "Gelu"
            enable_cann_graph: true

    openvino:
        inference_num_threads: -1

    paddle:
        cpu_math_library_num_threads: -1
        use_npu: false  # rapidocr>=3.3.0
        npu_id: 0  # rapidocr>=3.3.0
        use_cuda: false
        gpu_id: 0
        gpu_mem: 500

    torch:
        use_cuda: false
        gpu_id: 0
        use_npu: false  # rapidocr>3.4.1
        npu_id: 0  # rapidocr>3.4.1
```

该部分的详细使用，请参见：[如何使用不同推理引擎？](./how_to_use_infer_engine.md)

各个推理引擎的API：

- ONNXRuntime Python API 参见：[Python API](https://onnxruntime.ai/docs/api/python/api_summary.html)
- OpenVINO Python API 参见：[OpenVINO Python API](https://docs.openvino.ai/2025/api/ie_python_api/api.html)
- PaddlePaddle API 参见：[API 文档](https://www.paddlepaddle.org.cn/documentation/docs/zh/api/index_cn.html)
- PyTorch API 参见：[PyTorch documentation](https://pytorch.org/docs/stable/index.html)

以下三部分前4个参数基本类似，对应关系如下表，具体请参见[模型列表](../../model_list.md)文档：

| YAML 参数       | 对应枚举类       | 可用枚举值（示例）                 |导入方式 | 备注                                |
|-----------------|------------------|------------------|-------------------|-------------------------------------|
| `engine_type`   | `EngineType`     | `ONNXRUNTIME`（onnxruntime）<br>`OPENVINO`（openvino）<br>`PADDLE`（paddle）<br>`TORCH`（torch） | `from rapidocr import EngineType`|推理引擎类型         |
| `lang_type`     |  `LangDet`<br> `LangCls`<br> `LangRec` | **检测（Det）**：`CH`/`EN`/`MULTI`<br>**分类（Cls）**：`CH`<br>**识别（Rec）**：`CH`/`CH_DOC`/`EN`/`ARABIC`/... |`from rapidocr import LangDet`<br/> `from rapidocr import LangCls` <br/>`from rapidocr import LangRec`| 根据OCR处理阶段选择不同枚举值 |
| `model_type`    | `ModelType`      | `MOBILE`（mobile）<br>`SERVER`（server） |`from rapidocr import ModelType`| 模型大小与性能级别      |
| `ocr_version`   | `OCRVersion`     | `PPOCRV4`（PP-OCRv4）<br>`PPOCRV5`（PP-OCRv5） |`from rapidocr import OCRVersion`| 模型版本    |

#### Det

```yaml linenums="1"
Det:
    engine_type: "onnxruntime"
    lang_type: "ch"
    model_type: "mobile"
    ocr_version: "PP-OCRv4"

    task_type: "det"

    model_path: null
    model_dir: null

    limit_side_len: 736
    limit_type: min
    std: [ 0.5, 0.5, 0.5 ]
    mean: [ 0.5, 0.5, 0.5 ]

    thresh: 0.3
    box_thresh: 0.5
    max_candidates: 1000
    unclip_ratio: 1.6
    use_dilation: true
    score_mode: fast
```

`engine_type (str)`: 选定推理引擎。支持`onnxruntime`、`openvino`、`paddle`和`torch`四个值。默认为`onnxruntime`。

`lang_type (str)`: 支持检测的语种类型。这里指的是`LangDet`，具体支持`ch`、`en`和`multi`3个值。`ch`可以识别中文和中英文混合文本检测。`en`支持英文文字检测。`multi`支持多语言文本检测。默认为`ch`。

`model_type (str)`: 模型量级选择，支持`mobile`（轻量型）和`server`（服务型）。默认为`mobile`。

`ocr_version (str)`: ocr版本的选择，支持`PP-OCRv4`和`PP-OCRv5`，默认为`PP-OCRv4`。

`model_path (str)`: 文本检测模型路径，仅限于基于PaddleOCR训练所得DBNet文本检测模型。默认值为`null`。

`model_dir (str)`: 模型存放路径或目录。如果是PaddlePaddle，该参数则对应模型存在目录。其余推理引擎请使用`model_path`参数。

`limit_side_len (float)`: 限制图像边的长度的像素值。默认值为736。

`limit_type (str)`: 限制图像的最小边长度还是最大边为`limit_side_len`。 示例解释：当`limit_type=min`和`limit_side_len=736`时，图像最小边小于736时，会将图像最小边拉伸到736，另一边则按图像原始比例等比缩放。 取值范围为：`[min, max]`，默认值为`min`。

`thresh (float)`: 图像中文字部分和背景部分分割阈值。值越大，文字部分会越小。取值范围：`[0, 1]`，默认值为0.3。

`box_thresh (float)`: 文本检测所得框是否保留的阈值，值越大，召回率越低。取值范围：`[0, 1]`，默认值为0.5。

`max_candidates (int)`: 最大候选框数目。默认是1000。

`unclip_ratio (float)`: 控制文本检测框的大小，值越大，检测框整体越大。取值范围：`[1.6, 2.0]`，默认值为1.6。

`use_dilation (bool)`: 是否使用膨胀。默认为`true`。该参数用于将检测到的文本区域做形态学的膨胀处理。

`score_mode (str)`: 计算文本框得分的方式。取值范围为：`[slow, fast]`，默认值为`fast`。

#### Cls

```yaml linenums="1"
Cls:
    engine_type: "onnxruntime"
    lang_type: "ch"
    model_type: "mobile"
    ocr_version: "PP-OCRv4"

    task_type: "cls"

    model_path: null
    model_dir: null

    cls_image_shape: [3, 48, 192]
    cls_batch_num: 6
    cls_thresh: 0.9
    label_list: ["0", "180"]
```

`engine_type (str)`: 同Det部分介绍。

`lang_type (str)`: 支持检测的语种类型。这里指的是`LangCls`，目前只有一种选项：`ch`。默认为`ch`。

`model_type (str)`: 同Det部分介绍。

`ocr_version (str)`: 同Det部分介绍。

`model_path (str)`: 文本行方向分类模型路径，仅限于PaddleOCR训练所得二分类分类模型。默认值为`None`。

`model_dir (str)`: 占位参数，暂时无效。

`cls_image_shape (List[int])`: 输入方向分类模型的图像Shape(CHW)。默认值为`[3, 48, 192]`。

`cls_batch_num (int)`: 批次推理的batch大小，一般采用默认值即可，太大并没有明显提速，效果还可能会差。默认值为6。

`cls_thresh (float)`: 方向分类结果的置信度。取值范围：`[0, 1]`，默认值为0.9。

`label_list (List[str])`: 方向分类的标签，0°或者180°，**该参数不能动** 。默认值为`["0", "180"]`。

#### Rec

```yaml linenums="1"
Rec:
    engine_type: "onnxruntime"
    lang_type: "ch"
    model_type: "mobile"
    ocr_version: "PP-OCRv4"

    task_type: "rec"

    model_path: null
    model_dir: null

    rec_keys_path: null
    rec_img_shape: [3, 48, 320]
    rec_batch_num: 6
```

`engine_type (str)`: 同Det部分介绍。

`lang_type (str)`: 支持检测的语种类型。这里指的是`LangRec`，具体支持的语种参见：[model_list](../../model_list.md).

`model_type (str)`: 同Det部分介绍。

`ocr_version (str)`: 同Det部分介绍。

`model_path (str)`: 文本识别模型路径，仅限于PaddleOCR训练文本识别模型。默认值为`None`。

`model_dir (str)`: 模型存放路径或目录。如果是PaddlePaddle，该参数则对应模型存在目录。其余推理引擎请使用`model_path`参数。

`rec_keys_path (str)`: 文本识别模型对应的字典文件，默认为`None`。

`rec_img_shape (List[int])`: 输入文本识别模型的图像Shape(CHW)。默认值为`[3, 48, 320]`。

`rec_batch_num (int)`: 批次推理的batch大小，一般采用默认值即可，太大并没有明显提速，效果还可能会差。默认值为6。



