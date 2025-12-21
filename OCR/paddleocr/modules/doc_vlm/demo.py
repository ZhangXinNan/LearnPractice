
from paddleocr import DocVLM

model = DocVLM(model_name="PP-DocBee2-3B")
results = model.predict(
    input={"image": "medal_table.png", "query": "识别这份表格的内容, 以markdown格式输出"},
    batch_size=1
)
for res in results:
    res.print()
    res.save_to_json(f"./output/res.json")


