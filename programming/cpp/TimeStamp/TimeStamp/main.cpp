#include <stdio.h>
#include <io.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

//#include "util.h"
#include "data.h"


int main()
{

	std::list<Data> list_imu;
	std::list<Data> list_whe;
	list_imu.push_back(Data(1));
	list_imu.push_back(Data(2));
	list_imu.push_back(Data(4));
	list_imu.push_back(Data(7));
	list_imu.push_back(Data(21));
	list_whe.push_back(Data(3));
	list_whe.push_back(Data(5));
	list_whe.push_back(Data(6));
	list_whe.push_back(Data(8));
	list_whe.push_back(Data(25));

	print_list(list_imu);
	print_list(list_whe);

	std::list<Data> result;
	//sort_time(list_imu, list_whe, result);
	//sort_time(list_imu, result);
	//sort_time(list_whe, result);
	result.merge(list_imu);
	result.merge(list_whe);
	print_list(list_imu);
	print_list(list_whe);
	print_list(result);



	list_imu.push_back(Data(14));
	list_imu.push_back(Data(17));
	list_whe.push_back(Data(13));
	list_whe.push_back(Data(15));
	//sort_time(list_whe, result);
	//sort_time(list_imu, result);
	//sort_time(list_imu, list_whe, result);
	result.merge(list_imu);
	result.merge(list_whe);
	print_list(list_imu);
	print_list(list_whe);
	print_list(result);





	system("pause");
	return 0;
}