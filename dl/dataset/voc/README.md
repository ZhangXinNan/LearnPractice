参考资料：[PASCAL VOC数据集分析](https://blog.csdn.net/zhangjunbob/article/details/52769381)


解压后目录结构：
```
VOCdevkit
├── VOC2007
│   ├── Annotations
│   ├── ImageSets
│   ├── JPEGImages
│   ├── SegmentationClass
│   ├── SegmentationObject
│   └── labels
└── VOC2012
    ├── Annotations
    ├── ImageSets
    ├── JPEGImages
    ├── SegmentationClass
    ├── SegmentationObject
    └── labels
```

# ①JPEGImages
JPEGImages文件夹中包含了PASCAL VOC所提供的所有的图片信息，包括了训练图片和测试图片。
这些图像都是以“年份_编号.jpg”格式命名的。
图片的像素尺寸大小不一，但是横向图的尺寸大约在500*375左右，纵向图的尺寸大约在375*500左右，基本不会偏差超过100。（在之后的训练中，第一步就是将这些图片都resize到300*300或是500*500，所有原始图片不能离这个标准过远。）
这些图像就是用来进行训练和测试验证的图像数据。

# ②Annotations

Annotations文件夹中存放的是xml格式的标签文件，每一个xml文件都对应于JPEGImages文件夹中的一张图片。
```
<annotation>
	<folder>VOC2012</folder>                           
	<filename>2007_000392.jpg</filename>                               //文件名
	<source>                                                           //图像来源（不重要）
		<database>The VOC2007 Database</database>
		<annotation>PASCAL VOC2007</annotation>
		<image>flickr</image>
	</source>
	<size>					                           //图像尺寸（长宽以及通道数）						
		<width>500</width>
		<height>332</height>
		<depth>3</depth>
	</size>
	<segmented>1</segmented>		                           //是否用于分割（在图像物体识别中01无所谓）
	<object>                                                           //检测到的物体
		<name>horse</name>                                         //物体类别
		<pose>Right</pose>                                         //拍摄角度
		<truncated>0</truncated>                                   //是否被截断（0表示完整）
		<difficult>0</difficult>                                   //目标是否难以识别（0表示容易识别）
		<bndbox>                                                   //bounding-box（包含左下角和右上角xy坐标）
			<xmin>100</xmin>
			<ymin>96</ymin>
			<xmax>355</xmax>
			<ymax>324</ymax>
		</bndbox>
	</object>
	<object>                                                           //检测到多个物体
		<name>person</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>198</xmin>
			<ymin>58</ymin>
			<xmax>286</xmax>
			<ymax>197</ymax>
		</bndbox>
	</object>
</annotation>

```

# ③ImageSets

ImageSets存放的是每一种类型的challenge对应的图像数据。
在ImageSets下有四个文件夹：
```
VOCdevkit/VOC2007/ImageSets
├── Layout
├── Main
└── Segmentation


➜  voc tree VOCdevkit/VOC2012/ImageSets  -L 1
VOCdevkit/VOC2012/ImageSets
├── Action
├── Layout
├── Main
└── Segmentation
```

- Action下存放的是人的动作（例如running、jumping等等，这也是VOC challenge的一部分）
- Layout下存放的是具有人体部位的数据（人的head、hand、feet等等，这也是VOC challenge的一部分）
- Main下存放的是图像物体识别的数据，总共分为20类。
- Segmentation下存放的是可用于分割的数据。


Main文件夹下包含了20个分类的```***_train.txt、***_val.txt```和```***_trainval.txt```。
这些txt中的内容都差不多如下：
- 前面的表示图像的name，后面的1代表正样本，-1代表负样本。
- _train中存放的是训练使用的数据，每一个class的train数据都有5717个。
- _val中存放的是验证结果使用的数据，每一个class的val数据都有5823个。
- _trainval将上面两个进行了合并，每一个class有11540个。
- 需要保证的是train和val两者没有交集，也就是训练数据和验证数据不能有重复，在选取训练数据的时候 ，也应该是随机产生的。

# ④SegmentationClass和SegmentationObject

这两个文件夹下保存了物体分割后的图片，在物体识别中没有用到，在这里不做详细展开。

