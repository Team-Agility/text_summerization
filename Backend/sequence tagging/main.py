import json
import glob
import os
import copy
import pprint

# DATASET_DIR = 'dataset'
# DATASET_DIR = "/media/bhanuka/Bhanuka/Projects/FYP/Datasets/AMI-Corpus-JSON-Data-Manupulator/dataset"
DATASET_DIR = "C:/Project/FYP/FYP/AMI-Corpus-JSON-Data-Manupulator/dataset"
os.remove('dataset.csv')

"""
  Get All Dataset's Meeting IDs
  
  :return: String Array with Meeting IDs
"""


def GetAllMeetingIDs():
    files = [os.path.basename(folder_path) for folder_path in glob.glob(f'{DATASET_DIR}/*')]
    meetings = []
    for file in files:
        if '.' not in file and len(file) == 7:
            meetings.append(file)
    # return meetings
    # return meetings[0:16]
    # return ['ES2002a', 'ES2003a', 'ES2004a', 'ES2005a']
    return ['ES2002a', 'ES2003a', 'ES2004a', 'ES2005a', 'ES2002b', 'ES2003b', 'ES2004b', 'ES2005b',
            'ES2002c', 'ES2003c', 'ES2004c', 'ES2005c', 'ES2002d', 'ES2003d', 'ES2004d', 'ES2005d']


class Meeting:
    def __init__(self, meeting_id):
        self.meeting_id = meeting_id
        self.meeting_dir = f'{DATASET_DIR}/{self.meeting_id}'
        self.abs_summ = []
        self.sub_sequences = []
        self.confidence = []
        self.transcript = []

        self.loadSequences()
        self.loadConfidence()
        self.loadTranscript()

        print('\n')

    """
    Load Confidence
    """

    def loadConfidence(self):
        with open(f'{self.meeting_dir}/confidence.json') as f:
            self.confidence = json.load(f)

    """
        Load Transcript
        """

    def loadTranscript(self):
        with open(f'{self.meeting_dir}/transcript.json') as f:
            self.transcript = json.load(f)

    """
    Load Sequences
    """

    def loadSequences(self):
        with open(f'{self.meeting_dir}/abstractive_summary.json') as f:
            self.abs_summ = json.load(f)

        actions = self.abs_summ['actions']
        decisions = self.abs_summ['decisions']
        problems = self.abs_summ['problems']

        for action in actions:
            self.sub_sequences.append({
                'sub_sequence': action['extract_summ'],
                'type': 'action',
                'summary': action['summary']
            })

        for problem in problems:
            self.sub_sequences.append({
                'sub_sequence': problem['extract_summ'],
                'type': 'problem',
                'summary': problem['summary']
            })

        for decision in decisions:
            self.sub_sequences.append({
                'sub_sequence': decision['extract_summ'],
                'type': 'decision',
                'summary': decision['summary']
            })

    def getSequence(self):
        return self.sub_sequences

    def getConfidence(self):
        return self.confidence

    def getTranscript(self):
        return self.transcript


dataset = []

# output file path
overlapping_word = '../results/overlapping-word/temp.json'
# open output file
overlapping_word_file = open(overlapping_word, 'w+')

# problem #decision #action
time_utterance_problem = []
utterance_numbers_problem = []
time_utterance_decision = []
utterance_numbers_decision = []
time_utterance_action = []
utterance_numbers_action = []
number_problem = 0
number_decision = 0
number_action = 0

