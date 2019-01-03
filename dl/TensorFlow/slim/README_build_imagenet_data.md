
# 1 建立一个字典，图像名称->bounding box
image_to_bboxes = _build_bounding_box_lookup(bounding_box_file)


# 2 处理数据集——_process_dataset
_process_dataset('validation', FLAGS.validation_directory,
                   FLAGS.validation_shards, synset_to_human, image_to_bboxes)


## 2.1 获得每个图片的boxes——_find_image_bounding_boxes
bboxes = _find_image_bounding_boxes(filenames, image_to_bboxes)

## 2.2 处理文件——_process_image_files
_process_image_files(name, filenames, synsets, labels,
                       humans, bboxes, num_shards)


### 2.2.1 批量处理图片文件——_process_image_files_batch

#### 2.2.1.1 _process_image
#### 2.2.1.2 _convert_to_example

