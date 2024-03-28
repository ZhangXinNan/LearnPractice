
# 1 请使用C++实现shared_ptr的operator=，要求与C++11标准库中std::shared_ptr的函数功能一致。

## shared_ptr描述
### 声明
shared_ptr属于C++11特性中新加的一种智能指针，它的实现方式是模版类，头文件<memory>
template <class T> class shared_ptr
所以使用shared_ptr的声明方式即为
std::shared_ptr<type_id> statement 其中type_id为类型（可以是基本数据类型或者类），statement即为模版类对象

### 作用
shared_ptr 的理解如下：

使用一种叫做RAII（Resource Acquisition Is Initialization）的技术作为实现基础：
在对象构造时获取资源，接着控制对资源的访问使之在对象的生命周期内始终保持有效，最后在对象析构的时候释放资源
raii技术的好处是：
不需要显式释放资源
对象所拥有的资源在其生命周期内始终有效
防止忘记调用delete释放内存或者程序异常退出时没有释放内存。
同时它能够将值语义转为引用语义（即shared_ptr可以让多个指针指向相同的对象，共享同一块地址空间），shared_ptr使用引用技术方式来统计当前对象被引用的次数，每一次执行析构函数，引用计数就会-1，当引用计数减为0时自动删除所指对象，回收对象空间。

```c++
template <typename T>
class Shared_ptr{
    private:
        int* p_count;
        T* p_obj;
    public:
        Shared_ptr(T* t){
            this->p_obj = t;
            this->p_count = new int(1);
        }
        ~Shared_ptr(){
            if(*this->p_count > 1){
                *this->p_count--;
            } else if(*this->p_count == 1){
                delete this->p_obj;
                delete this->p_count;
            }
        }
        Shared_ptr& operator=(Shared_ptr& other){
            if(this == &other){ return *this; }
            *this->p_count++;
            // 减少原来的指向
            if(*this->p_count-- == 0){
                delete this->p_obj;
                delete this->p_count;
            }
            // 指向新的对象
            this->p_count = other.p_count;
            this->p_obj = other.p_obj;
        }
};
```

# 2 请使用C/C++或者python实现，给定一个只包含字符(){}[]的字符串，判断字符串中的括号是否有效。有效的括号需要满足以下条件：
   a.左括号必须用相同类型的右括号闭合。
   b.括号必须以正确的顺序闭合。
   例如，输入字符串“([]){}”是有效的，而"([)]"则是无效的。
```python
def check(s):
    tmp = []
    for c in s:
        if len(tmp) < 1:
            if c in [')', '}', ']']:
                return False
            tmp.append(c)
        else:
            if tmp[-1] == '(' and c == ')':
                del tmp[-1]
            elif tmp[-1] == '{' and c == '}':
                del tmp[-1]
            elif tmp[-1] == '[' and c == ']':
                del tmp[-1]
    if len(tmp) == 0:
        return True
    return False
```

# 3 请使用c/c++或者python实现图像的sobel边缘检测，并简述其优缺点。
kernel = [[-1, 0, -1], [-2, 0, -2], [-1, 0, -1]]
def sobel(img, kernel):
    kw = len(kernel[0])
    kh = len(kernel)
    half_kw = kw // 2
    half_kh = kh // 2
    img_sobel = []
    for r in range(len(img) - 2):
        new_row = []
        for c in range(len(img[0]) - 2):
            value = 0
            for y in range(kh):
                for x in range(kw):
                    value += kernel[y][x] * img[r + y][c + x]
            new_row.append(value)
        img_sobel.append(new_row)
    return img_sobel


sobel边缘检测的优点：对边缘部分检测效果较好，对噪声不敏感。
缺点：会出现双边现象。


# 4 请详述OCR技术中的数据处理和算法优化，并举例说明如何解决字符粘连的问题。
数据处理：（1）标注数据：使用ppocrlabel对图上中的文字行位置 和内容进行标注，文本行位置一般采用四点进行标准，即文本行当作一个四边形，用四个顶点来描述其位置。（2）训练数据：通过对训练数据进行裁剪、变形、变色（调整HSV）来扩充数据，或者使用字体来根据一定规则来生成图片样本。
算法优化：如果有文本检测、文本识别两个模型，则标注好的测试数据可以分别评估每个模型的效果。并且最终结果、或者提取的键值对，可以评估整个ocr算法的端到端结果。端到端结果包括整图准确率、字段准确率（提取字段键值对的情况）、文本行准确率、字符准确率等。
举例说明如何解决字符粘连：传统算法中可通过类似retina方法来去除光照光均匀影响。一个文本行中相邻字符的粘连可以通过多次尝试得到不同结果，最终选择总体概率最大的路径。两个文本行之间有粘连，可通过psenet或者dbnet，对文本行进行多次收缩，收缩之后的文本行不会再有粘连，因此会有较好的分割效果。


# 5 请详述OCR技术的基本原理和应用场景。
基本原理：OCR技术是为了识别图片中的文字内容，也包括提取需要的信息。OCR技术一般包括预处理、文本检测、文本识别、版面分析、后处理。预处理一般包括读取图像数据、图像的尺寸缩放、裁减图像中非图像部分（只保留需要识别的部分）、调整图像的对比度等、对图像的方向进行判断（例如横屏可能带来图像旋转）。文本检测主要是把图像中所有的文本行检测出来。文本识别则是把识别检测到的文本行，得到识别结果的字符串。版面分析有些场景下存在，例如图片中表格，需要借助于文本在表格中的位置 来提取所需要的信息。后处理主要是提取所需要的字段（键值对），并整理成接口规定的格式输出。
输入：图像最多来源是手机、相机或者摄像头拍摄得到的图像，也有可能是扫描仪扫描得到的（质量会更好）、截屏（不存在的姿态光照遮挡问题）。

应用场景：自然场景中的文字识别（车牌识别、广告牌识别、仪表仪器上的字符识别）；印刷纸质材料上的文字识别（拍照扫题、发票识别、证件识别）；视频、图片中的文字识别（截屏、视频字幕、PDF中图片的识别）。


