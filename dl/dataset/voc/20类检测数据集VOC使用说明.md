

# 1 下载　voc pascal 训练数据和测试数据
```bash
wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtrainval_06-Nov-2007.tar
wget http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar
wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtest_06-Nov-2007.tar
```

创建　train 和　test　文件夹，然后解压文件
```bash
ls train/VOCdevkit/VOC2007/JPEGImages/ | wc -l
5011
ls train/VOCdevkit/VOC2012/JPEGImages/ | wc -l
17125
ls test/VOCdevkit/VOC2007/JPEGImages/ | wc -l
4952
```

目录结构为：
```bash
zhangxin@zhangxin-Alienware-17-R5:/media/zhangxin/DATA/data_public/VOC$ tree -L 4
.
├── test
│   └── VOCdevkit
│       └── VOC2007
│           ├── Annotations
│           ├── ImageSets
│           ├── JPEGImages
│           ├── SegmentationClass
│           └── SegmentationObject
├── train
│   └── VOCdevkit
│       ├── VOC2007
│       │   ├── Annotations
│       │   ├── ImageSets
│       │   ├── JPEGImages
│       │   ├── SegmentationClass
│       │   └── SegmentationObject
│       └── VOC2012
│           ├── Annotations
│           ├── ImageSets
│           ├── JPEGImages
│           ├── SegmentationClass
│           └── SegmentationObject
├── VOCtest_06-Nov-2007.tar
├── VOCtrainval_06-Nov-2007.tar
└── VOCtrainval_11-May-2012.tar

```

# 2 标注类别信息

## 2.3 图片
```bash
zhangxin@zhangxin-Alienware-17-R5:/media/zhangxin/DATA/data_public/VOC$ ls test/VOCdevkit/VOC2007/JPEGImages/*.jpg | wc -l
4952
zhangxin@zhangxin-Alienware-17-R5:/media/zhangxin/DATA/data_public/VOC$ ls train/VOCdevkit/VOC2007/JPEGImages/*.jpg | wc -l
5011
zhangxin@zhangxin-Alienware-17-R5:/media/zhangxin/DATA/data_public/VOC$ ls train/VOCdevkit/VOC2012/JPEGImages/*.jpg | wc -l
17125
```

## 2.2 文件列表分别存放在：
```
zhangxin@zhangxin-Alienware-17-R5:/media/zhangxin/DATA/data_public/VOC$ wc -l test/VOCdevkit/VOC2007/ImageSets/Main/test.txt
4952 test/VOCdevkit/VOC2007/ImageSets/Main/test.txt
zhangxin@zhangxin-Alienware-17-R5:/media/zhangxin/DATA/data_public/VOC$ wc -l train/VOCdevkit/VOC2007/ImageSets/Main/trainval.txt
5011 train/VOCdevkit/VOC2007/ImageSets/Main/trainval.txt
zhangxin@zhangxin-Alienware-17-R5:/media/zhangxin/DATA/data_public/VOC$ wc -l train/VOCdevkit/VOC2012/ImageSets/Main/trainval.txt
11540 train/VOCdevkit/VOC2012/ImageSets/Main/trainval.txt
```

## 2.3 标注文件：
```bash
zhangxin@zhangxin-Alienware-17-R5:/media/zhangxin/DATA/data_public/VOC$ ls test/VOCdevkit/VOC2007/Annotations | wc -l
4952
zhangxin@zhangxin-Alienware-17-R5:/media/zhangxin/DATA/data_public/VOC$ ls train/VOCdevkit/VOC2007/Annotations | wc -l
5011
zhangxin@zhangxin-Alienware-17-R5:/media/zhangxin/DATA/data_public/VOC$ ls train/VOCdevkit/VOC2012/Annotations | wc -l
17125
```


标注文件示例：
```xml
<annotation>
	<folder>VOC2007</folder>
	<filename>000001.jpg</filename>
	<source>
		<database>The VOC2007 Database</database>
		<annotation>PASCAL VOC2007</annotation>
		<image>flickr</image>
		<flickrid>341012865</flickrid>
	</source>
	<owner>
		<flickrid>Fried Camels</flickrid>
		<name>Jinky the Fruit Bat</name>
	</owner>
	<size>
		<width>353</width>
		<height>500</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>dog</name>
		<pose>Left</pose>
		<truncated>1</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>48</xmin>
			<ymin>240</ymin>
			<xmax>195</xmax>
			<ymax>371</ymax>
		</bndbox>
	</object>
	<object>
		<name>person</name>
		<pose>Left</pose>
		<truncated>1</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>8</xmin>
			<ymin>12</ymin>
			<xmax>352</xmax>
			<ymax>498</ymax>
		</bndbox>
	</object>
</annotation>
```


