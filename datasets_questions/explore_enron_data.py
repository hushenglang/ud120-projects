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

print 'total number: ', len(enron_data)
print enron_data['SKILLING JEFFREY K']
print enron_data['LAY KENNETH L']['total_payments']
print enron_data['SKILLING JEFFREY K']['total_payments']
print enron_data['FASTOW ANDREW S']['total_payments']

print 'totla number:', len(enron_data.items())

poiPersons = [v for k, v in enron_data.items() if v['poi']==True]


print 'result:', len(poiPersons)
print 'result:', len(poiPersons)/float(len(enron_data.items()))
print  map(lambda x:x['total_stock_value'], poiPersons)

###############################################
array = []
with open('../final_project/poi_names.txt') as fo:
    array = fo.read().splitlines()

filteredArray = [s for s in array if (s.find('(y)')!=-1) or (s.find('(n)')!=-1)]

print len(filteredArray)
print filteredArray
