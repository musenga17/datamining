#!/usr/bin/python
import csv
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import StratifiedKFold
from sklearn.tree import export_graphviz
from numpy import genfromtxt
import pydot
from IPython.display import Image
from sklearn.externals.six import StringIO

"""
Xfile = open('X_final.csv','r')
Xreader = csv.reader(Xfile,delimiter=',')
Yfile = open('Y_final.csv','r')
Yreader = csv.reader(Yfile,delimiter=',')
"""

X = genfromtxt('X_final.csv',delimiter=',')
Y = genfromtxt('Y_final.csv',dtype=None)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20, random_state = 1992)

"""
skf = StratifiedKFold(n_splits=4, random_state = 1992, shuffle = True)

accuracy = []
for train_index, test_index in skf.split(X_train, Y_train) :
    X_fold_train = X_train[train_index]
    X_fold_test = X_train[test_index]
    Y_fold_train = Y_train[train_index]
    Y_fold_test = Y_train[test_index]
    accuracy_fold = []
    for mdepth in range(5,15) :
        model = RandomForestClassifier(n_estimators = 100, criterion = "gini", max_features = "sqrt", max_depth = mdepth, n_jobs = 4, verbose = 0)
        model.fit(X_fold_train,Y_fold_train)
        predictions = model.predict(X_fold_test)
        accuracy_fold.append(accuracy_score(Y_fold_test, predictions))
    accuracy.append(accuracy_fold)

average = np.mean(np.array(accuracy),0)

best_mdepth = range(5,15)[np.argmax(average)]
"""
final_model =  RandomForestClassifier(n_estimators = 1000, oob_score = True, n_jobs = 4)
final_model.fit(X_train,Y_train)
predictions = final_model.predict(X_test)
print "Score final du model: %2.2f" % accuracy_score(Y_test,predictions)

tree = final_model.estimators_[0]
dot_data = StringIO() 
export_graphviz(tree,out_file='tree.dot')

"""
import pylab as plt

variables = ['db','mtc','mrt','mc','mcr','nVic','nDef','nNul','nPts']
importance_var = final_model.feature_importances_

expl=(0, 0.15, 0, 0)
plt.pie(importance_var[0:9], labels=variables, autopct='%1.1f%%', shadow=True)
plt.axis('equal')
plt.show()
"""

dernierMatchs = [['Monaco','Montpellier'],
     ['Angers','Toulouse'],
     ['Bordeaux','Nancy'],
     ['Dijon','Lorient'],
     ['Lille','Bastia'],
     ['Lyon','Guingamp'],
     ['Nantes','Rennes'],
     ['Caen','St Etienne'],
     ['Metz','Nice'],
     ['Paris SG','Marseille']]

equipe = []
for d in dernierMatchs :
    equipe.extend(d)

derniereSaison = open('SaisonsStatsFinales/2016:2017_Stats_final.csv','r')
reader = csv.reader(derniereSaison,delimiter=',')
dernierMatchStat = []
for row in reader :
    if int(row[1]) == 10 :
        dernierMatchStat.append(row)

dico = {}
for i in range(0,10) :
    match = dernierMatchs[i]
    stat = dernierMatchStat[i]
    dico[match[0]] = stat[2:11]
    dico[match[1]] = stat[11:20]

while True :
    print equipe
    dom = input("Equipe domicile ?")
    while dom not in equipe :
        dom = input("Equipe domicile ?")
    ext = input("Equipe exterieure ?")
    while ext not in equipe :
        ext = input("Equipe exterieure ?")

    X_match = np.array(dico[dom]+dico[ext])
    X_match.reshape(1,-1)
    res = final_model.predict(X_match)[0]
    if res == 0 :
        print dom+'a gagne le match'
    if res == 1 :
        print ext+'a gagne le match'
    if res == 2 :
        print 'match nul'
