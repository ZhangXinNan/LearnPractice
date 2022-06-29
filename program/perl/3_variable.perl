
# 标量变量
$age = 25;             # 整型
$name = "runoob";      # 字符串
$salary = 1445.50;     # 浮点数
 
print "Age = $age\n";
print "Name = $name\n";
print "Salary = $salary\n";


# 数组变量
@ages = (25, 30, 40);             
@names = ("google", "runoob", "taobao");

# 程序中我们在 $ 标记前使用了转义字符 (\) ，这样才能输出字符 $。
# 要访问数组的变量，可以使用美元符号($)+变量名，并指定下标来访问
print "\$ages[0] = $ages[0]\n";
print "\$ages[1] = $ages[1]\n";
print "\$ages[2] = $ages[2]\n";
print "\$names[0] = $names[0]\n";
print "\$names[1] = $names[1]\n";
print "\$names[2] = $names[2]\n";



# 哈希变量
%data = ('google', 45, 'runoob', 30, 'taobao', 40);
 
print "\$data{'google'} = $data{'google'}\n";
print "\$data{'runoob'} = $data{'runoob'}\n";
print "\$data{'taobao'} = $data{'taobao'}\n";


# 变量上下文
@names = ('google', 'runoob', 'taobao');
 
@copy = @names;   # 复制数组
$size = @names;   # 数组赋值给标量，返回数组元素个数

print($names, "\n");
print(@names, "\n");
print "名字为 : @copy\n";
print "名字数为 : $size\n";

