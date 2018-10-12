//#include "load_dataset.hpp"

#include <stdint.h>
#include <sys/stat.h>

#include <fstream>
#include <string>

#include <opencv2/opencv.hpp>
using namespace cv;
#include <iostream>
#include <string>
#include <vector>
using namespace std;

#include <time.h>
#include <stdio.h>
#include <stdlib.h>

uint32_t swap_endian(uint32_t val) {
    val = ((val << 8) & 0xFF00FF00) | ((val >> 8) & 0xFF00FF);
    return (val << 16) | (val >> 16);
}

inline cv::Mat str2Mat(const char* pixels, const int row, const int col){
    cv::Mat m(row, col, CV_8UC1);
    for (int y = 0; y < row; y++) {
        memcpy(m.data + y * m.step, pixels + y * col, col);
    }
    return m;
}

void convert_dataset(const string &image_filename, const string &label_filename, std::vector< std::vector<cv::Mat> > &vvMat) {
    vvMat.resize(10);
    // Open files
    std::ifstream image_file(image_filename, std::ios::in | std::ios::binary);
    std::ifstream label_file(label_filename, std::ios::in | std::ios::binary);
    //CHECK(image_file) << "Unable to open file " << image_filename;
    //CHECK(label_file) << "Unable to open file " << label_filename;
    // Read the magic and the meta data
    uint32_t magic;
    uint32_t num_items;
    uint32_t num_labels;
    uint32_t rows;
    uint32_t cols;

    image_file.read(reinterpret_cast<char*>(&magic), 4);
    magic = swap_endian(magic);
    //CHECK_EQ(magic, 2051) << "Incorrect image file magic.";
    label_file.read(reinterpret_cast<char*>(&magic), 4);
    magic = swap_endian(magic);
    //CHECK_EQ(magic, 2049) << "Incorrect label file magic.";
    image_file.read(reinterpret_cast<char*>(&num_items), 4);
    num_items = swap_endian(num_items);
    label_file.read(reinterpret_cast<char*>(&num_labels), 4);
    num_labels = swap_endian(num_labels);
    std::cout << "num_items " << num_items << ", num_labels " << num_labels << std::endl;
    //CHECK_EQ(num_items, num_labels);
    image_file.read(reinterpret_cast<char*>(&rows), 4);
    rows = swap_endian(rows);
    image_file.read(reinterpret_cast<char*>(&cols), 4);
    cols = swap_endian(cols);
    std::cout << "rows " << rows << ", cols " << cols << std::endl;

    // Storing to db
    char label;
    char* pixels = new char[rows * cols];

    for (int item_id = 0; item_id < num_items; ++item_id) {
        image_file.read(pixels, rows * cols);
        label_file.read(&label, 1);
        cv::Mat img = str2Mat(pixels, rows, cols);
        //std::cout << int(label) << std::endl;
        //print_mat(img);
        //string winname = "0";
        //winname[0] += label;
        //imshow(winname, img);
        //waitKey();
        //destroyAllWindows();
        vvMat[label].push_back(img);
        //break;
    }

    delete[] pixels;
}



inline double sigmoid(double z) {
    return 1.0 / (1.0 + exp(-z));
}
//sigmoid函数的导数
inline double sigmoid_prime(double z) {
    return sigmoid(z) * (1 - sigmoid(z));
}


const int n_in      = 784;
const int n_hidden  = 30;
const int n_out     = 10;



double w1[n_hidden][n_in];
double w2[n_out][n_hidden];
double b1[n_hidden];
double b2[n_out];
double delta_w1[n_hidden];
double delta_w2[n_out];
double delta_b1[n_hidden];
double delta_b2[n_out];
double eta = 0.01;

void init_wb();
void init_delta();
double evaluate(const vector<vector<Mat>> &vvMatTest, const int num = 1000);
void forward(double* x, double* y, double* h);
void Mat8uc1_darr(const Mat& m, double *arr);

