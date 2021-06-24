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
from sklearn.neighbors import KNeighborsClassifier

error_rate = []  # iterate many models/different k values find find lowest
for i in range(1, 10):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, Y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != Y_test))

plt.figure(figsize=(10, 5))

plt.plot(range(1, 10), error_rate, color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.title('Error Rate vs K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
plt.show()

knn = KNeighborsClassifier(n_neighbors=8)  # it has minimum
knn.fit(X_train, Y_train)
pred = knn.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(Y_test, pred))
print(classification_report(Y_test, pred))
