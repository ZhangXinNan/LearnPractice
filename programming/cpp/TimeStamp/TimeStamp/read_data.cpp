

#include "read_data.h"

const string GYR = "@GYR";
const string A3D = "@A3D";
const string SEPERATOR_IMU = " ";


int read_imu(const string &imu_file, vector<long> &vec_gyr, vector<long> &vec_a3d, const vector<long> &vec_spo)
{
	const long spo_start = vec_spo[0];
	const long spo_end = vec_spo[vec_spo.size() - 1];
	vector<long>::const_iterator iter_spo = vec_spo.begin();

	string line;
	int num = 0;
	ifstream infile(imu_file);
	while (getline(infile, line)) {
		if (iter_spo == vec_spo.end()) {
			break;
		}
		num++;
		vector<string> v;
		SplitString(line, v, SEPERATOR_IMU);
		if (v.size() < 2 || v[1].size() > 10) {
			//cout << line << " v.size() < 2 || v[1].size() > 8" << endl;
			continue;
		}
		if (v[0].compare(GYR) != 0 && v[0].compare(A3D) != 0) {
			continue;

		}
		long timestamp = std::stol(v[1]);
		if (timestamp < spo_start) {
			continue;
		}
		else if (timestamp > spo_end) {
			break;
		}

		if (v[0].compare(GYR) == 0) {
			vec_gyr.push_back(stol(v[1]));
			//cout << GYR << " " << v[1] << " " << stol(v[1]) << endl;
		}
		else if (v[0].compare(A3D) == 0) {
			vec_a3d.push_back(stol(v[1]));
			//cout << A3D << " " << v[1] << " " << stol(v[1]) << endl;
		}
		if (vec_a3d.size() > 0 && vec_gyr.size() > 0 && _min(vec_a3d.size(), vec_gyr.size()) == 1) {
			const long imu_start = _max(vec_a3d[0], vec_gyr[0]);
			while (iter_spo != vec_spo.end()) {
				//if (*iter_spo < )
				iter_spo++;
			}
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




const string ID = "0x0000036b";
const string SEPERATOR_SPO = "\t";

int read_speedometer(const string &spo_dir, const vector<string> &vec_filename, vector<long> &vec_spo) {
	int num = 0;
	string line;
	for (vector<string>::const_iterator iter = vec_filename.begin(); iter != vec_filename.end(); iter++)
	{
		string filename = spo_dir + *iter;
		cout << filename << endl;
		ifstream infile(filename);
		getline(infile, line);
		std::cout << line << endl;
		while (getline(infile, line)) {
			num++;
			vector<string> v;
			SplitString(line, v, SEPERATOR_SPO);
			if (v.size() < 4) {
				continue;
			}
			if (v[3].compare(ID) != 0) {
				continue;
			}
			vec_spo.push_back(time2stamp(v[2].substr(1)));
		}
		//if (vec_spo.size() > 0 && vec_spo.size() % 10000 == 0) {
		cout << vec_spo.size() << " " << num << endl;
		//break;
		//}
	}

	return num;
}


//const string spo_dir = "D:\\data_xp\\slam\\20190529\\BCAN\\";
//// 读取文件列表
//vector<string> vec_file;
//get_all_files(spo_dir, vec_file);
//cout << spo_dir << " size of filename " << vec_file.size() << endl;
//// 依次读取轮速计数据
//vector<long> vec_spo;
//read_speedometer(spo_dir, vec_file, vec_spo);


//// 读取所有imu数据，要晚于IMU最早时间戳
//const string imu_file = "D:\\data_xp\\slam\\20190528001448-001-00.loc";
//vector<long> vec_gyr;
//vector<long> vec_a3d;
////read_imu(imu_file, vec_gyr, vec_a3d, vec_spo);