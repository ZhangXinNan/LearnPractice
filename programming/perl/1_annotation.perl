
# 单行注释
# perl中数字都是float类型
$data1 = 10;
$data2 = 10.00;
print($data1, "\n");
# 输出结果：10
print($data2, "\n");
# 输出结果：10


$p1 = 3141592639;
$p2 = 3_141_592_639;
print($p1, "\n");
print($p2, "\n");
=pod 多行注释
3141592639
3141592639
=cut

$s1 = "'hello'";
$s2 = '"hello"';
$s3 = '\'hello\'';
print "$s1\n";
print("$s2\n");
print("$s3\n");
# 输出转义字符
print("$s1,$s2,$s3\n");
print("\$s1,\$s2,\$s3\n");

print("hello\n");
print('hello\n');
print("\n");
=pod 单引号与双引号区别
双引号 \n 输出了换行，而单引号没有。
Perl双引号和单引号的区别: 双引号可以正常解析一些转义字符与变量，而单引号无法解析会原样输出。
=cut

print("hello
                world\n");
# 所有类型的空白如：空格，tab ，空行等如果在引号外解释器会忽略它，如果在引号内会原样输出。

$a = 10;
$var = <<"EOF";
这是一个 Here 文档实例，使用双引号。
可以在这输入字符串和变量。
例如：a = $a
EOF
print("$var\n")
