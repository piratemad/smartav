from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score,accuracy_score,confusion_matrix
import pandas as pd

Dataset = pd.read_csv('dataset.csv')
y = Dataset['clean']
X = Dataset.drop(df.columns['clean'],axis = 1)



clf = RandomForestClassifier(n_estimators = 100)
clf.fit(X_train,Y_train)
y_pred = clf.predict(X_test)



print accuracy_score(Y_test,y_pred,normalize = True)
print roc_auc_score(Y_test,y_pred)
tn, fp, fn, tp = confusion_matrix(Y_test,y_pred).ravel()

print "True Positive = ",tp
print "False Positive = ",fp
print "True Negative = ",tn
print "False Negative= ",fn
