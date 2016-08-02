
#include <iostream>
using namespace std;

#include <opencv2/opencv.hpp>
using namespace cv;

int main(int args, char* argv[]) {
  if (args < 2) {
    std::cout << "please input image path " << std::endl;
    return 0;
  }

  string filename = argv[1];
  Mat img = imread(filename);
  if(img.empty()) {
    std::cout << "read image error " << filename << std::endl;
    return 0;
  }

  // 基本的MSER检测器
  cv::MSER mser(5, 200, 1500);
  // 点集的容器
  std::vector<std::vector<cv::Point>> points;
  //检测MSER特征
  mser(img, points);
   
  // 创建白色图像
  cv::Mat output(img.size(), CV_8UC3);
  output = cv::Scalar(255, 255, 255);
  
  // 随机数生成器
  cv::RNG rng;
  // 针对检测到的特征区域
  for (std::vector<std::vector<cv::Point>>::iterator it = points.begin(); it != points.end(); it++) {
    //生成随机颜色
    cv::Vec3b c(rng.uniform(0, 255), rng.uniform(0, 255), rng.uniform(0, 255));
    
    //针对MSER集合中的每个点
    for (std::vector<cv::Point>:: iterator itPts = it->begin(); itPts != it->end(); ++itPts) {
      output.at<cv::Vec3b>(*itPts) = c;
    }
  }
  imshow("0", img);
  imshow("1", output);
  waitKey();
  destroyAllWindows();
  return 0;
}
