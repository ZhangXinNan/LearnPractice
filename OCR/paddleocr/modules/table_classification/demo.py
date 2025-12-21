

from paddleocr import TableClassification
model = TableClassification(model_name="PP-LCNet_x1_0_table_cls")
output = model.predict("table_recognition.jpg", batch_size=1)
for res in output:
    res.print(json_format=False)
    res.save_to_json("./output/res.json")



