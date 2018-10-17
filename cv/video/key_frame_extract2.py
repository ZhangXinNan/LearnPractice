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
    i = 0
    frames = []
    while(1):
        ret, frame = cap.read()
        i += 1
        if i > frame_num:
            break
        if frame_interval > 1 and i % frame_interval != 1:
            continue
        frame = resize_image_max_size(frame, max_size)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frames.append(frame)
    return frames


def get_variance(frames, indices):
    means = [np.array(frames[i:j]).mean(axis=0) for (i,j) in indices]
    vars = []
    sum_var = 0.0
    for i, (s, t) in enumerate(indices):
        vars.append(np.sum(np.absolute(frames[s:t] - means[i])))
        sum_var += vars[i]
        vars[i] /= t - s
    sum_var /= len(frames)
    return means, vars, sum_var

def reduce_var(frames, indices, means):
    for i, (s, t) in enumerate(indices[:-1]):
        print(i, s, t)
        d0 = np.sum(np.absolute(frames[t] - means[i]))
        d1 = np.sum(np.absolute(frames[t] - means[i+1]))
        d2 = np.sum(np.absolute(frames[t+1] - means[i]))
        d3 = np.sum(np.absolute(frames[t+1] - means[i+1]))
        print(s, t, indices[i+1])
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


def extract_key_frames(frames, key_frame_num=10, iteration=100):
    num = len(frames)
    assert num > key_frame_num
    interval = num/key_frame_num
    indices = [[int(x * interval), int((x+1) * interval)] for x in range(0, key_frame_num) ]

    means, vars, sum_var = get_variance(frames, indices)
    print(indices)
    print(vars)
    print(sum_var)
    key_frames = []
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

    return key_frames
    # return means


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='D:/github/LearnPractice/cv/OpticalFlow/vtest.avi')
    parser.add_argument('--key_frame_num', default=10, type=int)
    parser.add_argument('--frame_num', default=600, type=int)
    parser.add_argument('--frame_interval', default=1, type=int)
    parser.add_argument('--max_size', default=320, type=int)
    parser.add_argument('--out_dir', default='./keyframe')
    parser.add_argument('--iteration', default=10, type=int)
    parser.add_argument('--delta_var', default=0.01)
    return parser.parse_args()


def main(args):
    print(args)
    frames = get_frames(args.input, args.frame_num, args.frame_interval, args.max_size)
    key_frames = extract_key_frames(frames, args.key_frame_num, args.iteration)

    if not os.path.isdir(args.out_dir):
        os.makedirs(args.out_dir)
    basename = os.path.basename(args.input)
    for i, frame in enumerate(key_frames):
        cv2.imwrite(os.path.join(args.out_dir, basename + '_%d.jpg' % i), frame)

        


if __name__ == '__main__':
    main(get_args())



