import cv2
import argparse
import numpy as np

weights_file = 'yolov3.weights'
config_file  = 'yolov3.cfg'
classes_file = 'yolov3.txt'
confidence_threshold = 0.5

def get_output_layers(net):
  layer_names = net.getLayerNames()
  try:
      output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
  except:
      output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

  return output_layers


def count_objects(file, object_class_name):
  file_bytes = np.fromstring(file, np.uint8)
  image = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)

  Width = image.shape[1]
  Height = image.shape[0]
  scale = 0.00392

  classes = None
  with open(classes_file, 'r') as f:
      classes = [line.strip() for line in f.readlines()]
  object_class_index = classes.index(object_class_name)

  net = cv2.dnn.readNet(weights_file, config_file)
  blob = cv2.dnn.blobFromImage(image, scale, (416,416), (0,0,0), True, crop=False)
  net.setInput(blob)

  outs = net.forward(get_output_layers(net))

  class_ids = []
  confidences = []
  boxes = []
  conf_threshold = 0.5
  nms_threshold = 0.4

  for out in outs:
    for detection in out:
      scores = detection[5:]
      class_id = np.argmax(scores)
      confidence = scores[class_id]
      if confidence > confidence_threshold:
        if class_id == object_class_index:
            center_x = int(detection[0] * Width)
            center_y = int(detection[1] * Height)
            w = int(detection[2] * Width)
            h = int(detection[3] * Height)
            x = center_x - w / 2
            y = center_y - h / 2
            class_ids.append(class_id)
            confidences.append(float(confidence))
            boxes.append([x, y, w, h])


  indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

  object_count = 0
  object_coords = []
  for i in indices:
    if class_ids[i] == object_class_index:
      object_count += 1
      box = boxes[i]
      object_coords.append(box[:2])
      

  return {'count': object_count, 'coordinates': object_coords}
  
