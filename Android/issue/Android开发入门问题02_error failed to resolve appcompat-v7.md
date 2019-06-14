

# 1 问题
使用新版本的Android Studio编译项目时，出现
```bash
ERROR: Failed to resolve: com.android.support:appcompat-v7:24.2.1
Add Google Maven repository and sync project
Show in Project Structure dialog
Affected Modules: app


WARNING: Configuration 'compile' is obsolete and has been replaced with 'implementation' and 'api'.
It will be removed at the end of 2018. For more information see: http://d.android.com/r/tools/update-dependency-configurations.html
Affected Modules: app


WARNING: Configuration 'testCompile' is obsolete and has been replaced with 'testImplementation'.
It will be removed at the end of 2018. For more information see: http://d.android.com/r/tools/update-dependency-configurations.html
Affected Modules: app


WARNING: The specified Android SDK Build Tools version (24.0.2) is ignored, as it is below the minimum supported version (28.0.3) for Android Gradle Plugin 3.4.0.
Android SDK Build Tools 28.0.3 will be used.
To suppress this warning, remove "buildToolsVersion '24.0.2'" from your build.gradle file, as each version of the Android Gradle Plugin now has a default version of the build tools.
Remove Build Tools version and sync project
Affected Modules: app
```


# 2 解决

