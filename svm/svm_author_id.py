#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 


#########################################################
### your code goes here ###
from sklearn import svm
clf = svm.SVC(C=10000.0,  kernel='rbf')
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
t0 = time()

pred = clf.predict(features_test)
print "prediction time:", round(time()-t0, 3), "s"

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print "Acurracy: ", acc   

print "Prediction sample 10: ", pred[10]  
print "Prediction sample 26", pred[26]
print "Prediction sample 50", pred[50]            

counter = 0
for val in pred:
    if val==1:
        counter+=1
        
print "Label 1 predictions: ", counter

        

  
                             
#########################################################


