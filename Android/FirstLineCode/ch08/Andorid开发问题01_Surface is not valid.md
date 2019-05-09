

# 1 问题
```bash
2019-05-09 13:24:57.346 20274-20274/? E/Zygote: isWhitelistProcess - Process is Whitelisted
2019-05-09 13:24:57.347 20274-20274/? E/libpersona: scanKnoxPersonas
2019-05-09 13:24:57.347 20274-20274/? E/libpersona: Couldn't open the File - /data/system/users/0/personalist.xml - No such file or directory
2019-05-09 13:24:57.992 20274-20274/com.example.choosepictest E/ViewRootImpl@5a934c6[MainActivity]: Surface is not valid.
2019-05-09 13:25:02.326 20274-20274/com.example.choosepictest E/AndroidRuntime: FATAL EXCEPTION: main
    Process: com.example.choosepictest, PID: 20274
    android.os.FileUriExposedException: file:///storage/emulated/0/output_image.jpg exposed beyond app through ClipData.Item.getUri()
        at android.os.StrictMode.onFileUriExposed(StrictMode.java:1958)
        at android.net.Uri.checkFileUriExposed(Uri.java:2356)
        at android.content.ClipData.prepareToLeaveProcess(ClipData.java:944)
        at android.content.Intent.prepareToLeaveProcess(Intent.java:10480)
        at android.content.Intent.prepareToLeaveProcess(Intent.java:10465)
        at android.app.Instrumentation.execStartActivity(Instrumentation.java:1616)
        at android.app.Activity.startActivityForResult(Activity.java:4564)
        at android.support.v4.app.FragmentActivity.startActivityForResult(FragmentActivity.java:767)
        at android.app.Activity.startActivityForResult(Activity.java:4522)
        at android.support.v4.app.FragmentActivity.startActivityForResult(FragmentActivity.java:754)
        at com.example.choosepictest.MainActivity$1.onClick(MainActivity.java:52)
        at android.view.View.performClick(View.java:6897)
        at android.widget.TextView.performClick(TextView.java:12693)
        at android.view.View$PerformClick.run(View.java:26101)
        at android.os.Handler.handleCallback(Handler.java:789)
        at android.os.Handler.dispatchMessage(Handler.java:98)
        at android.os.Looper.loop(Looper.java:164)
        at android.app.ActivityThread.main(ActivityThread.java:6944)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
```


# 2 解决



