

问题：
早先安装了Anaconda3，后再安装出现问题：
```
-- Using Python nosetests: /home/zhangxin/anaconda3/bin/nosetests
ImportError: "from catkin_pkg.package import parse_package" failed: No module named 'catkin_pkg'
Make sure that you have installed "catkin_pkg", it is up to date and on the PYTHONPATH.
CMake Error at /opt/ros/kinetic/share/catkin/cmake/safe_execute_process.cmake:11 (message):
  execute_process(/home/zhangxin/anaconda3/bin/python
  "/opt/ros/kinetic/share/catkin/cmake/parse_package_xml.py"
  "/opt/ros/kinetic/share/catkin/cmake/../package.xml"
  "/home/zhangxin/tools/catkin_ws/build/catkin/catkin_generated/version/package.cmake")
  returned error code 1
Call Stack (most recent call first):
  /opt/ros/kinetic/share/catkin/cmake/catkin_package_xml.cmake:74 (safe_execute_process)
  /opt/ros/kinetic/share/catkin/cmake/all.cmake:163 (_catkin_package_xml)
  /opt/ros/kinetic/share/catkin/cmake/catkinConfig.cmake:20 (include)
  CMakeLists.txt:52 (find_package)


-- Configuring incomplete, errors occurred!
See also "/home/zhangxin/tools/catkin_ws/build/CMakeFiles/CMakeOutput.log".
See also "/home/zhangxin/tools/catkin_ws/build/CMakeFiles/CMakeError.log".

```