for meeting_id in GetAllMeetingIDs():
    print("\n----- ", meeting_id, "-------------\n")

    meeting = Meeting(meeting_id)
    sequences = meeting.getSequence()
    confidence = meeting.getConfidence()
    # pprint.pprint(sequences, width=300)

    overlapping_word_file.write("\nsequences : type : " + type(sequences).__name__ + "\n")
    overlapping_word_file.write("\nsequences : str : " + str(sequences) + "\n")

    for index, sequence in enumerate(sequences):
        speakers = []
        total_no_of_utterance_length = 0
        total_no_of_time_difference = 0
        no_of_utterances = len(sequence['sub_sequence'])
        no_of_confidence_utterances = 0
        no_of_unconfident_utterances = 0
        total_sequence_duration = 0

        all_words = []

        # sort by name (Ascending order)
        seq = sequence['sub_sequence']
        overlapping_word_file.write("\nseq  : type " + type(seq).__name__ + "\n")
        overlapping_word_file.write("\nseq  : str " + str(seq) + "\n")

        # sorted_sub_sequence = copy.deepcopy(seq).sort(key=lambda x: x.get('start_time'))
        sorted_sub_sequence = copy.deepcopy(seq)
        sorted_sub_sequence.sort(key=lambda x: x.get('start_time'))
        # sorted_sub_sequence = seq[:].sort(key=lambda x: x.get('start_time'))
        overlapping_word_file.write("\nsorted_sub_sequence  : type " + type(sorted_sub_sequence).__name__ + "\n")
        overlapping_word_file.write("\nsorted_sub_sequence  : str " + str(sorted_sub_sequence) + "\n")
        overlapping_word_file.write("\nutterance : total_sequence_duration : " + str(total_sequence_duration) + "\n")

        for idx, utterance in enumerate(sorted_sub_sequence):
            # print("utterance : ", utterance)
            overlapping_word_file.write("\nutterance : type : " + type(utterance).__name__ + "\n")

            total_sequence_duration += utterance['end_time'] - utterance['start_time']

            overlapping_word_file.write("utterance : idx : " + str(idx + 1) + "\n")
            overlapping_word_file.write("utterance : utterance : " + str(utterance) + "\n")

            overlapping_word_file.write("utterance : " + type(utterance).__name__ + "\n")
            overlapping_word_file.write("utterance : start_time : " + str(utterance["start_time"]) + "\n")
            overlapping_word_file.write("utterance : end_time : " + str(utterance["end_time"]) + "\n")
            overlapping_word_file.write("utterance : word_range : " + utterance["word_range"] + "\n")

            # ES2002a.B.words1358-ES2002a.B.words1383
            word_range = utterance["word_range"]
            # ES2002a.B.words1358
            startWord = word_range.split('-')[0]
            # ES2002a.B.words1383
            endWord = word_range.split('-')[-1]
            # 1358
            startWordId = int(startWord.split('.')[-1].replace('words', ''))
            # 1383
            endWordId = int(endWord.split('.')[-1].replace('words', ''))
            for ov_id in range(startWordId, endWordId + 1):
                all_words.append(ov_id)

            overlapping_word_file.write("utterance : word_range : startWordId : " + str(startWordId) + "\n")
            overlapping_word_file.write("utterance : word_range : endWordId : " + str(endWordId) + "\n")
            transcript = meeting.getTranscript()["transcript"]

            speakers.append(utterance['speaker_id'])
            total_no_of_utterance_length += utterance['end_time'] - utterance['start_time']

            prob_of_neutral_utterances = (len(utterance) - (
                    no_of_unconfident_utterances + no_of_confidence_utterances)) / no_of_utterances if no_of_utterances > 0 else 0
            overlapping_word_file.write("utterance : transcript : len(utterance) : " + str(len(utterance)) + "\n")
            overlapping_word_file.write(
                "utterance : transcript : prob_of_neutral_utterances : " + str(prob_of_neutral_utterances) + "\n")

            confidence_lvl = int(confidence[str(utterance['id'])])
            if confidence_lvl == 1:
                no_of_confidence_utterances += 1
            elif confidence_lvl == -1:
                no_of_unconfident_utterances += 1
            if idx != no_of_utterances - 1:
                total_no_of_time_difference += sorted_sub_sequence[idx + 1]['start_time'] - \
                                               sorted_sub_sequence[idx]['end_time']

            if sequence["type"] == "problem":  # problem #decision #action
                time_utterance_problem.append(utterance['end_time'] - utterance['start_time'])
                utterance_numbers_problem.append(number_problem)
                number_problem = number_problem + 1

            if sequence["type"] == "decision":  # problem #decision #action
                time_utterance_decision.append(utterance['end_time'] - utterance['start_time'])
                utterance_numbers_decision.append(number_decision)
                number_decision = number_decision + 1

            if sequence["type"] == "action":  # problem #decision #action
                time_utterance_action.append(utterance['end_time'] - utterance['start_time'])
                utterance_numbers_action.append(number_action)
                number_action = number_action + 1

            overlapping_word_file.write(
                "utterance : time_utterance : " + str(time_utterance_action) + "\n")
            overlapping_word_file.write(
                "utterance : utterance_numbers : " + str(utterance_numbers_action) + "\n")

            prob_of_confidence_utterances = no_of_confidence_utterances / no_of_utterances if no_of_utterances > 0 else 0
            prob_of_unconfident_utterances = no_of_unconfident_utterances / no_of_utterances if no_of_utterances > 0 else 0
            prob_of_neutral_utterances = 1 - (prob_of_confidence_utterances + prob_of_unconfident_utterances)

        overlapping_time = 0
        all_words.sort()
        # print(all_words)
        for idx_i, i in enumerate(all_words):
            for j in all_words[idx_i + 1:]:
                i_start_time = i_end_time = j_start_time = j_end_time = 0
                for item in transcript:
                    item_id = int(item["id"].split('.')[-1].replace('words', ''))
                    if item_id == i:
                        i_start_time = transcript[i]["start_time"]
                        i_end_time = transcript[i]["end_time"]
                        # print(i_start_time, i_end_time)
                    if item_id == j:
                        j_start_time = transcript[j]["start_time"]
                        j_end_time = transcript[j]["end_time"]
                # print(i_start_time, i_end_time, j_start_time, j_end_time)

                if j_start_time <= i_start_time <= j_end_time <= i_end_time:
                    overlapping_time += j_end_time - i_start_time
                elif i_start_time >= j_start_time and i_end_time <= j_end_time:
                    overlapping_time += i_end_time - i_start_time
                elif i_start_time <= j_start_time <= i_end_time and i_end_time >= j_end_time:
                    overlapping_time += j_end_time - j_start_time
                elif i_start_time <= j_start_time <= i_end_time <= j_end_time:
                    overlapping_time += i_end_time - j_start_time
                elif i_start_time == j_start_time and i_end_time == j_end_time:
                    overlapping_time += i_end_time - i_start_time

            overlapping_word_file.write("utterance : transcript : overlapping_time : " + str(overlapping_time) + "\n")

        dataset.append({
            'prob_of_confidence_utterances': prob_of_confidence_utterances,
            'prob_of_unconfident_utterances': prob_of_unconfident_utterances,
            'prob_of_neutral_utterances': prob_of_neutral_utterances,
            'no_of_speakers': len(set(speakers)),
            'total_no_of_utterance_length': total_no_of_utterance_length,
            'no_of_utterances': no_of_utterances,
            'total_no_of_time_difference': total_no_of_time_difference,
            'total_sequence_duration': abs(total_sequence_duration),
            "overlapping_time": overlapping_time / total_sequence_duration if total_sequence_duration > 0 else 0,
            # "time_vs_utterance_length": (utterance['end_time'] - utterance['start_time']) / (idx+1),
            'category': sequence['type']
        })

