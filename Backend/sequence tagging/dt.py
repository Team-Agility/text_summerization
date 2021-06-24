import pandas  as pd  # Data manipulation
import numpy as np  # Data manipulation
import matplotlib.pyplot as plt  # Visualization
import seaborn as sns  # Visualization

plt.rcParams['figure.figsize'] = [8, 5]
plt.rcParams['font.size'] = 14
plt.rcParams['font.weight'] = 'bold'
plt.style.use('seaborn-whitegrid')

# df = pd.DataFrame(dataset)
df = pd.read_csv('dataset.csv')

print('\nNumber of rows and columns in the data set: ', df.shape)
print(df.head())
print('')

y_t = np.array(df['category'])
X_t = df
X_t = df.drop(['category'], axis=1)
X_t = np.array(X_t)

print("shape of Y :" + str(y_t.shape))
print("shape of X :" + str(X_t.shape))

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

scaler = MinMaxScaler()
X_t = scaler.fit_transform(X_t)

X_train, X_test, Y_train, Y_test = train_test_split(X_t, y_t, test_size=.20, random_state=42)
print("shape of X Train :" + str(X_train.shape))
print("shape of X Test :" + str(X_test.shape))
print("shape of Y Train :" + str(Y_train.shape))
print("shape of Y Test :" + str(Y_test.shape))

# KNN
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()
# criterion : optional (default=”gini”) 
# splitter : string, optional (default=”best”)
# max_depth : int or None, optional (default=None) 

clf = clf.fit(X_train, Y_train)
pred = clf.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(Y_test, pred))

print(classification_report(Y_test, pred))

# !pip install pydotplus
# !conda install graphvizy

from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
from IPython.display import Image
import pydotplus

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True,
                feature_names=["prob_of_confidence_utterances", "prob_of_unconfident_utterances",
                               "prob_of_neutral_utterances", "no_of_speakers", "total_no_of_utterance_length",
                               "no_of_utterances", "total_no_of_time_difference", "total_sequence_duration",
                               "overlapping_time"], class_names=['0', '1', '2'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('dt.png')
Image(graph.create_png())
