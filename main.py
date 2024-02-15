from typing import Union, Annotated
from fastapi import FastAPI, File, UploadFile
import image_processor

app = FastAPI()

@app.get('/')
def heartbeat():
  return {'health': 'ok'}
  
@app.post('/count_people')
def count_objects(file: UploadFile):
  object_class = 'person'
  result = image_processor.count_objects(file.file.read(), object_class)
  return { 'object': object_class, 'result': result}
  
@app.post('/count_dogs')
def count_objects(file: UploadFile):
  object_class = 'dog'
  result = image_processor.count_objects(file.file.read(), object_class)
  return { 'object': object_class, 'result': result}
  
@app.post('/count_motorcycles')
def count_objects(file: UploadFile):
  object_class = 'motorcycle'
  result = image_processor.count_objects(file.file.read(), object_class)
  return { 'object': object_class, 'result': result}
  


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
  return {'item_id': item_id, 'q': q}