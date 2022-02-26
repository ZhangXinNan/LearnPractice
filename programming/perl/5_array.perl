
# 数组变量以 @ 开头。访问数组元素使用 $ + 变量名称 + [索引值] 格式来读取
@hits = (25, 30, 40);             
@names = ("google", "runoob", "taobao");
 
print "\$hits[0] = $hits[0]\n";
print "\$hits[1] = $hits[1]\n";
print "\$hits[2] = $hits[2]\n";
print "\$names[0] = $names[0]\n";
print "\$names[1] = $names[1]\n";
print "\$names[2] = $names[2]\n";


# 创建数组
@array = (1, 2, 'Hello');
print("$array[0]\n");
print("@array\n");

@array = qw/这是 一个 数组/;
print("$array[0],$array[1],$array[2]\n");

@days = qw/google
taobao
...
runoob/;
print("$days[0]\n");


# Perl 提供了可以按序列输出的数组形式，格式为 起始值 + .. + 结束值
@var_10 = (1..10);
@var_20 = (10..20);
@var_abc = ('a'..'z');
 
print "@var_10\n";   # 输出 1 到 10
print "@var_20\n";   # 输出 10 到 20
print "@var_abc\n";  # 输出 a 到 z


# 数组大小
@array = (1,2,3);
print "数组大小: ",scalar @array,"\n";


@array = (1,2,3);
$array[50] = 4;
 
$size = @array;
$max_index = $#array;
 
print "数组大小:  $size\n";
print "最大索引: $max_index\n";


# 创建一个简单是数组
@sites = ("google","runoob","taobao");
$new_size = @sites ;
print "1. \@sites  = @sites\n"."原数组长度 ：$new_size\n";
# 在数组结尾添加一个元素
$new_size = push(@sites, "baidu");
print "2. \@sites  = @sites\n"."新数组长度 ：$new_size\n";
 
# 在数组开头添加一个元素
$new_size = unshift(@sites, "weibo");
print "3. \@sites  = @sites\n"."新数组长度 ：$new_size\n";
 
# 删除数组末尾的元素
$new_byte = pop(@sites);
print "4. \@sites  = @sites\n"."弹出元素为 ：$new_byte\n";
 
# 移除数组开头的元素
$new_byte = shift(@sites);
print "5. \@sites  = @sites\n"."弹出元素为 ：$new_byte\n";


# 切割数组
@sites = qw/google taobao runoob weibo qq facebook 网易/;
 
@sites2 = @sites[3,4,5];
 
print "@sites2\n";

@sites = qw/google taobao runoob weibo qq facebook 网易/;
 
@sites2 = @sites[3..5];
 
print "@sites2\n";


# 替换数据元素
@nums = (1..20);
print "替换前 - @nums\n";
 
splice(@nums, 5, 5, 21..25); 
print "替换后 - @nums\n";


# 将字符串转换为数组
# 定义字符串
$var_test = "runoob";
$var_string = "www-runoob-com";
$var_names = "google,taobao,runoob,weibo";
 
# 字符串转为数组
@test = split('', $var_test);
@string = split('-', $var_string);
@names  = split(',', $var_names);
 
print "$test[3]\n";  # 输出 o
print "$string[2]\n";  # 输出 com
print "$names[3]\n";   # 输出 weibo




# 数组转为字符串
$string1 = join( '-', @string );
$string2 = join( ',', @names );
 
print "$string1\n";
print "$string2\n";



# 定义数组
@sites = qw(google taobao runoob facebook);
print "排序前: @sites\n";
 
# 对数组进行排序
@sites = sort(@sites);
print "排序后: @sites\n";



# 特殊变量： $[
# 定义数组
@sites = qw(google taobao runoob facebook);
print "网站: @sites\n";
 
# 设置数组的第一个索引为 1
$[ = 1;
 
print "\@sites[1]: $sites[1]\n";
print "\@sites[2]: $sites[2]\n";




# 数组的元素是以逗号来分割，我们也可以使用逗号来合并数组
@numbers = (1,3,(4,5,6));
 
print "numbers = @numbers\n";


@odd = (1,3,5);
@even = (2, 4, 6);
 
@numbers = (@odd, @even);
 
print "numbers = @numbers\n";




# 从列表中选择元素
$var = (5,4,3,2,1)[4];
 
print "var 的值为 = $var\n";

@list = (5,4,3,2,1)[1..3];
 
print "list 的值 = @list\n";


