#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here


from sklearn import cross_validation
from time import time

features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)

### it's all yours from here forward!
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()
t0 = time()
print "training"
clf.fit(features_train, labels_train)
print "trained in ", round(time()-t0, 3), "s"
print "predicting"
pred = clf.predict(features_test)
print "predicted: ", pred
print "actual: ", labels_test
print "test set size: ", len(features_test)
from sklearn.metrics import accuracy_score, precision_score, recall_score

print "accuracy score: ", accuracy_score(labels_test, pred)
print "precision score: ", precision_score(labels_test, pred)
print "recall score:", recall_score(labels_test, pred)
