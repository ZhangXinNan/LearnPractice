
运行catkin_make时出现错误：
```
[ 35%] Building CXX object VINS-Mono/camera_model/CMakeFiles/Calibration.dir/src/camera_models/CameraFactory.cc.o
/home/zhangxin/tools/catkin_ws/src/VINS-Mono/vins_estimator/src/estimator_node.cpp: In function ‘void restart_callback(const BoolConstPtr&)’:
/home/zhangxin/tools/catkin_ws/src/VINS-Mono/vins_estimator/src/estimator_node.cpp:193:31: error: ‘roslaunch’ was not declared in this scope
         m_estimator.unlock(); roslaunch vins_estimator euroc.launch 
                               ^
[ 36%] Building CXX object VINS-Mono/camera_model/CMakeFiles/Calibration.dir/src/camera_models/CostFunctionFactory.cc.o
[ 38%] Building CXX object VINS-Mono/camera_model/CMakeFiles/Calibration.dir/src/camera_models/PinholeCamera.cc.o
[ 40%] Linking CXX executable /home/zhangxin/tools/catkin_ws/devel/lib/benchmark_publisher/benchmark_publisher
[ 41%] Building CXX object VINS-Mono/camera_model/CMakeFiles/Calibration.dir/src/camera_models/CataCamera.cc.o
[ 41%] Built target benchmark_publisher
[ 43%] Building CXX object VINS-Mono/camera_model/CMakeFiles/Calibration.dir/src/camera_models/EquidistantCamera.cc.o
[ 44%] Building CXX object VINS-Mono/vins_estimator/CMakeFiles/vins_estimator.dir/src/factor/projection_factor.cpp.o
[ 46%] Building CXX object VINS-Mono/camera_model/CMakeFiles/Calibration.dir/src/camera_models/ScaramuzzaCamera.cc.o
[ 47%] Building CXX object VINS-Mono/camera_model/CMakeFiles/Calibration.dir/src/sparse_graph/Transform.cc.o
[ 49%] Building CXX object VINS-Mono/camera_model/CMakeFiles/Calibration.dir/src/gpl/gpl.cc.o
[ 50%] Building CXX object VINS-Mono/camera_model/CMakeFiles/Calibration.dir/src/gpl/EigenQuaternionParameterization.cc.o
[ 52%] Building CXX object VINS-Mono/vins_estimator/CMakeFiles/vins_estimator.dir/src/factor/projection_td_factor.cpp.o
[ 53%] Building CXX object VINS-Mono/vins_estimator/CMakeFiles/vins_estimator.dir/src/factor/marginalization_factor.cpp.o
[ 55%] Building CXX object VINS-Mono/vins_estimator/CMakeFiles/vins_estimator.dir/src/utility/utility.cpp.o
VINS-Mono/vins_estimator/CMakeFiles/vins_estimator.dir/build.make:62: recipe for target 'VINS-Mono/vins_estimator/CMakeFiles/vins_estimator.dir/src/estimator_node.cpp.o' failed
make[2]: *** [VINS-Mono/vins_estimator/CMakeFiles/vins_estimator.dir/src/estimator_node.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
CMakeFiles/Makefile2:2376: recipe for target 'VINS-Mono/vins_estimator/CMakeFiles/vins_estimator.dir/all' failed
make[1]: *** [VINS-Mono/vins_estimator/CMakeFiles/vins_estimator.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
[ 56%] Linking CXX shared library /home/zhangxin/tools/catkin_ws/devel/lib/libcamera_model.so
[ 56%] Built target camera_model
[ 58%] Linking CXX executable /home/zhangxin/tools/catkin_ws/devel/lib/camera_model/Calibration
[ 58%] Built target Calibration
Makefile:138: recipe for target 'all' failed
make: *** [all] Error 2
Invoking "make -j12 -l12" failed
```

代码有问题，修改即可。


