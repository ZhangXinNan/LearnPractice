'''

'''
import numpy as np
import cv2

def draw_flow(im, flow, step=16):
    """在间隔分开的像素采样点绘制光流"""
    h,w = im.shape[:2]
    y,x = np.mgrid[step//2:h:step, step//2:w:step].reshape(2,-1)
    fx, fy = flow[y,x].T

    # 创建线的终点
    lines = np.vstack([x,y,x+fx,y+fy]).T.reshape(-1,2,2)
    lines = np.int32(lines)
    # 创建图像并绘制
    vis = cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)
    for (x1,y1),(x2,y2) in lines:
        cv2.line(vis, (x1,y1), (x2,y2), (0,255,0), 1)
        cv2.circle(vis,(x1,y1), 1, (0,255,0), -1)
    return vis
# 设置视频捕获
cap = cv2.VideoCapture(0)
ret, im = cap.read()
prev_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

while True:
    ret, im = cap.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # 计算流
    flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    prev_gray = gray
    # 画出流矢量
    cv2.imshow('Optical flow', draw_flow(gray, flow))
    if cv2.waitKey(10) == 27:
        break