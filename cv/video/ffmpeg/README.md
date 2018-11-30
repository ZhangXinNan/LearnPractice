

-vf         是一个命令行，表示过滤图形的描述, 选择过滤器select会选择帧进行输出：包括过滤器常量pict_type和对应的类型:PICT_TYPE_I 表示是I帧，即关键帧。 
-vsync 2    阻止每个关键帧产生多余的拷贝 
-f image2 name_%02d.jpeg 
            将视频帧写入到图片中，样式的格式一般是:    “%d” 或者 “%0Nd” 
-qscale
-loglevel
-r          



ffmpeg [global_options] {[input_file_options] -i input_url} ... {[output_file_options] output_url} ...

ffmpeg -i [输入文件名] [参数选项] -f [格式] [输出文件] 

参数选项： 
(1) -an: 去掉音频 
(2) -vn: 去掉视频 
(3) -acodec: 设定音频的编码器，未设定时则使用与输入流相同的编解码器。音频解复用在一般后面加copy表示拷贝 
(4) -vcodec: 设定视频的编码器，未设定时则使用与输入流相同的编解码器，视频解复用一般后面加copy表示拷贝 
(5) –f: 输出格式（视频转码）
(6) -bf: B帧数目控制 
(7) -g: 关键帧间隔控制(视频跳转需要关键帧)
(8) -s: 设定画面的宽和高，分辨率控制(352*278)
(9) -i:  设定输入流
(10) -ss: 指定开始时间（0:0:05）
(11) -t: 指定持续时间（0:05）
(12) -b: 设定视频流量，默认是200Kbit/s
(13) -aspect: 设定画面的比例
(14) -ar: 设定音频采样率
(15) -ac: 设定声音的Channel数
(16)  -r: 提取图像频率（用于视频截图）
(17) -c:v:  输出视频格式
(18) -c:a:  输出音频格式
(18) -y:  输出时覆盖输出目录已存在的同名文件


-vcoder 设定视频的编码器，未设定时则使用与输入流相同的编解码器

作者：石先
链接：https://www.jianshu.com/p/91727ab25227
來源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。
[FFmpeg常用命令](https://www.jianshu.com/p/91727ab25227)

--------------------- 
作者：oneTaken 
来源：CSDN 
原文：https://blog.csdn.net/u011394059/article/details/78728809 
版权声明：本文为博主原创文章，转载请附上博文链接！
[ffmpeg 提取关键帧](https://blog.csdn.net/u011394059/article/details/78728809)

[H264编码原理以及I帧B帧P帧](http://blog.sina.com.cn/s/blog_4ad7c2540101me90.html)

[feixiao/ffmpeg](https://github.com/feixiao/ffmpeg/blob/master/src/B_FFmpeg%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97.md)