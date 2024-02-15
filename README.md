# Object counter using FastAPI and OpenCV's YOLO algrothm

This is the implementation of a webservice that implements a REST endpoint that counts the number of objects detected in a passed image.

## Dependencies
* fastapi
* opencv
* numpy

`pip install fastapi opencv numpy`

Download the pre-trained YOLO v3 weight file from [here](https://pjreddie.com/media/files/yolov3.weights) and place in the current directory.



## Starting the webservice

To start the webservice, run: `uvicorn main:app --reload`

The service will be ready to receive requests on its endpoints.


##Accessing the endpoint

There are three different endpoints which count different object classes: count_people, count_motorcycles, and count_dogs.

`curl -F file=@<image_file_path> localhost:8000/count_people`

`curl -F file=@<image_file_path> localhost:8000/count_motorcycles`

`curl -F file=@<image_file_path> localhost:8000/count_dogs`

Sample image files are in the `images` directory.

For example:

`curl -F file=@images/dog.jpg localhost:8000/count_dogs`

`curl -F file=@images/motorcycles.jpg localhost:8000/count_motorcycles`

`curl -F file=@images/people.jpg localhost:8000/count_people`

The result will be returned as a JSON object.


##Running the unit tests

Unit tests are contained in the `tests` directory.

To run: `python3 -m unittest tests/test_image_processor.py`

Tests should run successfully.


##Acknowledgements

Code for running the OpenCV YOLO model is based on code in:
https://github.com/arunponnusamy/object-detection-opencv
