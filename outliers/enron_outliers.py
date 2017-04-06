#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from pandas import DataFrame
from operator import itemgetter, attrgetter

### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]



data_dict.pop("TOTAL",0)

data = featureFormat(data_dict, features)



for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

maximum = 0
index = 0

for i in range(len(data)):
    if data[i][0] > maximum:
        maximum = data[i][0]
        index = i
        


#print data_dict


#Check who is the big outlier
data=DataFrame(data_dict)


#data.sort_values(['salary'], ascending=[False])



print "Maximum Salary: ", maximum
print "Maximum index: ", index
print "the person with highest salary: ", data.ix['salary'].idxmax(axis=1)
print "the person with highest bonus: ", data.ix['bonus'].idxmax(axis=1)
print data_dict["SKILLING JEFFREY K"]["salary"] , ",", data_dict["SKILLING JEFFREY K"]["bonus"]
print data_dict["LAVORATO JOHN J"]["salary"] , ",", data_dict["LAVORATO JOHN J"]["bonus"]



