TEST_DIR = '/model/sample_images/'
SAMPLES = 10

import numpy as np
import cv2
import tensorflow as tf
import glob
from matplotlib import pyplot as plt
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils

PATH_TO_BIKE_MODEL = "bike/saved_model"
bike_model = tf.saved_model.load(PATH_TO_BIKE_MODEL)

PATH_TO_PLATE_MODEL = "number_plate/saved_model"
plate_model = tf.saved_model.load(PATH_TO_PLATE_MODEL)

ext = ['png', 'jpg', "JPG", "JPEG", "jpeg"]
test_filenames = []
[test_filenames.extend(glob.glob(TEST_DIR + '*.' + e)) for e in ext]

count = 0
for image_path in test_filenames:
  if(count == SAMPLES):
    break
  if image_path.find(".jpg") != -1 or image_path.find(".jpeg") != -1:
    count = count+1
    image = cv2.imread(image_path)
    arr = np.array(image)
    input_tensor = tf.convert_to_tensor(arr)
    input_tensor = input_tensor[tf.newaxis]
    detections = bike_model(input_tensor)

    h = image.shape[0]
    w = image.shape[1]

    boxes = detections['detection_boxes']
    scores = detections['detection_scores']

    #image width = 300
    #image height = 168
    cv2.rectangle(image, (int(boxes[0][0][1]*w), int(boxes[0][0][0]*h)),
                  (int(boxes[0][0][3]*w), int(boxes[0][0][2]*h)), (255, 0, 0), 3)
    image1 = image[int(boxes[0][0][0]*h): int(boxes[0][0][2]*h),
                  int(boxes[0][0][1]*w):int(boxes[0][0][3]*w)]
                  
    arr1 = np.array(image1)
    input_tensor1 = tf.convert_to_tensor(arr1)
    input_tensor1 = input_tensor1[tf.newaxis]
    detections1 = plate_model(input_tensor1)

    boxes1 = detections1['detection_boxes']
    h1 = image1.shape[0]
    w1 = image1.shape[1]

    cv2.rectangle(image1, (int(boxes1[0][0][1]*w1), int(boxes1[0][0][0]*h1)),
                  (int(boxes1[0][0][3]*w1), int(boxes1[0][0][2]*h1)), (255, 0, 0), 3)

    number_plate = image1[int(boxes1[0][0][0]*h1): int(boxes1[0][0][2]*h1),
                          int(boxes1[0][0][1]*w1): int(boxes1[0][0][3]*w1)]
    h2 = number_plate.shape[0]
    w2 = number_plate.shape[1]
    output_path = f"/output/image_{count}.jpg"
    cv2.imwrite(output_path, number_plate)
    plt.figure(figsize=(h2,w2))
    plt.imshow(number_plate)

