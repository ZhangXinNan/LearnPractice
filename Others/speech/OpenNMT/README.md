

https://github.com/OpenNMT/OpenNMT-py

模型列表：https://opennmt.net/Models-py/#translation

conda create -n py39_opennmt python=3.9

conda activate py39_opennmt

pip install OpenNMT-py

onmt_translate -model /Users/zhangxin/nllb-200-600M-onmt.pt -src TheWaterCycle.txt -output TheWaterCycle_cn.txt -verbose
