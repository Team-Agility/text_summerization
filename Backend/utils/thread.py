from utils.s3 import S3Upload
from utils.db import updateStatus
from main import Meeting
import threading
import networkx as nx
import matplotlib.pyplot as plt
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

ID = STEPS = TRANSCRIPT = None

class tread(threading.Thread):

  def __init__(self, function_that_downloads):
    threading.Thread.__init__(self)
    self.runnable = function_that_downloads
    self.daemon = True

  def run(self):
    self.runnable()

def train():
  global ID, STEPS, TRANSCRIPT, DATASET_PATH
  id, transcript = ID, TRANSCRIPT
  meeting = Meeting(id)
  updateStatus(id, STEPS, len(STEPS), 1, StepsClass(transcript))

  meeting.preprocess()
  updateStatus(id, STEPS, len(STEPS), 2, StepsClass(transcript, ''))

  topics, nxGraph = meeting.createGraph()
  plt.figure(figsize=(100,100))
  nx.draw(nxGraph, nx.spring_layout(nxGraph), with_labels=True)
  # labels = {e: nxGraph[e[0]][e[1]]['weight'] for e in nxGraph.edges}
  # nx.draw_networkx_edge_labels(nxGraph, nx.spring_layout(nxGraph), edge_labels=labels)
  # nx.draw(nxGraph, pos = graphviz_layout(nxGraph), node_size=1200, node_color='lightblue', linewidths=0.25, font_size=10, font_weight='bold', with_labels=True)
  plt.savefig(f'{DATASET_PATH}/word_graph.png')
  file_url = S3Upload(id, 'word_graph.png')
  updateStatus(id, STEPS, len(STEPS), 3, StepsClass(transcript, file_url, topics))

  meeting.findClusters()
  sequences = meeting.findSequences()
  updateStatus(id, STEPS, len(STEPS), 5, StepsClass(transcript, file_url, topics, sequences, sequences))

def startTraining(id, steps, transcript, dataset_path):
  global ID, STEPS, TRANSCRIPT, DATASET_PATH
  ID, STEPS, TRANSCRIPT, DATASET_PATH = id, steps, transcript, dataset_path
  thread = tread(train)
  thread.start()