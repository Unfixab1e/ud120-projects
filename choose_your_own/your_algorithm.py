#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]

'''
#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################
'''


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary


from sklearn import neighbors
clfKNN = neighbors.KNeighborsClassifier(n_neighbors = 5)
clfKNN.fit(features_train, labels_train)
predKnn = clfKNN.predict(features_test)




from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier

clfRandomForest = RandomForestClassifier(n_estimators=10, criterion='gini', 
                                        max_depth=None, min_samples_split=2, 
                                        min_samples_leaf=1, min_weight_fraction_leaf=0.0, 
                                        max_features='auto', max_leaf_nodes=None, 
                                        min_impurity_split=1e-07, bootstrap=True, 
                                        oob_score=False, n_jobs=1, random_state=None, 
                                        verbose=0, warm_start=False, class_weight=None)


clfRandomForest.fit(features_train, labels_train)
predRandomForest = clfRandomForest.predict(features_test)




clfAdaBoost = AdaBoostClassifier(base_estimator=None, n_estimators=50, learning_rate=1.0, algorithm='SAMME.R', random_state=None)
clfAdaBoost.fit(features_train, labels_train)
predAdaBoost = clfAdaBoost.predict(features_test)




from sklearn.svm import SVC

    
clfSVM = SVC(C=1000.0,  kernel='rbf')
clfSVM.fit(features_train, labels_train)
predSVM_rbf = clfSVM.predict(features_test)

clfSVM = SVC(C=1000.0,  kernel='poly', degree=1)
clfSVM.fit(features_train, labels_train)
predSVM_polyFirst = clfSVM.predict(features_test)
    
    
try:
    prettyPicture(clfKNN, features_test, labels_test)
    prettyPicture(clfRandomForest, features_test, labels_test)
    prettyPicture(clfAdaBoost, features_test, labels_test)

except NameError:
    pass



from sklearn.metrics import accuracy_score
print "KNN-Accuracy: ",accuracy_score(predKnn, labels_test)
print "Random Forest-Accuracy: ",accuracy_score(predRandomForest, labels_test)
print "AdaBoost-Accuracy: ",accuracy_score(predAdaBoost, labels_test)
print "SVM-RBF Kernel: ",accuracy_score(predSVM_rbf, labels_test)
print "SVM-Poly Kernel: ",accuracy_score(predSVM_polyFirst, labels_test)
