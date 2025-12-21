
from paddleocr import TableCellsDetection
model = TableCellsDetection(model_name="RT-DETR-L_wired_table_cell_det")
output = model.predict("table_recognition.jpg", threshold=0.3, batch_size=1)
for res in output:
    res.print(json_format=False)
    res.save_to_img("./output/")
    res.save_to_json("./output/res.json")



