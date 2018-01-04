import numpy as np
import cv2
import os

PATH = 'images/test.jpg'
W = 300
H = 300
STEP = 50
PADDING = 10

im = cv2.imread(PATH)
w = W
h = H or W

height, width = im.shape[:2]
rows = (height - h) // STEP
columns = (width - w) // STEP
panel_shape = (height, width + PADDING + w, im.shape[-1])
panel = np.full(panel_shape, 255, dtype=np.uint8)
panel[:, 0: width, :] = im

rows += int(bool((height - h) % STEP)) + 1
columns += int(bool((width - w) % STEP)) + 1

run = True
first = True
while run:
    flag = True
    for row in range(rows):
        for column in range(columns):
            step = row * columns + column
            l = column * STEP
            t = row * STEP
            r = min(l + W, width)
            b = min(t + H, height)

            l = r - W
            t = b - H

            sub_im = im[t: b, l: r, :]

            panel[0: h, -w:, :] = sub_im
            cv2.imshow('Panel', cv2.rectangle(panel.copy(), (l, t), (r, b), (255, 0, 0), 2))
            print step / float(rows * columns)
            cv2.waitKey(50)
            while first and flag:
                if cv2.waitKey(1) & 0xFF == ord('s'):
                    flag = False
                    break
    first = False
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            run = False
            break
        elif key == ord('s'):
            break

cv2.destroyAllWindows()
