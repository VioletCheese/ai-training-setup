import os
import cv2


counter = 1
if not os.path.isdir("jpgs"):
    os.mkdir("jpgs")
for dirpath, dirname, filenames in os.walk("."):
    for filename in filenames:
        filepath = f"{dirpath}/{filename}"

        if filepath[-4:] == ".png":

            image = cv2.imread(filepath)
            cv2.imwrite(f"jpgs/{filename[:-4]}.jpg", image)
            print(f"jpgs/{filename[:-4]}.jpg DONE")
            print(f"JPG count: {counter}")
            counter += 1
