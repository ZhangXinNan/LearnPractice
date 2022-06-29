
#include "util.h"


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


int get_all_files(const string &in_dir, vector<string> &vec_file)
{
	int num = 0;
	//目标文件夹路径
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
		//printf("%s\n", fileinfo.name);
		string s = fileinfo.name;
		//cout << s << endl;
		vec_file.push_back(s);

	} while (!_findnext(handle, &fileinfo));

	_findclose(handle);
	return num;
}

/*
string s = "09:13:52.077.0";
cout << time2stamp(s) << endl;
*/
long time2stamp(const string& t) {
	//cout << t.substr(0, 2) << " " << std::stoi(t.substr(0, 2)) << endl;
	//cout << t.substr(3, 2) << " " << std::stoi(t.substr(3, 2)) << endl;
	//cout << t.substr(6, 2) << " " << std::stoi(t.substr(6, 2)) << endl;
	//cout << t.substr(9, 3) << " " << std::stoi(t.substr(9, 3)) << endl;
	int h = std::stoi(t.substr(0, 2));
	int m = std::stoi(t.substr(3, 2));
	int s = std::stoi(t.substr(6, 2));
	int ms = std::stoi(t.substr(9, 3));
	long stamp = h * 3600000 + m * 60000 + s * 1000 + ms;
	return stamp;
}