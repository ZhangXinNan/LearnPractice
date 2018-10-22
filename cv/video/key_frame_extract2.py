'''
使用kmeans聚类
'''
import argparse
import os
import numpy as np
import cv2
from sklearn.cluster import KMeans
from scipy.cluster.vq import whiten, kmeans, vq
import sys
sys.path.append('../../../PCV/')
from PCV.tools import pca

def resize_image_max_size(img, max_size=320):
    h, w = img.shape[:2]
    if max(w, h) > 320:
        if h >= w:
            new_h = 320
            new_w = w * 320 // h
        if w > h:
            new_w = 320
            new_h = h * 320 // w
        img = cv2.resize(img, (new_w, new_h))
    return img

def get_frames(video_file, frame_num=1800, frame_interval=3, max_size=320):
    cap = cv2.VideoCapture(video_file)
    frames = []
    frame_ids = []
    for i in range(frame_num):
        ret, frame = cap.read()
        if frame is None:
            print('frame is None', i)
            break
        if frame_interval > 1 and i % frame_interval != 0:
            continue
        frame = resize_image_max_size(frame, max_size)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frames.append(frame)
        frame_ids.append(i)
    return frames, frame_ids


def get_variance(frames, indices):
    '''
    means   每一段视频的平均图像
    vars    每一段的差值的绝对值的和
    sum_var 总的差值
    '''
    h, w = frames[0].shape[:2]
    means = []
    vars = []
    sum_var = 0.0
    for i, (s, t) in enumerate(indices):
        means.append(np.array(frames[s:t]).mean(axis=0))
        vars.append(np.sum(np.absolute(frames[s:t] - means[i])))
        sum_var += vars[i]
        vars[i] /= (t - s) * w * h
    n = len(frames)
    # 除以帧数*宽*高
    sum_var /= n * h * w
    return means, vars, sum_var



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='D:/github/LearnPractice/cv/OpticalFlow/vtest.avi')
    parser.add_argument('--key_frame_num', default=10, type=int)
    parser.add_argument('--frame_num', default=600, type=int)
    parser.add_argument('--frame_interval', default=1, type=int)
    parser.add_argument('--max_size', default=320, type=int)
    parser.add_argument('--out_dir', default='./keyframe')
    parser.add_argument('--iteration', default=10, type=int)
    # parser.add_argument('--delta_var', default=0.01)
    # parser.add_argument('--time_slice', default=20, type=int)
    return parser.parse_args()


def main(args):
    print(args)
    # 根据指定总帧数和间隔抽取帧
    frames, frame_ids = get_frames(args.input, args.frame_num, args.frame_interval, args.max_size)
    print(len(frames), len(frame_ids), frames[0].shape)

    immatrix = np.array([x.flatten() for x in frames]).astype(np.float32)
    print(immatrix.shape)
    # PCA降维
    V, S, immean = pca.pca(immatrix)
    print(V.shape, S.shape, immean.shape)

    imnbr = len(frames)
    projected = np.array([np.dot(V[:40],immatrix[i]-immean) for i in range(imnbr)])


    # k-means
    projected = whiten(projected)
    centroids,distortion = kmeans(projected, args.key_frame_num)
    code,distance = vq(projected,centroids)
    print(code.shape, distance.shape)
    print(code)
    print(distance)
    # 使用Kmeans进行聚类
    # kmeans = KMeans(n_clusters=args.key_frame_num, random_state=0).fit(np.array(frames))

    centers = []
    clusters = [[] for i in range(args.key_frame_num)]
    ids = [[] for i in range(args.key_frame_num)]
    for i in range(len(frames)):
        clusters[code[i]].append(distance[i])
        ids[code[i]].append(i)
    print(ids)
    print(clusters)
    for i in range(args.key_frame_num):
        index = np.argsort(clusters[i])
        j = index[0]
        print(index)
        index = ids[i][j]
        print(index)
        centers.append((frames[index], index))
    
    if not os.path.isdir(args.out_dir):
        os.makedirs(args.out_dir)
    basename = os.path.basename(args.input)
    for i, (frame, index) in enumerate(centers):
        cv2.imwrite(os.path.join(args.out_dir, basename + '_%d_%d.jpg' % (index,i)), frame)

     

    

if __name__ == '__main__':
    main(get_args())



