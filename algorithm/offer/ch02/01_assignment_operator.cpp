

#include <iostream>

class CMyString{
public:
  CMyString(char* pData = NULL);
  CMyString(const CMyString& str);
  ~CMyString(void);
  void print() {
    std::cout << this->m_pData << std::endl;
  }
  CMyString& operator =(const CMyString& str);
private:
  char* m_pData;
};

CMyString::CMyString(char* pData){
  std::cout << "CMyString::CMyString(char* pData = NULL)" << std::endl;
  this->m_pData = 0;
  if (pData) {
    this->m_pData = new char[strlen(pData) + 1];
    std::strcpy(this->m_pData, pData);
  }
}

CMyString::CMyString(const CMyString& str) {
  std::cout << "CMyString::CMyString(const CMyString& str)" << std::endl;

  this->m_pData = 0;
  if (str.m_pData == 0) {
    return ;
  } else {
    this->m_pData = new char[strlen(str.m_pData) + 1];
    std::strcpy(this->m_pData, str.m_pData);
  }
}

CMyString::~CMyString(void) {
  std::cout << "CMyString::~CMyString(void)" << "size of str:" << strlen(this->m_pData) << "-------" << this->m_pData << std::endl;
  delete[] this->m_pData;
  this->m_pData = 0;
  //std::cout << "CMyString::~CMyString(void)" << "size of str:" << "-------"  << std::endl;
}

CMyString& CMyString::operator =(const CMyString& str) {
  std::cout << "CMyString& CMyString::operator=(const CMyString& str) " << std::endl;
  if (this->m_pData == str.m_pData) {
    return *this;
  }
  delete[] this->m_pData;
  this->m_pData = 0;
  this->m_pData = new char[strlen(str.m_pData) + 1];
  std::strcpy(this->m_pData, str.m_pData);
  return *this;
}


int main() {
  CMyString str = "we are champion";
  str.print();
  CMyString str1("are you ok");
  str1.print();
  CMyString str2(str);
  str2.print();
  CMyString str3;
  str3 = str;
  str3.print();
  return 0;
}
