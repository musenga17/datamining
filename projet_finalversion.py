#!/usr/bin/python
import csv
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import StratifiedKFold
from numpy import genfromtxt


Xfile = open('X.csv','r')
Xreader = csv.reader(Xfile,delimiter=',')
Yfile = open('Y.csv','r')
Yreader = csv.reader(Yfile,delimiter=',')

X = genfromtxt('X.csv',delimiter=',')
Y = genfromtxt('Y.csv',dtype=None)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.33, random_state = 1992)

skf = StratifiedKFold(n_splits=4, random_state = 1992, shuffle = True)

accuracy = []
for train_index, test_index in skf.split(X_train, Y_train) :
    X_fold_train = X_train[train_index]
    X_fold_test = X_train[test_index]
    Y_fold_train = Y_train[train_index]
    Y_fold_test = Y_train[test_index]
    accuracy_fold = []
    for mdepth in range(1,5) :
        model = RandomForestClassifier(n_estimators = 500, criterion = "gini", max_features = "sqrt", max_depth = mdepth, n_jobs = 4, verbose = 0)
        model.fit(X_fold_train,Y_fold_train)
        predictions = model.predict(X_fold_test)
        accuracy_fold.append(accuracy_score(Y_fold_test, predictions))
    accuracy.append(accuracy_fold)

average = np.mean(np.array(accuracy),0)

best_mdepth = range(1,5)[np.argmax(average)]

final_model =  RandomForestClassifier(n_estimators = 100, criterion = "gini", max_features = "sqrt", max_depth = best_mdepth, n_jobs = 4, verbose = 0)
final_model.fit(X_train,Y_train)
predictions = final_model.predict(X_test)
print "Score final du model: %2.2f" % accuracy_score(Y_test,predictions)

