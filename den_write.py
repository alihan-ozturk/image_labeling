import cv2 as cv
import numpy as np
import os

class_names = {0: "x1", 1: "x2", 2: "x3", 3: "x4", 4: "x5", 5: "x6"}
path = "C:\\Users\\Alihan\\Desktop\\ds"
labels = dict()
labels_array = np.array([])
last_imgs = []

for img_name in os.listdir(path):
    print(img_name)
    abs_path = os.path.join(path, img_name)
    img = cv.imread(abs_path)
    cv.namedWindow(img_name, cv.WINDOW_NORMAL)
    cv.imshow(img_name, img)
    cv.waitKey()
    cv.destroyWindow(img_name)
    i = 1
    while i:
        which_class = input("s : show again, x : exit, w : write class, b : go back, [0,1,2,3,4,5] assign label : ")
        if which_class == "x":
            print("exit")
            i = 0
        elif which_class == "s":
            cv.namedWindow(img_name, cv.WINDOW_NORMAL)
            cv.imshow(img_name, img)
            cv.waitKey()
            cv.destroyWindow(img_name)
        elif which_class == "w":
            for key,class_name in class_names.items():
                print(key,class_name)
        elif which_class in ["0", "1", "2", "3", "4", "5"]:
            print("{} is assigned as {}nd class".format(img_name, which_class))
            i = 0
        elif which_class == "b":
            print("no, image name, class")
            for num, lst_img_name in enumerate(last_imgs):
                print(num, lst_img_name, labels[lst_img_name])
            which_last_image = int(input("which last image : "))
            if which_last_image<len(last_imgs):
                img_will_change_name = last_imgs[which_last_image]
                abs_path_change = os.path.join(path, img_will_change_name)
                img_will_change = cv.imread(abs_path_change)
                cv.namedWindow(img_will_change_name, cv.WINDOW_NORMAL)
                cv.imshow(img_will_change_name, img_will_change)
                cv.waitKey()
                cv.destroyWindow(img_will_change_name)
                which_class_img_will_change = input("[0,1,2,3,4,5] or with any key quit changing : ")
                if which_class_img_will_change not in ["0", "1", "2", "3", "4", "5"]:
                    print("please enter valid command")
                    continue
                else:
                    old_label = labels[img_will_change_name]
                    labels[img_will_change_name] = which_class_img_will_change
                    print("{} changed from {} to {}".format(img_will_change_name, old_label, which_class_img_will_change))
            else:
                print("please enter valid command")

        else:
            print("please enter valid command")

    if len(last_imgs)>5:
        del last_imgs[-1]
    last_imgs.insert(0,img_name)

    if which_class == "x":
        print("last image {}".format(img_name))
        print("ok computer, see you!")
        break
    else:
        labels[img_name] = which_class
        print("{} was registered as belonging to the {}nd class".format(img_name, which_class))

labels_data = np.array([(key, value) for key, value in labels.items()])
np.save("labels_array.npy", labels_data)