overlapping_word_file.close()
# print(dataset)

import pandas  as pd  # Data manipulation
import numpy as np  # Data manipulation
import matplotlib.pyplot as plt  # Visualization
import seaborn as sns  # Visualization

plt.rcParams['figure.figsize'] = [8, 5]
plt.rcParams['font.size'] = 14
plt.rcParams['font.weight'] = 'bold'
plt.style.use('seaborn-whitegrid')

# pd.set_option('display.max_columns', None)  # or 1000
# pd.set_option('display.max_rows', None)  # or 1000
# pd.set_option('display.max_colwidth', None)  # or 199

df = pd.DataFrame(dataset)
df.to_csv("dataset.csv", mode='a', encoding="utf-8", index=False)
print('\nNumber of rows and columns in the data set: ', df.shape)
print(df.head())
print('')

# plt.xlabel('utterance_numbers')
# plt.ylabel('time_utterance')
# plt.title('utterance_numbers vs time_utterance - problem')
# X_positions = np.array(time_utterance_problem)
# y_positions = np.array(utterance_numbers_problem)
# plt.plot([X_positions], [y_positions], 'ro')
# plt.axis([0, 20, 0, 20])
#
# plt.xlabel('utterance_numbers')
# plt.ylabel('time_utterance')
# plt.title('utterance_numbers vs time_utterance - decision')
# X_positions = np.array(time_utterance_decision)
# y_positions = np.array(utterance_numbers_decision)
# plt.plot([X_positions], [y_positions], 'ro')
# plt.axis([0, 20, 0, 20])
#
# plt.xlabel('utterance_numbers')
# plt.ylabel('time_utterance')
# plt.title('utterance_numbers vs time_utterance - action')
# X_positions = np.array(time_utterance_action)
# y_positions = np.array(utterance_numbers_action)
# plt.plot([X_positions], [y_positions], 'ro')
# plt.axis([0, 20, 0, 20])

# X_means = X_positions.mean()
# y_means = y_positions.mean()
# plt.plot([X_means], [y_means], 'go')
# plt.axis([0, 20, 0, 20])
#
# X_minus_X_means = X_positions - X_means
# y_minus_y_means = y_positions - y_means
# X_minus_X_means_squared = X_minus_X_means ** 2
# X_minus_X_means_times_y_minus_y_means = X_minus_X_means * y_minus_y_means
#
# m = sum(X_minus_X_means_times_y_minus_y_means) / sum(X_minus_X_means_squared)
# b = y_means - m * X_means
#
# x = np.linspace(0, 10, 10)  # constructs a numpy array of [0.0, 1.0, ... 10.0]
# plt.plot(x, m * x + b, linestyle='solid')
# plt.show()  # or use plt.savefig("filename.png")

# f, ax = plt.subplots(figsize=(10, 4))
# plt.xlabel('time_vs_utterance_length')
# plt.ylabel('category')
# plt.title('time_vs_utterance_length vs category')
# plt.scatter(y=(utterance['end_time'] - utterance['start_time']), x=(idx + 1), color='red')
# plt.show()

