
# 一、简介
CameraManager 是系统服务之一，专门用于 检测 和 打开相机，以及 获取相机设备特性。

官方文档其实说的蛮清楚的了，英文好的同学也可以直接看官方文档把：https://developer.android.google.cn/reference/android/hardware/camera2/CameraManager

# 二、获取 CameraManager 实例
通过 Context 类的 getSystemService() 方法来获取一个系统服务，参数使用 Context.CAMERA_SERVICE 或 CameraManager.class 都行。
```java
// 方式一
CameraManager manager = (CameraManager) context.getSystemService(Context.CAMERA_SERVICE);
// 方式二
CameraManager manager = (CameraManager) context.getSystemService(CameraManager.class);
```


# 三、内部类
CameraManager 中包含两个公有的内部类，分别为：

## 1. CameraManager.AvailabilityCallback
当一个相机设备的可用状态发生变化时，就会回调这个类的 onCameraAvailable(String cameraId) 和 onCameraUnavailable(String cameraId) 方法。

## 2. CameraManager.TorchCallback
当一个相机设备的闪光灯的 Torch 模式可用状态发生变化时，就会回调这个类的 onTorchModeChanged(String cameraId, boolean enabled) 和 onTorchModeUnavailable(String cameraId) 方法。

通过 setTorchMode(String cameraId, boolean enabled) 方法设置 Torch 模式。

# 四、常用方法
其中第二条和第三条是重点的重点，一定要掌握的。

## 1. String[] getCameraIdList()
获取当前连接的相机设备列表，这个 id 通常都是从 0 开始并依次递增的。

对于一般的手机而言:

后置摄像头一般为 “0”，常量值为 CameraCharacteristics.LENS_FACING_FRONT；
前置摄像头一般为 “1”，常量值为 CameraCharacteristics.LENS_FACING_BACK。

## 2. CameraCharacteristics getCameraCharacteristics(String cameraId)
根据 cameraId 获取对应相机设备的特征。返回一个 CameraCharacteristics，类比于旧 API 中的 Camera.Parameter 类，里面封装了相机设备固有的所有属性功能。

## 3. void openCamera(String cameraId, final CameraDevice.StateCallback callback, Handler handler)
打开指定的相机设备，该方法使用当前进程 uid 继续调用 openCameraForUid(cameraId, callback, handler, USE_CALLING_UID) 方法。

参数解释：
1. cameraId ： 需要打开的相机 id。
2. callback ： 回调类，常用如下几个回调方法。
* onOpened(CameraDevice camera) 成功打开时的回调，此时 camera 就准备就绪，并且可以得到一个 CameraDevice 实例。
* onDisconnected(CameraDevice camera) 当 camera 不再可用或打开失败时的回调，通常在该方法中进行资源释放的操作。
* onError(CameraDevice camera, int error) 当 camera 打开失败时的回调，error 为具体错误原因，定义在 CameraDevice.StateCallback 类中。通常在该方法中也要进行资源释放的操作。
3. handler ： 指定回调执行的线程。传 null 时默认使用当前线程的 Looper，我们通常创建一个后台线程来处理。
使用示例：
```java
    private int mCameraId = CameraCharacteristics.LENS_FACING_FRONT;
    private CameraManager mCameraManager; // 相机管理者
    private CameraDevice mCameraDevice; // 相机对象
    private Handler mBackgroundHandler;
    private HandlerThread mBackgroundThread;

    private CameraDevice.StateCallback mStateCallback = new CameraDevice.StateCallback() {
        @Override
        public void onOpened(@NonNull CameraDevice camera) {
            mCameraDevice = camera;
            // 当相机成功打开时回调该方法，接下来可以执行创建预览的操作
        }
        @Override
        public void onDisconnected(@NonNull CameraDevice camera) {
            // 当相机断开连接时回调该方法，应该在此执行释放相机的操作
        }
        @Override
        public void onError(@NonNull CameraDevice camera, int error) {
            // 当相机打开失败时，应该在此执行释放相机的操作
        }
    };

    public void openCamera() {
        try {
            // 前处理
            mCameraManager.openCamera(Integer.toString(mCameraId), mStateCallback, mBackgroundHandler);
        } catch (CameraAccessException e) {
            e.printStackTrace();
        }
    }
```


后台线程创建示例：
```java
    private void startBackgroundThread() {
        mBackgroundThread = new HandlerThread("CameraBackground");
        mBackgroundThread.start();
        mBackgroundHandler = new Handler(mBackgroundThread.getLooper());
    }

    private void stopBackgroundThread() {
        mBackgroundThread.quitSafely();
        try {
            mBackgroundThread.join();
            mBackgroundThread = null;
            mBackgroundHandler = null;
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
```

## 4. void registerAvailabilityCallback(AvailabilityCallback callback, Handler handler)
注册一个 AvailabilityCallback 回调，handle 指定处理回调的线程，传 null 时默认使用当前线程的 Looper。
```java
CameraManager cameraManager = (CameraManager) context.getSystemService(Context.CAMERA_SERVICE);
cameraManager.registerAvailabilityCallback(new CameraManager.AvailabilityCallback() {
    @Override
    public void onCameraAvailable(@NonNull String cameraId) {
        super.onCameraAvailable(cameraId);
    }

    @Override
    public void onCameraUnavailable(@NonNull String cameraId) {
        super.onCameraUnavailable(cameraId);
    }
}, mBackgroundHandler);
```

## 5. void unregisterAvailabilityCallback(AvailabilityCallback callback)
注销 AvailabilityCallback 回调，当回调不再需要时一定要注销，否则将带来内存泄漏的问题。

## 6. void registerTorchCallback(TorchCallback callback, Handler handler)
注册一个 TorchCallback 回调，handle 解释如上。
```java
CameraManager cameraManager = (CameraManager) context.getSystemService(Context.CAMERA_SERVICE);
cameraManager.registerTorchCallback(new CameraManager.TorchCallback() {
    @Override
    public void onTorchModeUnavailable(@NonNull String cameraId) {
        super.onTorchModeUnavailable(cameraId);
    }

    @Override
    public void onTorchModeChanged(@NonNull String cameraId, boolean enabled) {
        super.onTorchModeChanged(cameraId, enabled);
    }
}, mBackgroundHandler);
```


## 7. void unregisterTorchCallback(TorchCallback callback)
注销 TorchCallback 回调，当回调不再需要时一定要注销，否则将带来内存泄漏的问题。

## 8. void setTorchMode(String cameraId, boolean enabled)
打开和关闭指定相机设备的闪光灯功能。


# 参考

* [Android Camera2 之 CameraManager 详解](https://blog.csdn.net/afei__/article/details/85342160)


