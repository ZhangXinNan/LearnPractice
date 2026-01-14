from paddlex import PipelineClient

# 1. 初始化客户端，指向你服务运行的地址
client = PipelineClient(host="192.168.18.177", port=8080)

img_path = '/Users/zhangxin/gitlab/ocr_client/projects/screenshot/badcases/同花顺上海证券.png'
# 2. 调用预测接口
# 这里的 image 可以是：本地路径、URL、或者 numpy 数组
result = client.predict(
    # image="test_ocr_image.jpg"
    image=img_path
)

# 3. 解析结果
if result["status"] == "0":
    # 打印识别出的文字内容
    for item in result["result"]["texts"]:
        print(f"检测到文字: {item['text']}, 置信度: {item['score']:.2f}")
else:
    print(f"预测失败: {result['message']}")



