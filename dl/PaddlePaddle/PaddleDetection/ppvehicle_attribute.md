
```bash
# 车辆颜色
- "yellow"
- "orange"
- "green"
- "gray"
- "red"
- "blue"
- "white"
- "golden"
- "brown"
- "black"

# 车型
- "sedan"       # n. 轿车；轿子
- "suv"         # abbr. 运动型多用途汽车 (sport utility vehicle)；小型单层水泡 
- "van"         # n. （厢式）小型货车
- "hatchback"   # n. 仓门式汽车，掀背式汽车
- "mpv"         # abbr. 多用途车辆（Multi-Purpose Vehicle）
- "pickup"      # n. 小卡车，轻型货车（=pickup truck）
- "bus"
- "truck"       # n. 卡车
- "estate"      # 旅行车；客货两用轿车
```


python deploy/pipeline/pipeline.py \
    --config deploy/pipeline/config/infer_cfg_ppvehicle_attr.yml \
    --image_file=/home/zhangxin/gitlab/auto_client/test/badcase/多车.jpg \
    --device=gpu




