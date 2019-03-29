


在试图使用kdevelop的过程中，build时出现如下错误：
```
/home/zhangxin/tools/catkin_ws/build> /usr/bin/cmake -DCMAKE_INSTALL_PREFIX=/home/zhangxin/tools/catkin_ws/install -DCMAKE_BUILD_TYPE=Debug -DCATKIN_DEVEL_PREFIX=../devel -DCMAKE_INSTALL_PREFIX=../install /home/zhangxin/tools/catkin_ws/src/
CMake Error at CMakeLists.txt:59 (message):
  find_package(catkin) failed.  catkin was neither found in the workspace nor
  in the CMAKE_PREFIX_PATH.  One reason may be that no ROS setup.sh was
  sourced before.


-- Configuring incomplete, errors occurred!
See also "/home/zhangxin/tools/catkin_ws/build/CMakeFiles/CMakeOutput.log".
*** Failure: Exit code 1 ***
```

解决方法：






