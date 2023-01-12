import os
import numpy as np
import cv2 as cv

if __name__ == "__main__":
    image_path = "images/ori/"
    mono_path = "images/mono/"
    multi_path = "images/multi/"

    num_image = len(os.listdir(image_path))
    image_name = os.path.join(image_path, "{:010d}.jpg")
    mono_name = os.path.join(mono_path, "{:010d}.jpg")
    multi_name = os.path.join(multi_path, "{:010d}.jpg")

    image = cv.imread(image_name.format(0))
    h, w, _ = image.shape

    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    video = cv.VideoWriter("compare.mp4", fourcc, 12.0, (w, 3*h), True)
    for i in range(1, num_image):
        image = cv.imread(image_name.format(i))
        mono = cv.imread(mono_name.format(i))
        multi = cv.imread(multi_name.format(i))
        out = np.vstack((image, mono, multi))
        cv.putText(out, "{:010d}".format(i), (5, 50), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
        # cv.imshow("Out", out)
        # cv.waitKey(10)
        video.write(out)

    video.release()
