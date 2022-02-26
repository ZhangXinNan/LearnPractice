

# Perl中哈希变量以百分号 (%) 标记开始。
# 访问哈希元素格式：${key}。
%data = ('google', 'google.com', 'runoob', 'runoob.com', 'taobao', 'taobao.com');
 
print "\$data{'google'} = $data{'google'}\n";
print "\$data{'runoob'} = $data{'runoob'}\n";
print "\$data{'taobao'} = $data{'taobao'}\n";

# 1 通过key来设置
$data{'google'} = 'google.com';
$data{'runoob'} = 'runoob.com';
$data{'taobao'} = 'taobao.com';
print "\$data{'google'} = $data{'google'}\n";
print "\$data{'runoob'} = $data{'runoob'}\n";
print "\$data{'taobao'} = $data{'taobao'}\n";



# 2 通过列表来设置
%data1 = ('google', 'google.com', 'runoob', 'runoob.com', 'taobao', 'taobao.com');
%data2 = ('google'=>'google.com', 'runoob'=>'runoob.com', 'taobao'=>'taobao.com');
%data3 = (-google=>'google.com', -runoob=>'runoob.com', -taobao=>'taobao.com');

# 3 访问哈希元素
print("$data1\n");           # 无内容
print("$data2{'google'}\n");
print("$data3{-google}\n");

# 4 读取哈希值
%data = (-taobao => 45, -google => 30, -runoob => 40);
 
@array = @data{-taobao, -runoob};
 
print "Array : @array\n";

# 5 读取哈希的 key 和 value
%data = ('google'=>'google.com', 'runoob'=>'runoob.com', 'taobao'=>'taobao.com');
 
@names = keys %data;
 
print "$names[0]\n";
print "$names[1]\n";
print "$names[2]\n";


@urls = values %data;
 
print "$urls[0]\n";
print "$urls[1]\n";
print "$urls[2]\n";

# 6 检测元素是否存在
%data = ('google'=>'google.com', 'runoob'=>'runoob.com', 'taobao'=>'taobao.com');
 
if( exists($data{'facebook'} ) ){
   print "facebook 的网址为 $data{'facebook'} \n";
}
else
{
   print "facebook 键不存在\n";
}

# 7 获取哈希大小

%data = ('google'=>'google.com', 'runoob'=>'runoob.com', 'taobao'=>'taobao.com');
 
@keys = keys %data;
$size = @keys;
print "1 - 哈希大小: $size\n";
 
@values = values %data;
$size = @values;
print "2 - 哈希大小: $size\n";


# 8 哈希中添加或删除元素
%data = ('google'=>'google.com', 'runoob'=>'runoob.com', 'taobao'=>'taobao.com');
@keys = keys %data;
$size = @keys;
print "1 - 哈希大小: $size\n";
 
# 添加元素
$data{'facebook'} = 'facebook.com';
@keys = keys %data;
$size = @keys;
print "2 - 哈希大小: $size\n";
 
# 删除哈希中的元素
delete $data{'taobao'};
@keys = keys %data;
$size = @keys;
print "3 - 哈希大小: $size\n";



# 9 迭代哈希
%data = ('google'=>'google.com', 'runoob'=>'runoob.com', 'taobao'=>'taobao.com');
foreach $key (keys %data){
    print "$data{$key}\n";
}


%data = ('google'=>'google.com', 'runoob'=>'runoob.com', 'taobao'=>'taobao.com');
while(($key, $value) = each(%data)){
    print "$data{$key}\n";
}


