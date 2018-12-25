import numpy as np
import os
import lmdb
from PIL import Image 
import numpy as np 
import sys
# Make sure that caffe is on the python path:
caffe_root = 'your caffe root path'
sys.path.insert(0, caffe_root + '/python')
import caffe
####################pre-treatment############################
#txt with labels eg. (0001.jpg 2 5)
file_input=open('your label txt','r')
img_list=[]
label1_list=[]
label2_list=[]
for line in file_input:
    content=line.strip()
    content=content.split(' ')
    img_list.append(int(content[1]))
    label1_list.append(int(content[1]))
    label2_list.append(int(content[2]))
    del content
file_input.close() 
####################train data(images)############################
#your data lmdb path
#注意一定要先删除之前生成的lmdb，因为lmdb会在之前的数据基础上新增数据，而不会先清空
#os.system('rm -rf  ' + your data(images) lmdb path)
in_db=lmdb.open('your data(images) lmdb path',map_size=int(1e12))
with in_db.begin(write=True) as in_txn:
    for in_idx,in_ in enumerate(img_list):         
        im_file='your images path'+in_
        im=Image.open(im_file)
        im = im.resize((w,h),Image.BILINEAR)#放缩图片，分类一般用
        #双线性BILINEAR，分割一般用最近邻NEAREST，**注意准备测试数据时一定要一致**
        im=np.array(im) # im: (w,h)RGB->(h,w,3)RGB
        im=im[:,:,::-1]#把im的RGB调整为BGR
        im=im.transpose((2,0,1))#把height*width*channel调整为channel*height*width
        im_dat=caffe.io.array_to_datum(im)
        in_txn.put('{:0>10d}'.format(in_idx),im_dat.SerializeToString())   
        print 'data train: {} [{}/{}]'.format(in_, in_idx+1, len(file_list))        
        del im_file, im, im_dat
in_db.close()
print 'train data(images) are done!'
######train data of label################    
#your labels lmdb path
in_db=lmdb.open('your labels lmdb path',map_size=int(1e12))
with in_db.begin(write=True) as in_txn:
    for in_idx,in_ in enumerate(img_list):
        target_label=np.zeros((2,1,1))# 2种label
        target_label[0,0,0]=label1_list[in_idx]
        target_label[1,0,0]=label2_list[in_idx]
        label_data=caffe.io.array_to_datum(target_label)
        in_txn.put('{:0>10d}'.format(in_idx),label_data.SerializeToString())
        print 'label train: {} [{}/{}]'.format(in_, in_idx+1, len(file_list))
        del target_label, label_data    
in_db.close()
print 'train labels are done!'