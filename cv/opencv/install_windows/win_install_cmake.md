Installation by Using git-bash (version>=2.14.1) and cmake (version >=3.9.1)
________________________________

参考installOCV.sh


[Configuring CMake to build OpenCV on Windows](https://perso.uclouvain.be/allan.barrea/opencv/cmake_config.html)

1. Start the GUI version of CMake (cmake-gui).

2. Select the folder C:\OpenCV\sources as the source directory.

3. Select the folder C:\OpenCV\builds as the build directory.

4. Enable the Grouped and Advanced checkboxes just below the build directory name. These will impact the way the packages information will be displayed in the CMake GUI in the following steps.


5. Press the “Configure” button. A window pops up, letting you specify the compiler (and IDE) you want to use. Pick Visual Studio 10, 32-bit or 64-bit according to your Matlab version. Select also “Use default native compilers” and click Finish.

6. CMake will start out and based on your system variables will try to automatically locate as many packages as possible. You can modify the packages to use for the build in the WITH > WITH_X menu points (where X is the package abbreviation).

7. Configure CMake until all the elements are found. Follow the instructions below.

8. Once you are comfortable with your CMake configuration, press Generate and close CMake.