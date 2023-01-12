from matplotlib import image


import os

image_path = "images/ori/"
image_names = os.listdir(image_path)
image_names = sorted(image_names)
for i in range(len(image_names)):
    # fmt: off
    os.rename(
        os.path.join(image_path, image_names[i]),
        os.path.join(image_path, "{:010d}.jpg".format(i))
    )
    # fmt: on
    pass
