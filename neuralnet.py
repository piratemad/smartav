#neural network test
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score,accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix

dataset = pd.read_csv("malware-dataset.csv")

X = dataset.drop('clean',axis = 1)
y = dataset['clean']

X = np.asarray(X)
y = np.asarray(y)
X = X[:,1:]

state = np.random.randint(100)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state=state)

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

mlp = MLPClassifier(hidden_layer_sizes=(12,12,12,12,12,12))

mlp.fit(X_train,y_train)
predictions = mlp.predict(X_test)

print classification_report(y_test,predictions)
print accuracy_score(y_test,predictions)
good = 0
bad = 0
for i in range(0,len(predictions)):
    if predictions[i] == y_test[i]:
        good += 1
    else:
        bad += 1

print good
print bad