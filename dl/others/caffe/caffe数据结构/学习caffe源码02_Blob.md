# Blob
Blob实际是一个4维的张量 **(N,C,H,W)**。
自动同步CPU/GPU上的数据。
Caffe类中成员变量全部带后缀“_”，容易区分临时变量和类成员变量。
```c++
template <typename Dtype>
class Blob {
  public:
    Dtype* mutable_cpu_data(); // 读写访问cpu数据上data的数据
    Dtype* mutable_gpu_data(); // 读写访问gpu数据上data的数据
    Dtype* mutable_cpu_diff(); // 读写访问cpu数据上diff的数据
    Dtype* mutable_gpu_diff(); // 读写访问gpu数据上diff的数据
    void Update();            // 实现了data = data - diff操作
    void FromProto(const BlobProto& proto, bool reshape = true);        // 从序列化中得到proto
    void ToProto(BlobProto* proto, bool write_diff = false) const;      // 将proto序列化
    Dtype asum_data() const;  // 计算data的L1范数，绝对值之和
    Dtype asum_diff() const;  // 计算diff的L1范数，绝对值之和
    Dtype sumsq_data() const; // 计算data的L2范数，平方和
    Dtype sumsq_diff() const; // 计算diff的L2范数，平方和
  protected:
    shared_ptr<SyncedMemory> data_; //存储原始数据
    shared_ptr<SyncedMemory> diff_; // 反向传播的梯度更新值
    shared_ptr<SyncedMemory> shape_data_;
    vector<int> shape_;             //形状信息
    int count_;
    int capacity_;

    DISABLE_COPY_AND_ASSIGN(Blob);
};  // class Blob
```


# 参考
1. 《深度学习21天实战Caffe》
2. 《深度学习轻松学》