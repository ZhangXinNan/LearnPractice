#coding=utf-8
import copy, numpy as np
np.random.seed(0) # 设置随机数生成种子
# compute sigmoid nonlinearity
def sigmoid(x):
    output = 1/(1+np.exp(-x))
    return output

# convert output of sigmoid function to its derivative
def sigmoid_output_to_derivative(output):
    return output*(1-output)


# training dataset generation
int2binary = {} # 查找表。实数与对应二进制表示的映射。
binary_dim = 8  # 二进制数的最大长度

largest_number = pow(2,binary_dim) # 跟二进制最大长度对应的可以表示的最大十进制数。
binary = np.unpackbits(
    np.array([range(largest_number)],dtype=np.uint8).T,axis=1)
for i in range(largest_number):
    int2binary[i] = binary[i]


# input variables
alpha = 0.1 # 学习率
input_dim = 2 # 一次输入两位字符
hidden_dim = 16 # 隐含层大小
output_dim = 1  # 预测和的值


# initialize neural network weights
synapse_0 = 2*np.random.random((input_dim,hidden_dim)) - 1   # 输入层与隐含层的权值矩阵
synapse_1 = 2*np.random.random((hidden_dim,output_dim)) - 1  # 隐藏层与输出层的权值矩阵
synapse_h = 2*np.random.random((hidden_dim,hidden_dim)) - 1  # 隐藏层与隐藏层的权值矩阵

synapse_0_update = np.zeros_like(synapse_0) # 存储权值更新
synapse_1_update = np.zeros_like(synapse_1) # 
synapse_h_update = np.zeros_like(synapse_h) # 

# training logic
for j in range(10000):
    
    # generate a simple addition problem (a + b = c)
    a_int = np.random.randint(largest_number/2) # int version 防止两数相加超过最大值，限定小于最大值一半
    a = int2binary[a_int] # binary encoding 对应的二进制表示

    b_int = np.random.randint(largest_number/2) # int version
    b = int2binary[b_int] # binary encoding

    # true answer 正确结果
    c_int = a_int + b_int
    c = int2binary[c_int]
    
    # where we'll store our best guess (binary encoded)
    d = np.zeros_like(c) # 存储神经网络的预测值

    overallError = 0 # 重置误差值
    
    layer_2_deltas = list()
    layer_1_values = list()
    layer_1_values.append(np.zeros(hidden_dim))
    
    # moving along the positions in the binary encoding # 遍历二进制数字
    for position in range(binary_dim):
        
        # generate input and output
        X = np.array([[a[binary_dim - position - 1],b[binary_dim - position - 1]]])
        y = np.array([[c[binary_dim - position - 1]]]).T

        # hidden layer (input ~+ prev_hidden)
        layer_1 = sigmoid(np.dot(X,synapse_0) + np.dot(layer_1_values[-1],synapse_h)) # 隐藏层由当前输入层及其连接参数、前隐藏层及其连接参数计算得来

        # output layer (new binary representation)
        layer_2 = sigmoid(np.dot(layer_1,synapse_1))

        # did we miss?... if so by how much?
        layer_2_error = y - layer_2 # 预测误差
        layer_2_deltas.append((layer_2_error)*sigmoid_output_to_derivative(layer_2)) # 导数值存起来
        overallError += np.abs(layer_2_error[0]) # 误差的绝对值，并把它们加起来
    
        # decode estimate so we can print it out
        d[binary_dim - position - 1] = np.round(layer_2[0][0]) #存储当前得到的二进制位
        
        # store hidden layer so we can use it in the next timestep
        layer_1_values.append(copy.deepcopy(layer_1))
    
    future_layer_1_delta = np.zeros(hidden_dim)
    
    for position in range(binary_dim):
        
        X = np.array([[a[position],b[position]]])
        layer_1 = layer_1_values[-position-1] #当前隐藏层
        prev_layer_1 = layer_1_values[-position-2] #前一个隐藏层
        
        # error at output layer
        layer_2_delta = layer_2_deltas[-position-1] # 当前输出层误差
        # error at hidden layer
        layer_1_delta = (future_layer_1_delta.dot(synapse_h.T) + \
            layer_2_delta.dot(synapse_1.T)) * sigmoid_output_to_derivative(layer_1)
        # let's update all our weights so we can try again
        synapse_1_update += np.atleast_2d(layer_1).T.dot(layer_2_delta)
        synapse_h_update += np.atleast_2d(prev_layer_1).T.dot(layer_1_delta)
        synapse_0_update += X.T.dot(layer_1_delta)
        
        future_layer_1_delta = layer_1_delta
    

    synapse_0 += synapse_0_update * alpha
    synapse_1 += synapse_1_update * alpha
    synapse_h += synapse_h_update * alpha    

    synapse_0_update *= 0
    synapse_1_update *= 0
    synapse_h_update *= 0
    
    # print out progress
    if(j % 1000 == 0):
        print "Error:" + str(overallError)
        print "Pred:" + str(d)
        print "True:" + str(c)
        out = 0
        for index,x in enumerate(reversed(d)):
            out += x*pow(2,index)
        print str(a_int) + " + " + str(b_int) + " = " + str(out)
        print "------------"