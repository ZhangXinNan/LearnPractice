
如果你想显示一段在线视频或者任意的数据流比如视频或者OpenGL 场景，你可以用android中的TextureView做到。

# 1 SurfaceView ——————（TextureView的兄弟）
应用程序的视频或者opengl内容往往是显示在一个特别的UI控件中：SurfaceView。SurfaceView的工作方式是**创建一个置于应用窗口之后的新窗口**。这种方式的效率非常高，因为**SurfaceView窗口刷新的时候不需要重绘应用程序的窗口**（android普通窗口的视图绘制机制是一层一层的，任何一个子元素或者是局部的刷新都会导致整个视图结构全部重绘一次，因此效率非常低下，不过满足普通应用界面的需求还是绰绰有余），但是SurfaceView也有一些非常不便的限制。

因为SurfaceView的内容不在应用窗口上，所以不能使用变换（平移、缩放、旋转等）。也难以放在ListView或者ScrollView中，不能使用UI控件的一些特性比如View.setAlpha()。

为了解决这个问题 Android 4.0中引入了TextureView。

# 2 TextureView

与SurfaceView相比，**TextureView并没有创建一个单独的Surface用来绘制**，这使得它可以像一般的View一样执行一些变换操作，设置透明度等。另外，**Textureview必须在硬件加速开启的窗口中**。

TextureView的使用非常简单，你唯一要做的就是获取用于渲染内容的SurfaceTexture。具体做法是先创建TextureView对象，然后实现SurfaceTextureListener接口，代码如下：

```java
public class LiveCameraActivity extends Activity implements TextureView.SurfaceTextureListener {
      private Camera mCamera;
      private TextureView mTextureView;

      protected void onCreate(Bundle savedInstanceState) {
          super.onCreate(savedInstanceState);

          mTextureView = new TextureView(this);
          mTextureView.setSurfaceTextureListener(this);

          setContentView(mTextureView);
      }

      public void onSurfaceTextureAvailable(SurfaceTexture surface, int width, int height) {
          mCamera = Camera.open();

          try {
              mCamera.setPreviewTexture(surface);
              mCamera.startPreview();
          } catch (IOException ioe) {
              // Something bad happened
          }
      }

      public void onSurfaceTextureSizeChanged(SurfaceTexture surface, int width, int height) {
          // Ignored, Camera does all the work for us
      }

      public boolean onSurfaceTextureDestroyed(SurfaceTexture surface) {
          mCamera.stopPreview();
          mCamera.release();
          return true;
      }

      public void onSurfaceTextureUpdated(SurfaceTexture surface) {
          // Invoked every time there's a new Camera preview frame
      }
  }
 
```


Activity implements SurfaceTextureListener接口因此activity中需要重写如下方法：
```java
@Override
public void onSurfaceTextureAvailable(SurfaceTexture arg0, int arg1, int arg2) {
}
@Override
public boolean onSurfaceTextureDestroyed(SurfaceTexture arg0) {
}
@Override
public void onSurfaceTextureSizeChanged(SurfaceTexture arg0, int arg1,int arg2) {
}
@Override
public void onSurfaceTextureUpdated(SurfaceTexture arg0) {
}
```


TextureView可以使用setAlpha和setRotation方法达到改变透明度和旋转的效果。
```java
myTexture.setAlpha(1.0f);
myTexture.setRotation(90.0f);
```

除了上面的方法之外，TextureView 还有如下方法：

序号 |	方法 | 描述
-- | -- | --
1	| getSurfaceTexture()                       | This method returns the SurfaceTexture used by this view.
2	| getBitmap(int width, int height)          | This method returns Returns a Bitmap representation of the content of the associated surface texture.
3	| getTransform(Matrix transform)            | This method returns the transform associated with this texture view.
4	| isOpaque()                                | This method indicates whether this View is opaque.
5	| lockCanvas()                              | This method start editing the pixels in the surface
6	| setOpaque(boolean opaque)                 | This method indicates whether the content of this TextureView is opaque.
7	| setTransform(Matrix transform)            | This method sets the transform to associate with this texture view.
8	| unlockCanvasAndPost(Canvas canvas)        | This method finish editing pixels in the surface.


# 3 与SurfaceView再次对比

既然TextureView与SurfaceView一样都可以在其它线程中进行UI更新，并且还有SurfaceView做不到的移动，透明度变化等设置，那么是不是就可以让TextureView代替SurfaceView呢。

这就要先讲讲这个两个View：

1. SurfaceView提供一个嵌入在视图层次上的专用绘制表面，我们可以控制该表面（Surface）的格式和尺寸。SurfaceView负责将表面放置在屏幕上正确的位置。它的行为多少有些类似于传统桌面系统上的onscreen窗口，比如，X11系统中的XWindow可以是无边框的，嵌入在另一个XWindow中。

2. SurfaceView存在如下两个缺点：
* 不能应用动画、变换和缩放
* 不能叠加（Overlay）两个SurfaceView

TextureView看似更像一个通用的View，可以应用动画、变换和缩放，就如同TextView。TextureView只能用在硬件加速的窗口。但是，TextureView比SurfaceView更耗内存，而且可能会有1～3帧的延迟。

所以在使用的时候要斟酌两者的不同。

# 4 TextureView的相关类SurfaceTexture
* Surface就是SurfaceView中使用的Surface，就是内存中的一段绘图缓冲区。 
* SurfaceTexture是什么呢，官方文档给出的解释是这样的：
SurfaceTexture用来捕获视频流中的图像帧的，视频流可以是相机预览或者视频解码数据。SurfaceTexture可以作为android.hardware.camera2, MediaCodec, MediaPlayer, 和 Allocation这些类的目标视频数据输出对象。可以调用updateTexImage()方法从视频流数据中更新当前帧，这就使得视频流中的某些帧可以跳过。
TextureView可以通过getSurfaceTexture()方法来获取TextureView相应的SurfaceTexture。但是最好的方式还是使用TextureView.SurfaceTextureListener监听器来对SurfaceTexture的创建销和毁进行监听，因为getSurfaceTexture可能获取的是空对象。




# 参考
* [TextureView](https://developer.android.com/reference/android/view/TextureView)
* [Android TextureView简易教程](http://www.jcodecraeer.com/a/anzhuokaifa/androidkaifa/2014/1213/2153.html)
* [Android控件--TextureView](https://blog.csdn.net/HardWorkingAnt/article/details/72784044)
* [Android-TextureView的原理分析及使用](https://blog.csdn.net/u013068887/article/details/79326893)
* [TextureView、SurfaceTexture、Surface](https://blog.csdn.net/Holmofy/article/details/66583879)