# f, ax = plt.subplots(figsize=(10, 4))
# plt.xlabel('prob_of_confidence_utterances')
# plt.ylabel('category')
# plt.title('prob_of_confidence_utterances vs category')
# plt.scatter(y=df['category'], x=df['prob_of_confidence_utterances'], color='red')
# # plt.show()
#
# f, ax = plt.subplots(figsize=(10, 4))
# plt.xlabel('prob_of_unconfident_utterances')
# plt.ylabel('category')
# plt.title('prob_of_unconfident_utterances vs category')
# plt.scatter(y=df['category'], x=df['prob_of_unconfident_utterances'], color='red')
# # plt.show()
#
# f, ax = plt.subplots(figsize=(10, 4))
# plt.xlabel('no_of_speakers')
# plt.ylabel('category')
# plt.title('no_of_speakers vs category')
# plt.scatter(y=df['category'], x=df['no_of_speakers'], color='red')
# # plt.show()
#
# f, ax = plt.subplots(figsize=(10, 4))
# plt.xlabel('total_no_of_utterance_length')
# plt.ylabel('category')
# plt.title('total_no_of_utterance_length vs category')
# plt.scatter(y=df['category'], x=df['total_no_of_utterance_length'], color='red')
# # plt.show()
#
# f, ax = plt.subplots(figsize=(10, 4))
# plt.xlabel('no_of_utterances')
# plt.ylabel('category')
# plt.title('no_of_utterances vs category')
# plt.scatter(y=df['category'], x=df['no_of_utterances'], color='red')
# # plt.show()
#
f, ax = plt.subplots(figsize=(10, 4))
plt.xlabel('total_no_of_time_difference')
plt.ylabel('category')
plt.title('total_no_of_time_difference vs category')
plt.scatter(y=df['category'], x=df['total_no_of_time_difference'], color='red')
plt.show()
#
# f, ax = plt.subplots(figsize=(10, 4))
# plt.xlabel('total_sequence_duration')
# plt.ylabel('category')
# plt.title('total_sequence_duration vs category')
# plt.scatter(y=df['category'], x=df['total_sequence_duration'], color='red')
# # plt.show()
#
# f, ax = plt.subplots(figsize=(10, 4))
# plt.xlabel('overlapping_time')
# plt.ylabel('category')
# plt.title('overlapping_time vs category')
# plt.scatter(y=df['category'], x=df['overlapping_time'], color='red')
# # plt.show()

# f, ax = plt.subplots(figsize=(10, 4))
# plt.xlabel('prob_of_neutral_utterances')
# plt.ylabel('category')
# plt.title('prob_of_neutral_utterances vs category')
# plt.scatter(y=df['category'], x=df['prob_of_neutral_utterances'], color='red')
# # plt.show()


y_t = np.array(df['category'])
X_t = df
X_t = df.drop(['category'], axis=1)
X_t = np.array(X_t)

print("shape of Y :" + str(y_t.shape))
print("shape of X :" + str(X_t.shape))

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_t = scaler.fit_transform(X_t)

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X_t, y_t, test_size=.20, random_state=42)
print("shape of X Train :" + str(X_train.shape))
print("shape of X Test :" + str(X_test.shape))
print("shape of Y Train :" + str(Y_train.shape))
print("shape of Y Test :" + str(Y_test.shape))

from sklearn.svm import SVC

for this_C in [1, 3, 5, 10, 40, 60, 80, 100]:
    clf = SVC(kernel='linear', C=this_C).fit(X_train, Y_train)
    scoretrain = clf.score(X_train, Y_train)
    scoretest = clf.score(X_test, Y_test)
    print(
        "Linear SVM value of C:{}, training score :{:2f} , Test Score: {:2f} \n".format(this_C, scoretrain, scoretest))

from sklearn.model_selection import cross_val_score, StratifiedKFold, LeaveOneOut

clf1 = SVC(kernel='linear', C=20).fit(X_train, Y_train)
scores = cross_val_score(clf1, X_train, Y_train, cv=3)
start_scores = cross_val_score(clf1, X_train, Y_train, cv=StratifiedKFold(3, random_state=10, shuffle=True))
# Loo = LeaveOneOut()
# Loo_scores = cross_val_score(clf1,X_train,Y_train,cv=Loo)
print("The Cross Validation Score :" + str(scores))
print("The Average Cross Validation Score :" + str(scores.mean()))
# print("The Stratified Cross Validation Score :" + str(start_scores))
# print("The Average Stratified Cross Validation Score :" + str(start_scores.mean()))
# print("The LeaveOneOut Cross Validation Score :"+str(Loo_scores))
# print("The Average LeaveOneOut Cross Validation Score :"+str(Loo_scores.mean()))
