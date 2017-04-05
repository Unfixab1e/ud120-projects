#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data)



x = 0
for p, o in enron_data.iteritems():	
    if enron_data[p]["poi"]==1 :
        x += 1
print x


print enron_data["PRENTICE JAMES"]
print enron_data["PRENTICE JAMES"]["total_stock_value"]

print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]


print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]



print enron_data["SKILLING JEFFREY K"]["total_payments"]
print enron_data["FASTOW ANDREW S"]["total_payments"]
print enron_data["LAY KENNETH L"]["total_payments"]


email_count = 0
for k in enron_data:
    if enron_data[k]['email_address'] != 'NaN':
        email_count += 1
print email_count

salary_count = 0
for person in enron_data:
    if enron_data[person]['salary'] != 'NaN':
        salary_count += 1
print salary_count


total_payments_count = 0
total_payments_nan=0
for person in enron_data:
    if enron_data[person]['total_payments'] == 'NaN':
        total_payments_nan += 1
    total_payments_count += 1

print total_payments_count
print total_payments_nan
print float(total_payments_nan) / float(total_payments_count)




total_payments_poi = 0
total_payments_poi_nan=0
total_poi = 0
for person in enron_data:
    if enron_data[person]['poi'] == True:
        total_poi+=1
        if enron_data[person]['total_payments'] == 'NaN':
            total_payments_poi_nan += 1
        total_payments_poi += 1
        
total_payments_poi+=10    
total_payments_poi_nan+=10    
print total_poi

print total_payments_poi
print float(total_payments_poi_nan) / float(total_payments_poi)       





        
