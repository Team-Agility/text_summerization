from utils.s3 import S3Upload
from utils.db import updateStatus
from sequenceTagging.main import main as FeatureTagging
from sequenceTagging.svm import main as SVMModel
from meetingMinute.multi_sentence_compression_single import main as Summarization
import threading
import networkx as nx
# import matplotlib.pyplot as plt
# from networkx.drawing.nx_agraph import graphviz_layout

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

  # topics, nxGraph = meeting.createGraph()
  # plt.figure(figsize=(100,100))
  # nx.draw(nxGraph, nx.spring_layout(nxGraph), with_labels=True)
  # # labels = {e: nxGraph[e[0]][e[1]]['weight'] for e in nxGraph.edges}
  # # nx.draw_networkx_edge_labels(nxGraph, nx.spring_layout(nxGraph), edge_labels=labels)
  # # nx.draw(nxGraph, pos = graphviz_layout(nxGraph), node_size=1200, node_color='lightblue', linewidths=0.25, font_size=10, font_weight='bold', with_labels=True)
  # plt.savefig(f'{DATASET_PATH}/word_graph.png')
  # file_url = S3Upload(id, 'word_graph.png')
  # updateStatus(id, STEPS, len(STEPS), 3, StepsClass(input_dataset, file_url, topics))

  # meeting.findClusters()
  # sequences = meeting.findSequences()
  # updateStatus(id, STEPS, len(STEPS), 5, StepsClass(input_dataset, file_url, topics, sequences, sequences))

def startTraining(id, steps, dataset, dataset_path, input_json):
  global ID, STEPS, INPUT_DATASET, DATASET_PATH, INPUT_JSON
  ID, STEPS, INPUT_DATASET, DATASET_PATH, INPUT_JSON = id, steps, dataset, dataset_path, input_json
  thread = tread(train)
  thread.start()