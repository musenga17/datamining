#!/usr/bin/python
import psycopg2
import datetime
import hashlib
import numpy as np

def encode (s) :
    hash_object = hashlib.md5(str.encode(s))
    hex_dig = hash_object.hexdigest()
    return (int (hex_dig, 16))

#recuperer la base
db = psycopg2.connect(database="dataminingdb")
#db = psycopg2.connect(database="christ")
#recuperer le curseur
cursor = db.cursor()
#la requete

reqX = "select ht,at,fthg,ftag,hthg,htag,hs,as_,hst,ast,hf,af,hc,ac,hy,ay,hr,ar from resultats;" 
reqY = "select ftr from resultats;"

DX ,DY = [], []
# executer la requete
cursor.execute(reqX)
# liste de tuples / chaque tuple decrit un match
resultX = cursor.fetchall()
keys = ["ht","at","fthg","ftag","hthg","htag","hs","as","hst","ast","hf","af","hc","ac","hy","ay","hr","ar"]
for i in range(0,len(resultX)) :
    dico = {}
    row = resultX[i]
    for j in range(0,len(keys)) :
        key = keys[j]
        dico[key] = row[j]
    DX.append(dico)

cursor.execute(reqY)

resultY = cursor.fetchall()

for i in range(0,len(resultY)) :
    dico = {}
    dico["ftr"] = resultY[i][0]
    DY.append(dico)

from sklearn.feature_extraction import DictVectorizer 
        
vectorizer = DictVectorizer(sparse=False)

X = vectorizer.fit_transform(DX)
Y = vectorizer.fit_transform(DY)

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import Imputer

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20, random_state = 42)
imp = Imputer(missing_values='NaN',strategy='mean',axis=0)

X_train = imp.fit_transform(X_train)
Y_train = imp.fit_transform(Y_train)
X_test = imp.fit_transform(X_test)
Y_test = imp.fit_transform(Y_test)

model = RandomForestClassifier(n_estimators = 1000, criterion = "gini", max_features = "sqrt")
model.fit(X_train,Y_train)
predictions = model.predict(X_test)
print "Score final du model: %2.2f" % accuracy_score(Y_test,predictions)

dicoX = {'ht' : 'Lille' , 'at' : 'Paris SG' , 'fthg' : 0 , 'ftag' : 1, 'hthg' : 0 , 'htag' : 0 , 'hs' : 10 , 'as' : 17 , 'hst' : 1 , 'ast' : 7 , 'hf' : 21, 'af' : 17 , 'hc' : 2 , 'ac' : 4 , 'hy' : 2 , 'ay' : 1 , 'hr' : 0 , 'ar' : 0}

DXX = []
DXX.append(dicoX)

XX = vectorizer.fit_transform(DXX)
XX = imp.fit_transform(XX)
#DXX = vectorizer.inverse_transform(XX)

#p = model.predict(XX)
#print vectorizer.inverse_transform(p)
#print p 
