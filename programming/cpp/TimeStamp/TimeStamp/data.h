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

	long timestamp;				// ʱ�������λ���� milliseconds
	double x, y, z;				// type=1 Ϊ���ٶȼ����� ��type=2 Ϊ���ټ�����
	double roll, pitch, yaw;		// type=1 Ϊ���������ݣ�type=2 ʱ���á�
	int type;					// �������� 1 ��ʾIMU��2 ��ʾ���ټ�

	void print() const {
		std::cout << timestamp << std::endl;
	}
};


void print_list(const list<Data> &lst);

/*
1. ���������ǰ���ʱ���˳�����еġ�
2. list_imu list_wheel �е�Ԫ�ز��뵽lst�к�Ҫ��ԭ�������Ƴ�������list_imu �� list_wheelΪ�ա�
3. list��erase��������ֵָ��ɾ��Ԫ�ص�λ�ã���ʱ�洢����ԭ��ɾ��Ԫ�غ�ߵ�Ԫ��
4. list��insert�����������Ԫ����ָ���λ���ϣ�ԭ��ָ���λ�ö�����ţ�����ֵ ָ��ǰ�����λ�á�
*/
void sort_time(std::list<Data> &list_imu, std::list<Data> &list_whe, std::list<Data> &lst);

/*
1. ����a��b���ǰ���ʱ���˳��洢�ġ�
2. ��a�е�Ԫ�أ�����ʱ���˳������ȫ�����뵽b�У�ÿ�β����ɾ��a�е�Ԫ�ء�
*/
void sort_time(std::list<Data> &a, std::list<Data> &b);