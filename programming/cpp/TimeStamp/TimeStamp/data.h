#pragma once
#include <list>
#include <iostream>
using namespace std;

struct Data {
	Data() {}
	Data(long t):timestamp(t){}
	Data(long t, double x) : timestamp(t), x(x) {}
	Data(long t, double x, double y, double z): timestamp(t), x(x), y(y), z(z){}

	bool operator<(const Data& f) {
		if (f.timestamp < this->timestamp) {
			return false;
		}
		return true;
	}

	long timestamp;				// 时间戳，单位毫秒 milliseconds
	double x, y, z;				// type=1 为加速度计数据 ；type=2 为轮速计数据
	double roll, pitch, yaw;		// type=1 为陀螺仪数据；type=2 时无用。
	int type;					// 数据类型 1 表示IMU，2 表示轮速计

	void print() const {
		std::cout << timestamp << std::endl;
	}
};


void print_list(const list<Data> &lst);

/*
1. 所有链表是按照时间戳顺序排列的。
2. list_imu list_wheel 中的元素插入到lst中后，要从原链表中移除。最终list_imu 和 list_wheel为空。
3. list的erase方法返回值指向删除元素的位置，此时存储的是原来删除元素后边的元素
4. list的insert方法，插入的元素在指向的位置上，原来指向的位置都往后放，返回值 指向当前插向的位置。
*/
void sort_time(std::list<Data> &list_imu, std::list<Data> &list_whe, std::list<Data> &lst);

/*
1. 链表a和b都是按照时间戳顺序存储的。
2. 将a中的元素，根据时间戳顺序，依次全部插入到b中，每次插入后，删除a中的元素。
*/
void sort_time(std::list<Data> &a, std::list<Data> &b);