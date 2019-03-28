#include <iostream>
#include "opencv2/core/version.hpp"

int main(int argc, char ** argv)
{
  std::cout << "OpenCV version: "
            << CV_MAJOR_VERSION << "." 
            << CV_MINOR_VERSION << "."
            << CV_SUBMINOR_VERSION
            << std::endl;
  return 0;
}


