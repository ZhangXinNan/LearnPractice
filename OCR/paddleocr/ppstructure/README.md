
# Environment Preparation
## 1.1 Install PaddlePaddle

## 1.2 Install PaddleOCR
```bash
# Install paddleocr, version 2.6 is recommended
pip3 install "paddleocr>=2.6"

# Install the image direction classification dependency package paddleclas (if you do not use the image direction classification, you can skip it)
pip3 install paddleclas>=2.4.3

# Install the KIE dependency packages (if you do not use the KIE, you can skip it)
pip3 install -r kie/requirements.txt

# Install the layout recovery dependency packages (if you do not use the layout recovery, you can skip it)
pip3 install -r recovery/requirements.txt
```

# PP-Structure

1. layout analysis：divide the image into different areas such as text, table, and figure, and then analyze these areas separately.
2. form recognition module
3. OCR engine
4. the layout recovery module

# model
```json
'PP-Structurev2': {
            'table': {
                'en': {
                    'url':
                    'https://paddleocr.bj.bcebos.com/ppstructure/models/slanet/en_ppstructure_mobile_v2.0_SLANet_infer.tar',
                    'dict_path': 'ppocr/utils/dict/table_structure_dict.txt'
                },
                'ch': {
                    'url':
                    'https://paddleocr.bj.bcebos.com/ppstructure/models/slanet/ch_ppstructure_mobile_v2.0_SLANet_infer.tar',
                    'dict_path': 'ppocr/utils/dict/table_structure_dict_ch.txt'
                }
            },
            'layout': {
                'en': {
                    'url':
                    'https://paddleocr.bj.bcebos.com/ppstructure/models/layout/picodet_lcnet_x1_0_fgd_layout_infer.tar',
                    'dict_path':
                    'ppocr/utils/dict/layout_dict/layout_publaynet_dict.txt'
                },
                'ch': {
                    'url':
                    'https://paddleocr.bj.bcebos.com/ppstructure/models/layout/picodet_lcnet_x1_0_fgd_layout_cdla_infer.tar',
                    'dict_path':
                    'ppocr/utils/dict/layout_dict/layout_cdla_dict.txt'
                }
            }
        }
```