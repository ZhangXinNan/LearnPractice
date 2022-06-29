
# SyncedMemory
把CPU/GPU的数据传输操作封装起来，只要调用简章的接口就能获得两个处理端同步后的数据。

```C++
class SyncedMemory {
public:
  const void* cpu_data();           // 只读获取cpu data
  void set_cpu_data(void* data);    // 设置CPU data
  const void* gpu_data();           // 只读获取gpu data
  void set_gpu_data(void* data);    // 设置GPU data
  void* mutable_cpu_data();         // 读写CPU data
  void* mutable_gpu_data();         // 读取GPU data
  // 状态机变量，4种状态：未初始化，CPU数据有效，GPU数据有效，已同步
  enum SyncedHead { UNINITIALIZED, HEAD_AT_CPU, HEAD_AT_GPU, SYNCED };
  SyncedHead head() { return head_; }   // 获得当前状态机变量
private:
  void* cpu_ptr_;
  void* gpu_ptr_;
  SyncedHead head_; //保存了数据的状态
}
```


# 参考
1. 《深度学习21天实战Caffe》
2. 《深度学习轻松学》