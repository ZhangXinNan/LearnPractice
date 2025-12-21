

from paddleocr import ChartParsing
model = ChartParsing(model_name="PP-Chart2Table")
results = model.predict(
    input={"image": "chart_parsing_02.png"},
    batch_size=1
)
for res in results:
    res.print()
    res.save_to_json(f"./output/res.json")


