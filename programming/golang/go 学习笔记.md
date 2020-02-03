```bash
C:\Users\zhang>go version
go version go1.13.5 windows/amd64

C:\Users\zhang>go env
set GO111MODULE=
set GOARCH=amd64
set GOBIN=
set GOCACHE=C:\Users\zhang\AppData\Local\go-build
set GOENV=C:\Users\zhang\AppData\Roaming\go\env
set GOEXE=.exe
set GOFLAGS=
set GOHOSTARCH=amd64
set GOHOSTOS=windows
set GONOPROXY=
set GONOSUMDB=
set GOOS=windows
set GOPATH=C:\Users\zhang\go
set GOPRIVATE=
set GOPROXY=https://proxy.golang.org,direct
set GOROOT=D:\Users\zhang\sdk\go1.13.5
set GOSUMDB=sum.golang.org
set GOTMPDIR=
set GOTOOLDIR=D:\Users\zhang\sdk\go1.13.5\pkg\tool\windows_amd64
set GCCGO=gccgo
set AR=ar
set CC=gcc
set CXX=g++
set CGO_ENABLED=1
set GOMOD=
set CGO_CFLAGS=-g -O2
set CGO_CPPFLAGS=
set CGO_CXXFLAGS=-g -O2
set CGO_FFLAGS=-g -O2
set CGO_LDFLAGS=-g -O2
set PKG_CONFIG=pkg-config
set GOGCCFLAGS=-m64 -mthreads -fno-caret-diagnostics -Qunused-arguments -fmessage-length=0 -fdebug-prefix-map=C:\Users\zhang\AppData\Local\Temp\go-build736404830=/tmp/go-build -gno-record-gcc-switches
```



1. GOPATH 以后写代码的位置
2. GOROOT SDK安装位置
3. PATH bin目录
4. 在项目目录下新建 src bin pkg 三个文件夹

编译
```bash
go build -o 指定输出名称
# 执行
go run
# 先编译，后把可执行程序拷贝到GOPATH/bin目录下
go install 
```


 