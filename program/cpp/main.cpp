#include <stdio.h>
#include <io.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

void SplitString(const std::string& s, std::vector<std::string>& v, const std::string& c)
{
	std::string::size_type pos1, pos2;
	pos2 = s.find(c);
	pos1 = 0;
	while (std::string::npos != pos2)
	{
		v.push_back(s.substr(pos1, pos2 - pos1));

		pos1 = pos2 + c.size();
		pos2 = s.find(c, pos1);
	}
	if (pos1 != s.length())
		v.push_back(s.substr(pos1));
}

string imu_file = "D:\\data_xp\\slam\\20190528001448-001-00.loc";
const string GYR = "@GYR";
const string A3D = "@A3D";





int read_imu_earliest(const string &imu_file, long &earliest_gyr, long &earliest_a3d)
{
	string c(" ");
	string line;
	int num = 0;
	ifstream infile(imu_file);
	while (getline(infile, line)) {
		vector<string> v;
		SplitString(line, v, c);
		if (v.size() < 2 || v[1].size() > 8) {
			cout << line << " v.size() < 2 || v[1].size() > 8" << endl;
			continue;
		}
		if (v[0].compare(GYR) == 0) {
			earliest_gyr = stol(v[1]);
			num++;
			continue;
		}
		else if (v[0].compare(A3D) == 0) {
			earliest_a3d = stol(v[1]);
			num++;
			continue;
		}
		if (num >= 2) {
			break;
		}
	}
	return num;
}



int read_imu(const string &imu_file, vector<long> &vec_gyr, vector<long> &vec_a3d, const long earliest=-1)
{
	string c(" ");
	string line;
	int num = 0;
	ifstream infile(imu_file);
	while (getline(infile, line)) {
		num++;
		vector<string> v;
		SplitString(line, v, c);
		if (v.size() < 2 || v[1].size() > 8) {
			//cout << line << " v.size() < 2 || v[1].size() > 8" << endl;
			continue;
		}
		if ( v[0].compare(GYR) == 0 || v[0].compare(A3D) == 0 ) {
			if (stol(v[1]) <= earliest) {
				cout << line << " " << earliest << endl;
				continue;
			}	
		}
		else {
			continue;
		}

		if (v[0].compare(GYR) == 0) {
			vec_gyr.push_back(stol(v[1]));
			//cout << GYR << " " << v[1] << " " << stol(v[1]) << endl;
			
		} else if (v[0].compare(A3D) == 0) {
			vec_a3d.push_back(stol(v[1]));
			//cout << A3D << " " << v[1] << " " << stol(v[1]) << endl;
		}

		if (vec_gyr.size() % 10000 == 0 && vec_gyr.size() > 0) {
			cout << GYR << " " << vec_gyr.size() << " " << num << endl;
			cout << A3D << " " << vec_a3d.size() << " " << num << endl;
			break;
		}
		//if (vec_a3d.size() % 10000 == 0 && vec_a3d.size() > 0) {
		//	cout << A3D << " " << vec_a3d.size() << " " << num << endl;
		//}
	}
	return num;
}



string spo_dir = "D:\\data_xp\\slam\\20190529\\BCAN\\";
const int spo_frame_num = 1600000;
const string ID = "0x0000036b";

int read_speedometer(const string &spo_dir, const int frame_num, vector<string> &vec_spo) {
	int num = 0;
	char filename[300];
	string line;
	string c("\t");
	for (int i = 0; i <= frame_num; i += 10000) {
		sprintf_s(filename, "%sFrame(%d-%d).txt", spo_dir.c_str(), i, i + 9999);
		cout << filename << endl;
		ifstream infile(filename);
		getline(infile, line);
		std::cout << line << endl;
		while (getline(infile, line)) {
			num++;
			vector<string> v;
			SplitString(line, v, c);
			if (v.size() < 4) {
				continue;
			}
			if ( v[3].compare(ID) != 0 ) {
				continue;
			}
			vec_spo.push_back(v[2]);
			if (vec_spo.size() > 0 && vec_spo.size() % 10000 == 0) {
				cout << vec_spo.size() << " " << num << endl;
				break;
			}
		}
	}

	return num;
}

int get_all_files(const string &in_dir, vector<string> &vec_file) {
	int num = 0;
	//目标文件夹路径
	//std::string inPath = "C:\\Program Files\\*";//遍历文件夹下的所有文件
	string inPath = in_dir + "*.txt";
	//用于查找的句柄
	long handle;
	struct _finddata_t fileinfo;
	//第一次查找
	handle = _findfirst(inPath.c_str(), &fileinfo);
	if (handle == -1)
		return -1;
	do
	{
		//找到的文件的文件名
		printf("%s\n", fileinfo.name);
		string s = fileinfo.name;
		cout << s << endl;
		vec_file.push_back(s);

	} while (!_findnext(handle, &fileinfo));

	_findclose(handle);
	return num;
}


int main()
{
 //   // 获取得最早的GYR和A3D的时间戳，两者取较大的作为 IMU 最早时间戳
	//long earliest_gyr = -1;
	//long earliest_a3d = -1;
	//read_imu_earliest(imu_file, earliest_gyr, earliest_a3d);
	//long earliest_imu = earliest_gyr > earliest_a3d ? earliest_gyr : earliest_a3d;
	//cout << " earliest gyr : " << earliest_gyr << endl;
	//cout << " earliest a3d : " << earliest_a3d << endl;
	//cout << " earliest imu : " << earliest_imu << endl;
	//// 读取所有imu数据，要晚于IMU最早时间戳
	//vector<long> vec_gyr;
	//vector<long> vec_a3d;
	//read_imu(imu_file, vec_gyr, vec_a3d, earliest_imu);

	// 依次读取轮速计数据
	//vector<string> vec_spo;
	//read_speedometer(spo_dir, spo_frame_num, vec_spo);

	vector<string> vec_file;
	get_all_files(spo_dir, vec_file);

	system("pause");
	return 0;
}