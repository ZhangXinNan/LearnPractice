#include <string>
#include <sstream>
#include <vector>
#include <iostream>


std::vector<std::string> split(const std::string &s, const std::string& delim) {
    //std::cout << s << " split by " << delim << std::endl; 
    std::vector<std::string> elems;
    std::string::size_type begin = 0;
    std::string::size_type pos = s.find(delim, begin);

    while(pos != std::string::npos) {
        //std::cout << "pos:" << pos << ", begin:" << begin << std::endl;
        elems.push_back(s.substr(begin, pos - begin));
        begin = pos + delim.size();
        pos = s.find(delim, begin);
    }
    if (pos == std::string::npos) {
        elems.push_back(s.substr(begin, s.size()-begin));
    }
    return elems;
}

int main(int args, char* argv[]) {
    if (args < 3) {
        return -1;
    }
    std::string s(argv[1]);
    std::string delim(argv[2]);
    std::vector<std::string> vec = split(s, delim);
    for (size_t i = 0; i < vec.size(); i++) {
        std::cout << "[" + vec[i] + "]" << std::endl;
        
    }
    return 0;

}
