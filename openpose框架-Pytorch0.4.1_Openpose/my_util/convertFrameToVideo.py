import cv2
import glob
import numpy as np
import os

convert_img_path = "../dataset/videoframe1/"
save_path = "../dataset/concatVideo-teacher.avi"
fps = 6
size = (1280,720)

# videoWriter = cv2.VideoWriter(save_path,cv2.VideoWriter_fourcc('I','4','2','0'),
# 							  fps,size)

videoWriter = cv2.VideoWriter(save_path,cv2.VideoWriter_fourcc(*'MJPG'),
							  fps,size)

print(convert_img_path+"*.jpg")

images = os.listdir(convert_img_path)
# images = np.unique(images)
for i in range(5300):
	# print("/home/gpu/yang/openpose/dataset/videoframe/{}.jpg".format(i))
	image = cv2.imread("/home/gpu/yang/openpose/dataset/videoframe1/{}.jpg".format(i))

	videoWriter.write(image)


# for img in glob.glob(convert_img_path+"*.jpg"):
# 	read_img = cv2.imread(img)
# 	cv2.imshow('demo',read_img)
# 	videoWriter.write(read_img)
# videoWriter.release()