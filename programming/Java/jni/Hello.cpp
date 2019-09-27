#include "Hello.h"
#include <stdio.h> 
// 与 Hello.h 中函数声明相同
JNIEXPORT void JNICALL Java_Hello_SayHello(JNIEnv * env, jobject arg, jstring instring) 
{ 
  // 从 instring 字符串取得指向字符串 UTF 编码的指针
const jbyte *str = 
       (const jbyte *)env->GetStringUTFChars( instring, JNI_FALSE ); 
   printf("Hello,%s\n",str); 
    // 通知虚拟机本地代码不再需要通过 str 访问 Java 字符串。
   env->ReleaseStringUTFChars( instring, (const char *)str ); 
   return; 
}
