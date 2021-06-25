from utils.db import updateStatus
from sequenceTagging.main import main as FeatureTagging
from sequenceTagging.svm import main as SVMModel
from meetingMinute.multi_sentence_compression_single import main as Summarization
import threading
import os

def StepsClass(input = [], features = [], sequences = [], wordgraphs = [], rerank = [], output = []):
  return [
    {
      "type": "confidenceSequence",
      "step": "Input",
      "data": input
    },
    {
      "type": "featureExtraction",
      "step": "Feature Extraction",
      "data": features
    },
    {
      "type": "categorizedSequence",
      "step": "Categorized Sequence",
      "data": sequences
    },
    {
      "type": "imageArray",
      "step": "Word Graph Generate",
      "data": wordgraphs   
    },
    {
      "type": "summery",
      "step": "Path re-ranking",
      "data": rerank 
    },
    {
      "type": "abstractiveSummery",
      "step": "Output",
      "data": output  
    }
  ]

ID = STEPS = INPUT_DATASET = INPUT_JSON = None

class tread(threading.Thread):

  def __init__(self, function_that_downloads):
    threading.Thread.__init__(self)
    self.runnable = function_that_downloads
    self.daemon = True

  def run(self):
    self.runnable()

def train():
  global ID, STEPS, INPUT_DATASET, DATASET_PATH, INPUT_JSON
  id, input_dataset, input_json = ID, INPUT_DATASET, INPUT_JSON
  features = FeatureTagging(True, id)
  updateStatus(id, STEPS, len(STEPS), 2, StepsClass(input_json, features))

  model = SVMModel(True)
  sequences = {
    'actions': [],
    'decisions': [],
    'problems': []
  }

  abstract = input_dataset['sequences']['abstract']
  actions = input_dataset['sequences']['actions']
  decisions = input_dataset['sequences']['decisions']
  problems = input_dataset['sequences']['problems']

  all_sequences_idx = abstract + actions + decisions + problems
  print(all_sequences_idx)

  for idx, utt in enumerate(features):
    category = model.predict([[utt['prob_of_confidence_utterances'], utt['prob_of_unconfident_utterances'], utt['prob_of_neutral_utterances'], utt['no_of_speakers'], utt['total_no_of_utterance_length'], utt['no_of_utterances'], utt['total_no_of_time_difference'], utt['total_sequence_duration'], utt['overlapping_time']]])[0]
    sequences[f'{category}s'].append(all_sequences_idx[idx]['extract_summ'])

  updateStatus(id, STEPS, len(STEPS), 3, StepsClass(input_json, features, sequences))

  Summarization([id])

  wordgraphs = []
  for file in os.listdir(f'{DATASET_PATH}/graphs/'):
    # wordgraphs.append(S3Upload(id, f'graphs/{file}'))
    wordgraphs.append(f'http://localhost:5000/dataset/{id}/graphs/{file}')


  with open(f'{DATASET_PATH}/summary.txt') as f:
    summary = f.readlines()
  summary = [x.strip() for x in summary] 

  output = {
    'actions': [],
    'decisions': [],
    'problems': []
  }

  no_of_actions = len(sequences['actions'])
  no_of_decisions = len(sequences['decisions'])
  no_of_problems = len(sequences['problems'])

  output['actions'] = summary[0:no_of_actions]
  output['decisions'] = summary[no_of_actions:no_of_actions+no_of_decisions]
  output['problems'] = summary[no_of_actions+no_of_decisions:no_of_actions+no_of_decisions+no_of_problems]

  updateStatus(id, STEPS, len(STEPS), 6, StepsClass(input_json, features, sequences, wordgraphs, [], output))

def startTraining(id, steps, dataset, dataset_path, input_json):
  global ID, STEPS, INPUT_DATASET, DATASET_PATH, INPUT_JSON
  ID, STEPS, INPUT_DATASET, DATASET_PATH, INPUT_JSON = id, steps, dataset, dataset_path, input_json
  thread = tread(train)
  thread.setDaemon(True)
  thread.start()