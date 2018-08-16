# 0 SED 简明教程

sed全名叫stream editor，流编辑器，用程序的方式来编辑文本。sed基本上就是玩正则模式匹配，所以，玩sed的人，正则表达式一般都比较强。

# 1 用s命令替换
## 1.1 入门示例-替换
```
sed "s/my/Hao Chen's/g" pets.txt

This is Hao Chen's cat
  Hao Chen's cat's name is betty
This is Hao Chen's dog
  Hao Chen's dog's name is frank
This is Hao Chen's fish
  Hao Chen's fish's name is george
This is Hao Chen's goat
  Hao Chen's goat's name is adam
```
s : 替换
g : 一行上替换所有匹配
注意：
（1）单引号不支持转义；
（2）没有对文件内容改变，如需改变可以使用重定向，或者加-i。
```
sed "s/my/Hao Chen's/g" pets.txt > hao_pets.txt
sed -i "s/my/Hao Chen's/g" pets.txt
```




# 2 多个匹配
## 2.1 替换多个模式
第一个模式把第一行到第三行的my替换成your，第二个则把第3行以后的This替换成了That
```
sed '1,3s/my/your/g; 3,$s/This/That/g' my.txt
```

## 2.2 使用&来当作被匹配的变量
在匹配左右加方括号
```
sed 's/my/[&]/g' my.txt
```

# 3 圆括号匹配
圆括号括起来的正则表达式匹配的字符串当成变量来使用。
