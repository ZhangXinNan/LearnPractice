

```java
//        File out_dir = new File(Environment.getExternalStorageDirectory().toString());
        //[LOG 打印]		/storage/emulated/0 可以运行，通过adb shell可以找到，但是不知道怎么导出视频。

//		File out_dir = getExternalCacheDir();
        //[LOG 打印]		/storage/emulated/0/Android/data/com.example.cameratest/cache adb shell可以找到，但是不知道怎么导出。

//        File out_dir = getExternalFilesDir(null);
        //[LOG 打印]              /storage/emulated/0/Android/data/com.example.cameratest/files/
        //[Device File Explorer] /Android/data/com.example.cameratest/files
        //[手机文件]              /Android/data/com.example.cameratest/files


        File out_dir = new File("/sdcard/0/");
        //[LOG 打印] /sdcard/0
        // [Device File Explorer] /sdcard/0/
        // [手机文件] /0/
```