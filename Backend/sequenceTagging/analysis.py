import pandas  as pd  # Data manipulation
import numpy as np  # Data manipulation
import matplotlib.pyplot as plt  # Visualization
# import seaborn as sns  # Visualization

# df = pd.DataFrame(dataset)
df = pd.read_csv('dataset.csv')

print('\nNumber of rows and columns in the data set: ', df.shape)
print(df.head())
print('')
plt.rcParams['figure.figsize'] = [8, 5]
plt.rcParams['font.size'] = 14
plt.rcParams['font.weight'] = 'bold'
plt.style.use('seaborn-whitegrid')

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

f, ax = plt.subplots(figsize=(10, 4))
plt.xlabel('prob_of_confidence_utterances')
plt.ylabel('category')
plt.title('prob_of_confidence_utterances vs category')
plt.scatter(y=df['category'], x=df['prob_of_confidence_utterances'], color='red')
# plt.show()

f, ax = plt.subplots(figsize=(10, 4))
plt.xlabel('prob_of_unconfident_utterances')
plt.ylabel('category')
plt.title('prob_of_unconfident_utterances vs category')
plt.scatter(y=df['category'], x=df['prob_of_unconfident_utterances'], color='red')
# plt.show()

f, ax = plt.subplots(figsize=(10, 4))
plt.xlabel('no_of_speakers')
plt.ylabel('category')
plt.title('no_of_speakers vs category')
plt.scatter(y=df['category'], x=df['no_of_speakers'], color='red')
# plt.show()

f, ax = plt.subplots(figsize=(10, 4))
plt.xlabel('total_no_of_utterance_length')
plt.ylabel('category')
plt.title('total_no_of_utterance_length vs category')
plt.scatter(y=df['category'], x=df['total_no_of_utterance_length'], color='red')
# plt.show()

f, ax = plt.subplots(figsize=(10, 4))
plt.xlabel('no_of_utterances')
plt.ylabel('category')
plt.title('no_of_utterances vs category')
plt.scatter(y=df['category'], x=df['no_of_utterances'], color='red')
# plt.show()

f, ax = plt.subplots(figsize=(10, 4))
plt.xlabel('total_no_of_time_difference')
plt.ylabel('category')
plt.title('total_no_of_time_difference vs category')
plt.scatter(y=df['category'], x=df['total_no_of_time_difference'], color='red')
# plt.show()

f, ax = plt.subplots(figsize=(10, 4))
plt.xlabel('total_sequence_duration')
plt.ylabel('category')
plt.title('total_sequence_duration vs category')
plt.scatter(y=df['category'], x=df['total_sequence_duration'], color='red')
# plt.show()

f, ax = plt.subplots(figsize=(10, 4))
plt.xlabel('overlapping_time')
plt.ylabel('category')
plt.title('overlapping_time vs category')
plt.scatter(y=df['category'], x=df['overlapping_time'], color='red')
# plt.show()

f, ax = plt.subplots(figsize=(10, 4))
plt.xlabel('prob_of_neutral_utterances')
plt.ylabel('category')
plt.title('prob_of_neutral_utterances vs category')
plt.scatter(y=df['category'], x=df['prob_of_neutral_utterances'], color='red')
plt.show()
