

# 1 问题

```
2019-05-10 19:26:59.774 17842-17842/? E/Zygote: isWhitelistProcess - Process is Whitelisted
2019-05-10 19:26:59.774 17842-17842/? E/libpersona: scanKnoxPersonas
2019-05-10 19:26:59.774 17842-17842/? E/libpersona: Couldn't open the File - /data/system/users/0/personalist.xml - No such file or directory
2019-05-10 19:26:59.777 17842-17842/? W/SELinux: SELinux selinux_android_compute_policy_index : Policy Index[2],  Con:u:r:zygote:s0 RAM:SEPF_SM-G9350_8.0.0_0015, [-1 -1 -1 -1 0 1]
2019-05-10 19:26:59.789 17842-17842/? I/SELinux: SELinux: seapp_context_lookup: seinfo=untrusted, level=s0:c512,c768, pkgname=com.example.cameraalbumtest 
2019-05-10 19:26:59.815 17842-17842/? I/zygote64: Late-enabling -Xcheck:jni
2019-05-10 19:26:59.924 17842-17842/com.example.cameraalbumtest W/ActivityThread: Application com.example.cameraalbumtest can be debugged on port 8100...
2019-05-10 19:26:59.941 17842-17842/com.example.cameraalbumtest I/zygote64: no shared libraies, dex_files: 1
2019-05-10 19:27:00.076 17842-17842/com.example.cameraalbumtest I/InstantRun: starting instant run server: is main process
2019-05-10 19:27:00.086 17842-17842/com.example.cameraalbumtest D/AndroidRuntime: Shutting down VM
    
    
    --------- beginning of crash
2019-05-10 19:27:00.089 17842-17842/com.example.cameraalbumtest E/AndroidRuntime: FATAL EXCEPTION: main
    Process: com.example.cameraalbumtest, PID: 17842
    java.lang.RuntimeException: Unable to get provider android.support.v4.content.FileProvider: java.lang.IllegalArgumentException: Name must not be empty
        at android.app.ActivityThread.installProvider(ActivityThread.java:6581)
        at android.app.ActivityThread.installContentProviders(ActivityThread.java:6133)
        at android.app.ActivityThread.handleBindApplication(ActivityThread.java:6043)
        at android.app.ActivityThread.-wrap1(Unknown Source:0)
        at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1764)
        at android.os.Handler.dispatchMessage(Handler.java:105)
        at android.os.Looper.loop(Looper.java:164)
        at android.app.ActivityThread.main(ActivityThread.java:6944)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
     Caused by: java.lang.IllegalArgumentException: Name must not be empty
        at android.support.v4.content.FileProvider$SimplePathStrategy.addRoot(FileProvider.java:705)
        at android.support.v4.content.FileProvider.parsePathStrategy(FileProvider.java:648)
        at android.support.v4.content.FileProvider.getPathStrategy(FileProvider.java:579)
        at android.support.v4.content.FileProvider.attachInfo(FileProvider.java:392)
        at android.app.ActivityThread.installProvider(ActivityThread.java:6578)
        at android.app.ActivityThread.installContentProviders(ActivityThread.java:6133) 
        at android.app.ActivityThread.handleBindApplication(ActivityThread.java:6043) 
        at android.app.ActivityThread.-wrap1(Unknown Source:0) 
        at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1764) 
        at android.os.Handler.dispatchMessage(Handler.java:105) 
        at android.os.Looper.loop(Looper.java:164) 
        at android.app.ActivityThread.main(ActivityThread.java:6944) 
        at java.lang.reflect.Method.invoke(Native Method) 
        at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327) 
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374) 

```