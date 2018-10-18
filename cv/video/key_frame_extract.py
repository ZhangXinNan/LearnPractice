import argparse
import os
import numpy as np
import cv2

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


def reduce_var(frames, indices, means):
    for i, (s, t) in enumerate(indices[:-1]):
        # frame_mid0 = frames[(s+t)//2]
        # frame_mid1 = frames[(indices[i+1][0] + indices[i+1][1])//2]
        d0 = np.sum(np.absolute(frames[t] - means[i]))
        d1 = np.sum(np.absolute(frames[t] - means[i+1]))
        d2 = np.sum(np.absolute(frames[t+1] - means[i]))
        d3 = np.sum(np.absolute(frames[t+1] - means[i+1]))
        print(i, s, t, indices[i+1])
        if d0 > d1 and d2 > d3 and indices[i+1][1] - indices[i+1][0] > 10:
            # 右移
            indices[i][1] += 1
            indices[i+1][0] += 1
        elif d3 > d2 and d1 > d0 and t - s > 10:
            # 左移
            indices[i][1] -= 1
            indices[i+1][0] -= 1
    means = [np.array(frames[i:j]).mean(axis=0) for (i,j) in indices]
    return indices, means


def extract_key_frames(frames, frame_ids, key_frame_num=10, iteration=100):
    num = len(frames)
    assert num > key_frame_num
    interval = num/key_frame_num
    indices = [[int(x * interval), int((x+1) * interval)] for x in range(0, key_frame_num) ]

    means, vars, sum_var = get_variance(frames, indices)
    print(indices)
    print(vars)
    print(sum_var)
    key_frames = []
    key_frame_ids = []
    for i in range(iteration):
        indices, means = reduce_var(frames, indices, means)
        means, vars, sum_var = get_variance(frames, indices)
        print(i, '-----------------------')
        print(indices)
        print(vars)
        print(sum_var)
    print(indices)
    for s, t in indices:
        key_frames.append(frames[(s+t)//2])
        key_frame_ids.append((s+t)//2)

    return key_frames, key_frame_ids
    # return means



def filter_similar_frame(key_frames, kf_num):
    m = len(key_frames)
    if m <= kf_num:
        return key_frames
    dd = np.zeros((m, m))
    ds = np.zeros(m)
    h, w = key_frames[0].shape[:2]
    size = w * h
    for i in range(m):
        for j in range(m):
            if j <= i:
                continue
            dd[j,i] = dd[i, j] = np.sum(np.absolute(key_frames[i] - key_frames[j]))/size
        ds[i] = np.sum(dd[i,:])
    ind = np.unravel_index(np.argsort(dd, axis=None), dd.shape)
    print(dd)
    print(ds)
    print(ind)
    ind_key = []
    for x in range(m):
        r, c = ind[0][m - x - 1], ind[1][m - x - 1]
        if r in ind_key or c in ind_key:
            continue
        # if ds[r] >= ds[c]:
        #     ind_key.append(r)
        # elif ds[c] > ds[r]:
        #     ind_key.append(c)
        ind_key.append(r)
        if len(ind_key) >= kf_num:
            break
    print(ind_key)
    return np.array(key_frames)[ind_key]

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='D:/github/LearnPractice/cv/OpticalFlow/vtest.avi')
    parser.add_argument('--key_frame_num', default=10, type=int)
    parser.add_argument('--frame_num', default=600, type=int)
    parser.add_argument('--frame_interval', default=2, type=int)
    parser.add_argument('--max_size', default=320, type=int)
    parser.add_argument('--out_dir', default='./keyframe')
    parser.add_argument('--iteration', default=10, type=int)
    parser.add_argument('--delta_var', default=0.01)
    parser.add_argument('--time_slice', default=20, type=int)
    return parser.parse_args()


def main(args):
    print(args)
    # 根据指定总帧数和间隔抽取帧
    frames, frame_ids = get_frames(args.input, args.frame_num, args.frame_interval, args.max_size)
    # 使用平分+距离调整分割点获取若干分段视频帧
    key_frames, key_frame_ids = extract_key_frames(frames, frame_ids, args.key_frame_num, args.iteration)

    # 从前边按时间分段获取的关键帧中再去除方差小的
    # key_frames = filter_similar_frame(key_frames, args.key_frame_num)

    if not os.path.isdir(args.out_dir):
        os.makedirs(args.out_dir)
    basename = os.path.basename(args.input)
    for i, frame in enumerate(key_frames):
        cv2.imwrite(os.path.join(args.out_dir, basename + '_%d_%d.jpg' % (i, key_frame_ids[i])), frame)

        


if __name__ == '__main__':
    main(get_args())