void print_mat(const cv::Mat &m);
void print_array(const double* arr, int size1, int size2 = 0);

void sgd(const vector<vector<Mat>> &vvMatTrain, const int numTrain, const int beginIndex = 0);

int main() {
    string data_path = "/Users/zhangxin/datas/mnist/";
    string images_test = "t10k-images-idx3-ubyte";
    string labels_test = "t10k-labels-idx1-ubyte";
    string images_train = "train-images-idx3-ubyte";
    string labels_train = "train-labels-idx1-ubyte";
    std::vector< std::vector<cv::Mat> > vvMat;
    std::vector< std::vector<cv::Mat> > vvMatTest;
    convert_dataset(data_path + images_test,  data_path + labels_test, vvMatTest);
    convert_dataset(data_path + images_train, data_path + labels_train, vvMat);

    init_wb();
    evaluate(vvMatTest, 2000);

    for (int i = 0; i < 1000; i++) {
        printf("%4d --------\n", i);
        sgd(vvMat, 100, i * 100);
        evaluate(vvMatTest, 2000);
    }
    //evaluate(vvMatTest, 1000);

    return 0;

}

void sgd(const vector<vector<Mat>> &vvMatTrain, const int numTrain, const int beginIndex){
    init_delta();
   for (int j = 0; j < numTrain ; j++) {
        for (int i = 0; i < n_out; i++) {
            double y[n_out] = {0.0};
            double x[n_in] = {0.0};
            double h[n_hidden] = {0.0};
            Mat8uc1_darr(vvMatTrain[i][(beginIndex + j) % vvMatTrain[i].size()], x);
            forward(x, y, h);

            double t[n_out] = {0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0};
            t[i] = 1.0;

            for (int m = 0; m < n_out; m++) {
                delta_w2[m] = delta_b2[m] = y[m] * (1-y[m]) * (t[m] - y[m]);
                b2[m] += eta * delta_b2[m];

                for (int n = 0; n < n_hidden; n++) {
                    w2[m][n] += eta * delta_w2[m] * h[n];
                }
            }

            for (int m = 0; m < n_hidden; m++) {
                delta_b1[m] = 0.0;
                for (int k = 0; k < n_out; k++) {
                    delta_b1[m] += w2[k][m] * delta_w2[k];
                }
                delta_w1[m] = delta_b1[m] = delta_b1[m] * h[m] * (1 - h[m]);
                b1[m] += eta * delta_b1[m];

                for (int n = 0; n < n_in; n++) {
                    w1[m][n] += eta * delta_w1[m] * x[n];
                }

            }
        }
    }
}


double evaluate(const vector<vector<Mat>> &vvMatTest, const int num){
    int sum = 0;
    int sum_right = 0;
    vector<int> vec_sum(10, 0);
    vector<int> vec_sum_right(10, 0);
    int result[10][10];
    memset(result, 0, sizeof(int) * 100);

    for (int i = 0; i < n_out && i < vvMatTest.size(); i++) {
        for (int j = 0; j < num && j < (int)vvMatTest[i].size(); j++) {//
            double x[n_in];
            double y[n_out];
            double h[n_hidden];
            const Mat &img = vvMatTest[i][j];

            Mat8uc1_darr(img, x);
//            print_mat(img);
//            print_array(x, img.rows, img.cols);
//            imshow("00", img);
//            waitKey();
//            continue;

            forward(x, y, h);
            int predict_label = 0;
            double predict_f = y[0];//y.at<double>(0, 0);
            //printf("%2d %4d :[ 0] %6.3f, ", i, j, predict_f);
            for (int k = 1; k < n_out; k++) {
                double f = y[k];//y.at<double>(0, k);
                //printf("%d %6.3f, ", k, f);
                if (f  > predict_f ) {
                    predict_f = f;
                    predict_label = k;
                }
            }
            //printf(" predict : %d %6.3f\n", predict_label, predict_f);

            vec_sum[i]++;
            sum++;
            if (predict_label == i) {
                sum_right++;
                vec_sum_right[i]++;
            }
            result[i][predict_label]++;
        }
    }
    std::cout << "sum : " << sum << ", sum_right : " << sum_right << std::endl;
    for (int i = 0; i < n_out; i++) {
        printf(" [%d] [%4d %4d] ", i, vec_sum[i], vec_sum_right[i]);
        for (int j = 0; j < n_out; j++) {
            printf ("%4d ", result[i][j]);
        }
        printf("\n");
    }
    return sum_right / double(sum);
}

