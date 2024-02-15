import unittest
import numpy as np

from image_processor import count_objects

class TestImageProcessor(unittest.TestCase):

  def run_test(self, filepath, object_class, expected_result):
    with open(filepath, 'rb') as f:
      self.assertEqual(count_objects(np.asarray(bytearray(f.read())), object_class)['count'], 
        expected_result)
  
  def test_image_processor_dog(self):
    self.run_test('images/dog.jpg', 'dog', 1)
    self.run_test('images/crowd2.jpg', 'dog', 0)
    self.run_test('images/motorcycles.jpg', 'dog', 0)
    self.run_test('images/people.jpg', 'dog', 0)
    self.run_test('images/people2.jpg', 'dog', 0)
    self.run_test('images/people3.jpg', 'dog', 0)
      
  def test_image_processor_person(self):
    self.run_test('images/dog.jpg', 'person', 0)
    self.run_test('images/crowd2.jpg', 'person', 7)
    self.run_test('images/motorcycles.jpg', 'person', 0)
    self.run_test('images/people.jpg', 'person', 5)
    self.run_test('images/people2.jpg', 'person', 6)
    self.run_test('images/people3.jpg', 'person', 6)

  def test_image_processor_motorcycle(self):
    self.run_test('images/dog.jpg', 'motorcycle', 0)
    self.run_test('images/crowd2.jpg', 'motorcycle', 0)
    self.run_test('images/motorcycles.jpg', 'motorcycle', 6)
    self.run_test('images/people.jpg', 'motorcycle', 0)
    self.run_test('images/people2.jpg', 'motorcycle', 0)
    self.run_test('images/people3.jpg', 'motorcycle', 0)
