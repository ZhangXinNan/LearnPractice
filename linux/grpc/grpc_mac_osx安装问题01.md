


# 1 问题
```bash
➜  grpc-1.25.0  LIBTOOL=glibtool LIBTOOLIZE=glibtoolize make
Package libcares was not found in the pkg-config search path.
Perhaps you should add the directory containing `libcares.pc'
to the PKG_CONFIG_PATH environment variable
No package 'libcares' found

DEPENDENCY ERROR

You are missing system dependencies that are essential to build grpc,
and the third_party directory doesn't have them:

  cares

Installing the development packages for your system will solve
this issue. Please consult INSTALL to get more information.

If you need information about why these tests failed, run:

  make run_dep_checks

make: *** [stop] Error 1
```


# 2 解决
