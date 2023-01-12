import os
import numpy as np
import cv2 as cv

if __name__ == "__main__":
    image_path = "images/ori/"
    depth_path = "images/multi/"

    num_image = len(os.listdir(image_path))
    image_name = os.path.join(image_path, "{:010d}.jpg")
    depth_name = os.path.join(depth_path, "{:010d}.jpg")

    image = cv.imread(image_name.format(0))
    h, w, _ = image.shape

    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    video = cv.VideoWriter("demo.mp4", fourcc, 24.0, (w, 2*h), True)
    for i in range(1, num_image):
        image = cv.imread(image_name.format(i))
        depth = cv.imread(depth_name.format(i))
        out = np.vstack((image, depth))
        # cv.imshow("Out", out)
        # cv.waitKey(10)
        video.write(out)

    video.release()