void forward(double* x, double* y, double* h){

    for (int i = 0; i < n_hidden; i++) {
        h[i] = b1[i];
        for (int j = 0; j < n_in; j++) {
            h[i] += x[j] * w1[i][j];

        }
        h[i] = sigmoid(h[i]);
    }

    for (int i = 0; i < n_out; i++) {
        y[i] = b2[i];
        for (int j = 0; j < n_hidden; j++) {
            y[i] += h[j] * w2[i][j];
        }
        y[i] = sigmoid(y[i]);
    }

}

void Mat8uc1_darr(const Mat& m, double *arr) {
    for (int y = 0; y < m.rows; y++) {
        for (int x = 0; x < m.cols; x++) {
            arr[y * m.cols + x] = m.at<uchar>(y,x) / 255.0;
        }
    }
}


void init_delta(){
    memset(delta_w1, 0, sizeof(double) * n_hidden);
    memset(delta_w2, 0, sizeof(double) * n_out);
    memset(delta_b1, 0, sizeof(double) * n_hidden);
    memset(delta_b2, 0, sizeof(double) * n_out);
}


void init_wb() {
    std::srand((unsigned)std::time(0)); // use current time as seed for random generator
    cout << " init w1 : " << endl;
    for (int i = 0; i < n_hidden; i++) {
        cout << " w1[" << i << "]" << endl;
        for (int j = 0; j < n_in; j++) {
            w1[i][j] = std::rand()/double(RAND_MAX) - 0.5;
            w1[i][j] *= 0.1;
            printf("%6.3f ", w1[i][j]);
        }
        printf("\n");
    }
    cout << " init w2 : " << endl;
    for (int i = 0; i < n_out; i++) {
        cout << " w1[" << i << "]" << endl;
        for (int j = 0; j < n_hidden; j++) {
            w2[i][j] = std::rand()/double(RAND_MAX) - 0.5;
            w2[i][j] *= 0.1;
            printf("%6.3f ", w2[i][j]);
        }
        printf("\n");
    }
    cout << "init b1" << endl;
    for (int i = 0; i < n_hidden; i++) {
        b1[i] = std::rand() / double(RAND_MAX) - 0.5;
        b1[i] *= 0.1;
        printf("%6.3f ", b1[i]);
    }
    printf("\n");

    cout << "init b2" << endl;
    for (int i = 0; i < n_out; i++) {
        b2[i] = std::rand() / double(RAND_MAX) - 0.5;
        b2[i] *= 0.2;
        printf("%6.3f ", b2[i]);
    }
    printf("\n");

}



void print_mat(const cv::Mat &m) {
    for (int y = 0; y < m.rows; y++) {
        printf("[%4d] ", y);
        for (int x = 0; x < m.cols; x++) {
            switch(m.type()){
                case CV_8UC1:
                    printf("%3d ", m.data[y * m.step + x]); break;
                case CV_64FC1:
                    printf("%6.3f ", m.at<double>(y,x));    break;
            }
        }
        std::cout << std::endl;
    }
}
void print_array(const double* arr, int size1, int size2) {
    for (int i = 0; i < size1; i++) {
        if( size2 > 1){
            printf("[%4d] ", i);
            for (int j = 0; j < size2; j++) {
                printf("%6.3f ", arr[i * size2 + j]);
            }
            printf("\n");
        }else {
            printf("%6.3f ", arr[i]);
        }
    }
    printf("\n");
}