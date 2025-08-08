
js框架之jQuery
____
# 1 jQuery是一个javascript框架/库

为什么出现javascript框架？
提高开发js的效率。

比如：
```js
// 为了获取id对象
document.getElementById('id号')
// 为了获取标签名获取对象
document.getElementsByTagName("tagname");

// 使用框架
$('#id')$('.classname')
// 使用jQuery发送ajax请求
Jquery.send(...);
```

# 2 write less, do more

# 3 jQuery是一个轻量级的js库，给使用者提供了一系列的函数。
使用户方便地处理HTML documents/events/实现动画效果，并且方便地为网站提供ajax交互。

在使用jquery开发中，有两种对象：
1. jquery对象。如果是jquery对象，则只能使用jquery库提供的方法。
2. dom对象。如果是dom对象，则只能使用js本身提供的方法。

JavaScript库封装了很多预定义的对象和实用函数。能帮助使用者建立高难度交互的Web2.0特性的富客户端页面，并且兼容各大浏览器。

# 4 什么是jQuery对象

- jQuery对象就是通过jQuery包装DOM对象后产生的对象。
- jQuery对象是jQuery独有的。如果一个对象是jQuery对象，那么它就可以使用jQuery里的方法。
  - `$("#test").html` 获取ID为test的元素内的html代码。html()是jQuery里的方法。这段代码等同于DOM实现的代码：`document.getElementById("id").innerHTML;`
- 虽然jQuery对象是包装 DOM 对象后产生的，但是jQuery无法使用DOM对象的任何方法，同理DOM对象也不能使用jQuery里的方法。
- 约定：
  - `var $variable = jQuery对象`
  - `var variable = DOM对象`


