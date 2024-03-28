

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


kernel = [[-1, 0, 1],
          [-2, 0, 2],
          [-1, 0, 1]]

img = [[1,2,3,4,5],
       [6,7,8,9,10],
       [11,12,13,14,15]]

result = sobel(img, kernel)
print(result)

