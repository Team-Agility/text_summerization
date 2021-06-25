from utils.s3 import S3Upload
from utils.thread import StepsClass, startTraining
from utils.db import getAllMeetingIDs, getData
from utils.requests import ClientError, ResponseData, convertToObj
from flask import Flask, request, send_from_directory
from flask_swagger import swagger
from flask_cors import CORS, cross_origin
import uuid
import json
import os
import decimal
import matplotlib
matplotlib.use('Agg')

# def _build_cors_prelight_response():
#     response = make_response()
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     response.headers.add('Access-Control-Allow-Headers', "*")
#     response.headers.add('Access-Control-Allow-Methods', "*")
#     return response

# def _corsify_actual_response(response):
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     return response

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): return float(obj)

DATASET_OUT_DIR = 'dataset'
STEPS = ["Input", "Feature Extraction" ,"Categorized Sequence", "Word Graph Building", "Path re-ranking", "Output"]

app = Flask(__name__, static_url_path='')
CORS(app)
app.json_encoder = JSONEncoder

@app.route('/dataset/<path:path>')
def send_static_files(path):
    return send_from_directory('dataset', path)

@app.route('/<id>', methods=['GET'])
def getResult(id):
  data = getData(id)
  return ResponseData(convertToObj(data['pk'], data['completed_steps'], data['all_steps'], json.loads(data['data'])))

@app.route('/', methods=['GET'])
def getAllMeetings():
    return ResponseData(getAllMeetingIDs())

@app.route('/', methods=['POST'])
def createNewJob():
  id = str(uuid.uuid4())
  print(f'Adding New Meeting {id}')

  data = request.json

  if 'transcript' not in data:
    return ClientError('Paramater `transcript` Required')

  if 'confidence' not in data:
    return ClientError('Paramater `confidence` Required')

  if 'sequences' not in data:
    return ClientError('Paramater `sequences` Required')

  dataset_path = f'{DATASET_OUT_DIR}/{id}'
  if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

  input_json = {}
  with open(f'{dataset_path}/transcript.json', 'w') as f:
    f.write(json.dumps({'transcript' : data['transcript']}, indent=4, sort_keys=True))  
  input_json['transcript'] = S3Upload(id, 'transcript.json')

  with open(f'{dataset_path}/confidence.json', 'w') as f:
    f.write(json.dumps(data['confidence'], indent=4, sort_keys=True))  
  input_json['confidence'] = S3Upload(id, 'confidence.json')

  with open(f'{dataset_path}/abstractive_summary.json', 'w') as f:
    f.write(json.dumps(data['sequences'], indent=4, sort_keys=True)) 
  input_json['sequences'] = S3Upload(id, 'abstractive_summary.json') 

  startTraining(id, STEPS, data, dataset_path, input_json)

  return ResponseData(convertToObj(id, 1, STEPS, StepsClass(input_json)))

@app.route("/spec")
def spec():
    return jsonify(swagger(app))

if __name__ == '__main__':
   app.run(host='0.0.0.0')