

# 一. Android内外存储基础知识
Android手机上的存储空间可做如下划分：
* 内存：RAM
* 内部存储：内部ROM
* 外部存储：外部ROM和SDCard

## 1.1 内部存储
Android可以说是一个Linux操作系统，它的内部存储空间对于应用程序和用户来讲就是“/data/data“目录。内部存储与外部存储相比有着比较稳定，存储方便，操作简单，更加安全（可以控制访问权限）等优点，而它唯一的缺点就是空间有限。

内部存储空间的有限意味着应物尽其用，用来保存比较重要的数据，例如用户信息资料，口令秘码等不需要与其他应用程序共享的数据。注意应用程序被卸载时，应用程序在内部存储空间的文件数据将全部被删除，避免占用宝贵的空间。

内部存储即data文件夹，其中里面有两个文件夹值得关注：
* app文件夹（未root无法打开）：存放着所有app的apk文件夹，当开发者调试某个app时，AS控制台输出的内容中有一项是uploading…，代表正在上传apk到这个文件夹。
* data文件夹：内部都是app的包名，存储着应用程序相关的数据，例如 data/data/包名/(shared_prefs、database、files、cache)


## 1。2 外部存储
外部存储是指用户在使用时自行在手机上添加的外部存储介质，例如TS卡，SD卡等闪存储介质。其显著的优点就是存储空间大，无需担心数据清除问题，与内部存储不同的是当应用程序卸载时，它在外部存储所创建的文件数据不会被清除，因此清理外部存储空间的责任丢给了用户自己。缺点则是不太稳定，闪存介质对于Android手机而言会出现SD卡不能正常使用的情况。

外部存储即storage文件夹或mnt文件夹。需要注意的是storage中有一个sdcard0文件夹，其中又分为公有目录和私有目录：
* 公有目录：有9大类，比如DCIM、Download等系统为用户创建的文件夹；
* 私有目录： 即Android文件夹/storage/sdcard/Android/，其中的data文件夹包含了许多包名组成的文件夹。


## 1.3 内外部存储常用目录操作

* context.getFilesDir() 内部存储data/data/包名/files目录
* context.getCacheDir() 内部存储data/data/包名/cache目录
* Environment.getExternalStorageDirectory() 外部存储根目录
* Environment.getExternalStoragePublicDirectory (Environment.DIRECTORY_DCIM) 外部存储公有目录
* context.getExternalFilesDir() 外部存储私有目录storage/sdcard/Android/data/包名/files。一般存储长时间保存的数据。
* context.getExternalCacheDir() 外部存储私有目录storage/sdcard/Android/data/包名/cache。一般存储临时缓存数据。

注意上述最后两个API：当app被卸载后，sdCard/Android/data/PackageName/下的所有文件都会被删除，不会留下垃圾信息。两个API对应的目录分别对应着 设置->应用->应用详情里面的“清除数据”与“清除缓存”选项。





# 参考
* [Android内、外存储 易混淆点剖析（/mnt/sdcard、/storage/sdcard0、/storage/emulated/0等区别）](https://blog.csdn.net/itermeng/article/details/79423035)