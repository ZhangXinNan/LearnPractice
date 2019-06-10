


## 3.3 详解4种基本布局
### 3.3.1 线性布局 LinearLayout
控件在线性方向上依次排列

水平和竖直排列：
```xml
android:orientation="horizontal"
android:orientation="vertical"
```

文字在控件中在对齐方式。优先级比layout_width更高，
```xml
android:layout_gravity="top"
android:layout_gravity="center_vertical"
android:layout_gravity="bottom"
```


使用比例的方式来指定控件的大小
```xml
android:layout_weight="1"
```

### 3.3.2 相对布局 RelativeLayout
通过相对定位的方式让控件出现在布局的任何位置

相对于父布局进行定位：
```xml
android:layout_alignParentLeft="true"
android:layout_alignParentTop="true"
android:layout_alignParentRight="true"
android:layout_alignParentBottom="true"
android:layout_centerInParent="true"
```


相对于控件进行定位
```xml
android:layout_above="true"
android:layout_below="true"
android:layout_toLeftOf="@id/button3"
android:layout_toRightOf="@id/button3"
```

### 3.3.3 帧布局 FrameLayout
所有控件默认摆放在布局的左上角。
可以通过layout_gravity来指定控件在布局中的对齐方式。

### 3.3.4 百分比布局
允许直接使用控件在布局中所占的百分比。

百分比布局为FrameLayout和RelativeLayout进行了功能扩展。




