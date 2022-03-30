import cv2 as cv
import os
''' 
image = cv.imread('DataSet/testing_folder/images/image_1.png')
mask = cv.imread('DataSet/testing_folder/masks/image_1.png')
print(image.shape)
print(mask.shape)
'''
image_names = os.listdir('DataSet/training_folder/images')

for image_name in image_names:
    image_path = 'DataSet/training_folder/images/' + image_name
    mask_path = 'DataSet/training_folder/masks/' + image_name

    image = cv.imread(image_path)
    mask = cv.imread(mask_path)
    print(image.shape)
    print(mask.shape)

    image = cv.resize(image, (760, 428))
    mask = cv.resize(mask, (760, 428))
    os.remove(image_path)
    cv.imwrite(image_path, image)
    os.remove(mask_path)
    cv.imwrite(mask_path, mask)