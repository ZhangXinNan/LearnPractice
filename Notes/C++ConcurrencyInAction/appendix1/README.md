
# 引用
```c++
int& i = 42;
```


```bash
g++ A1.cpp
g++ -std=c++11 A1.cpp
```

```bash
A1.cpp:6:10: error: non-const lvalue reference to type 'int' cannot bind to a temporary of type 'int'
    int& i = 42;
         ^   ~~
1 error generated.
```

# 右值引用
```c++
int&& i = 42;
int j = 42;
int&& k = j;
```

```bash
g++ A1.cpp
g++ -std=c++11 A1.cpp
```


```bash
A1.cpp:11:11: error: rvalue reference to type 'int' cannot bind to lvalue of type 'int'
    int&& k = j;
          ^   ~
1 error generated.
```

