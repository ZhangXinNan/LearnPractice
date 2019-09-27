

#include "data.h"
#include <list>
#include <iostream>
using namespace std;

void print_list(const list<Data> &lst) {
	std::cout << "list<Data> size : " << lst.size() << std::endl;
	for (list<Data>::const_iterator it = lst.begin(); it != lst.end(); it++) {
		it->print();
	}
}


/*
1. ���������ǰ���ʱ���˳�����еġ�
2. list_imu list_wheelʱ�������lst֮��
3. list_imu list_wheel �е�Ԫ�ز��뵽lst�к�Ҫ��ԭ�������Ƴ�������list_imu �� list_wheelΪ�ա�
*/
void sort_time(std::list<Data> &list_imu, std::list<Data> &list_whe, std::list<Data> &lst) {
	std::list<Data>::iterator a = list_imu.begin();
	std::list<Data>::iterator b = list_whe.begin();
	//std::list<Data>::iterator c = lst.begin();

	while (a != list_imu.end() && b != list_whe.end())
	{
		if (a->timestamp <= b->timestamp) {
			lst.push_back(*a);
			a = list_imu.erase(a);
		} else {
			lst.push_back(*b);
			b = list_whe.erase(b);
		}
	}
	if (list_imu.size() > 0) {
		lst.insert(lst.end(), a, list_imu.end());
		list_imu.resize(0);
	}
	if (list_whe.size() > 0) {
		lst.insert(lst.end(), b, list_whe.end());
		list_whe.resize(0);
	}
}

/*
1. ����a��b���ǰ���ʱ���˳��洢�ġ�
2. ��a�е�Ԫ�أ�����ʱ���˳������ȫ�����뵽b�У�ÿ�β����ɾ��a�е�Ԫ�ء�
*/
void sort_time(std::list<Data> &a, std::list<Data> &b) {
	std::list<Data>::iterator ia = a.begin();
	std::list<Data>::iterator ib = b.begin();

	while (ia != a.end())
	{
		// ���b�Ѿ����˽�β����ôa�����ݾ�ȫ������b���
		if (ib == b.end()) {
			//b.push_back(*ia);
			//ia = a.erase(ia);
			//continue;
			b.insert(ib, ia, a.end());
			a.resize(0);
			break;
		}
		// �����ǰa��Ԫ��ʱ��С��b�ģ�����뵽b��ǰλ��
		// ib ��Ȼָ��ǰԪ��(insert����ֵָ������Ԫ��)
		// ia ɾ���󣬷���ֵָ��aɾ����Ԫ�غ�ߵ�λ��
		if (ia->timestamp <= ib->timestamp) {
			b.insert(ib, *ia);
			ia = a.erase(ia);
			continue;
		}
		else {
			ib++;
		}
	}
}
