
# 1 查看图片



# 2 摄像头拍照
参考：
* 《第一行代码》第二版

1. activity_main.xml 中添加ImageView控件，一个按钮控件
2. 按钮注册上点击事件，在点击事件里调用摄像头的逻辑。
2.1 创建File对象，用于存放拍的图片，存在应用关联缓存目录下。
2.2 
（1）系统版本低于7.0，将file对象转换成Uri对象，这个对象标识着图片的本地真实路径；
（2）高于7.0，调用 FileProvider的getUriForFile()方法将File对象转换成Uri对象。
2.3 
（1）构建一个Intent对象，其action指定为android.media.action.IMAGE_CAPTURE;
（2）调用 Intent的putExtra()指定图片的输出地址；
（3）startActivityForResult() 启动活动。

3. 在AndroidManifest.xml中对内容提供器进行注册。
4. 声明SD卡的访问权限。


# 3 查看视频
1. activity_main.xml 中添加 VideoView控件。VideoView的父类是android.view.SurfaceView。
2. MainActivity类实现View.OnClickListener接口。（响应事件用）
3. onCreate() 运行时权限处理，用户同意授权才能调用视频路径。
4. AndroidManifest.xml中声明用到的权限。
5. onDestroy() 方法中，调用 videoView.suspend()将VideoView占用的资源释放掉。



# 4 摄像头预览
推荐使用android.hardware.camera2

参考代码：
* [lb377463323/GraphicsTestBed  Camera/CameraV2/](https://github.com/lb377463323/GraphicsTestBed/tree/master/Camera/CameraV2)
* [ZhangXinNan/GraphicsTestBed](https://github.com/ZhangXinNan/GraphicsTestBed)

## 4.0 AndroidManifest.xml 
1.1 Camera Permission - Your application must request permission to use a device camera. 
```xml
<uses-permission android:name="android.permission.CAMERA" />
```

1.2 Camera Features - Your application must also declare use of camera features, for example:
```xml
<uses-feature android:name="android.hardware.camera" />
```

1.3 Storage Permission - If your application saves images or videos to the device's external storage (SD Card), you must also specify this in the manifest.
```xml
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```

1.4  Audio Recording Permission - For recording audio with video capture, your application must request the audio capture permission.
```xml
<uses-permission android:name="android.permission.RECORD_AUDIO" />
```



## 4.1 定义TextView作为 预览界面


## 4.2 设置相机 参数


## 4.3 开启相机

## 4.4 开启相机预览

## 4.5 实现PreviewCallback

## 4.6 拍照 


# 5 视频录制


# 参考
* [Android Camera2教程之打开相机、开启预览、实现PreviewCallback、拍照](https://blog.csdn.net/lb377463323/article/details/52740411)
* [lb377463323/GraphicsTestBed  Camera/CameraV2/](https://github.com/lb377463323/GraphicsTestBed/tree/master/Camera/CameraV2)


