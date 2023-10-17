
# BOXES = [(X1,Y1,X2,Y2, CONF)]

def sorted_by_conf(boxes):
    for i in range(len(boxes) - 1):
        for j in range(i+1, len(boxes)):
            if boxes[j][-1] > boxes[i][-1]:
                boxes[i], boxes[j] = boxes[j], boxes[i]


def iou(a, b):
    ix = min(a[2], b[2]) - max(a[0], b[0])
    iy = min(a[3], b[3]) - max(a[1], b[1])
    if ix <= 0 or iy <= 0:
        return 0
    sa = (a[2] - a[0]) * (a[3] - a[1])
    sb = (b[2] - b[0]) * (b[3] - b[1])
    return ix * iy / (sa + sb - ix * iy)


def nms(boxes, thresh_iou=0.5):
    sorted_by_conf(boxes)
    boxes_valid = [boxes[0]]

    for i in range(1, len(boxes)):
        max_iou = 0
        for j in range(0, i):
            tmp_iou = iou(boxes[j], boxes[i])
            if tmp_iou > max_iou:
                max_iou = tmp_iou
            if max_iou >= thresh_iou:
                break
        if max_iou < thresh_iou:
            boxes_valid.append(boxes[j])
    return boxes_valid

