import cv2
import time
import argparse
from openpose import Openpose, draw_person_pose
import pandas as pd
from my_util.util import delfile
from timeit import timeit


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pose detector')
    parser.add_argument('weights', help='weights file path')
    parser.add_argument('--img', '-i', help='image file path')
    parser.add_argument('--webcam', '-w',type=bool, default=False, help='use webcam')
    parser.add_argument('--video', '-v', type=str, default='../dataset/video.mp4', help='use video path')
    parser.add_argument('--precise', '-p', action='store_true', help='do precise inference')
    args = parser.parse_args()

    # load model
    openpose = Openpose(weights_file = args.weights, training = False)

    # read image
    if args.video != '':
        cap = cv2.VideoCapture(args.video)
        print("video FPS = ",cap.get(cv2.CAP_PROP_FPS))

        # cap.set(cv2.CAP_PROP_FPS,50)
    if args.webcam:
        cap = cv2.VideoCapture(0)
        print("webcam FPS = ", cap.get(cv2.CAP_PROP_FPS))
        # cap.set(3, 640)
        # cap.set(4, 480)
        # print(cap)
    frame = 0
    count = 0
    # delete old csv file

    delfile()

    while True:
        ret, img = cap.read()
        # print("img shape",img.shape)
        # img = cv2.resize(img,(1280, 720))
        # inference
        # start = time.clock()
        if count % 5 != 0:
            count += 1
            continue
        else:
            count += 1
            start = time.clock()
            poses, _ = openpose.detect(img, precise=args.precise)
            end = time.clock()
            print("time = %.4fs"%(end-start))

            img,df = draw_person_pose(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), poses)

            # df.to_csv("./csv/df{}.csv".format(frame))

            # cv2.imwrite('result.png', img)
            cv2.imshow('demo', img)  # 一个窗口用以显示原视频
            # cv2.imwrite("../dataset/videoframe1/"+"%d.jpg"%frame,img)
            frame+=1

        key = cv2.waitKey(33)
        if key == 27:  # ESC
            break
    cap.release()
    cv2.destroyAllWindows()







