import cv2
import numpy as np
from numpy.random import *
import itertools

def fill(size, color):
    w, h = size
    canvas =  np.zeros((h, w, 3), dtype="uint8")
    cv2.rectangle(canvas, (0,0), (w,h), color, -1)
    return canvas

def is_nearby(pt1, pt2):
    if (pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2 < 6000:
        return True
    return False

def main(framesize, frame_max, writer):

    # -------------------------------------------------
    # setup
    # -------------------------------------------------
    width, height = framesize

    frame_counter = 0

    radius = 2
    num = 64 # ball len
    max_speed = 3 
    last_pts = [(randint(width), randint(height)) for _ in range(num)]
    dpos = np.array([(randint(max_speed * 2), randint(max_speed * 2)) for _ in range(num)]) - 3 # dx, dy

    color = (222, 222, 222)
    bg_color =  (0, 0, 0)


    # -------------------------------------------------
    # loop
    # -------------------------------------------------
    while True:
        if frame_counter > frame_max:
            break

        canvas = fill(framesize, bg_color)

        for i, pt in enumerate(last_pts):
            dx, dy = dpos[i]

            x = pt[0] + dx
            y = pt[1] + dy

            if x>width or x<0:
                dx *= -1
            if y>height or y<0:
                dy *= -1

            cv2.circle(canvas, pt, radius, color, -1)
            last_pts[i] = [x, y]
            dpos[i] = [dx, dy]


        for pair in itertools.combinations(last_pts, 2): # combination
            pt1, pt2 = pair
            if is_nearby(pt1, pt2):
                cv2.line(canvas, pt1, pt2, color)


        writer.write(canvas)
        cv2.imshow("Canvas", canvas)
        if frame_counter == 0:
            cv2.imwrite('../dots_and_lines.png', canvas)


        key = cv2.waitKey(5)
        if key == 27: # Esc
            break
        frame_counter += 1



if __name__ == "__main__":
    outpath = '../build/canvas_animation2.mp4'

    framesize = (600, 400)
    w, h = framesize
    fps = 30
    frame_max = 10 * fps # 5sec

    fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    writer = cv2.VideoWriter(outpath, fmt, fps, framesize) # ライター作成
    
    
    main(framesize, frame_max, writer)
    writer.release()