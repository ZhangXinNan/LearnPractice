
1.1.1 是长期支持版（LTS)，2.0不再更新，下个主要支持版本是3.0版本。

编译：
```bash
./config
sudo make install

pkg-config --cflags --libs openssl
# -I/usr/local/include -L/usr/local/lib -lssl -lcrypto
```


