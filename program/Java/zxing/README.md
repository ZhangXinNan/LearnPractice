
# 编译
```bash
cd zxing
mvn install
```

# 运行
## javase
```bash
cd javase/

# 创建一个jar包
mvn -DskipTests package assembly:single

java -jar target/javase-3.4.1-SNAPSHOT-jar-with-dependencies.jar /Users/zhangxin/data_md/barcodes/JT00001_0.jpg
```