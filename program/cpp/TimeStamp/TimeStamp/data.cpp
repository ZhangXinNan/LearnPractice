

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
1. 所有链表是按照时间戳顺序排列的。
2. list_imu list_wheel时间戳都在lst之后
3. list_imu list_wheel 中的元素插入到lst中后，要从原链表中移除。最终list_imu 和 list_wheel为空。
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
1. 链表a和b都是按照时间戳顺序存储的。
2. 将a中的元素，根据时间戳顺序，依次全部插入到b中，每次插入后，删除a中的元素。
*/
void sort_time(std::list<Data> &a, std::list<Data> &b) {
	std::list<Data>::iterator ia = a.begin();
	std::list<Data>::iterator ib = b.begin();

	while (ia != a.end())
	{
		// 如果b已经到了结尾，那么a的数据就全部放入b后边
		if (ib == b.end()) {
			//b.push_back(*ia);
			//ia = a.erase(ia);
			//continue;
			b.insert(ib, ia, a.end());
			a.resize(0);
			break;
		}
		// 如果当前a的元素时间小于b的，则插入到b当前位置
		// ib 仍然指向当前元素(insert返回值指向插入的元素)
		// ia 删除后，返回值指向a删除的元素后边的位置
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
