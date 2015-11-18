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

print len(enron_data.keys())

len(enron_data['METTS MARK'].keys())

poiCount=0
salaryCount=0
emailAddressCount=0
totalPaymentsCount=0
poiTotalPaymentsNanCount=0
for item in enron_data.keys():
    if enron_data[item]['poi']==True:
        poiCount+=1
        if enron_data[item]['total_payments']=='NaN':
            poiTotalPaymentsNanCount+=1
    if enron_data[item]['salary']!='NaN':
        salaryCount+=1
    if enron_data[item]['email_address']!='NaN':
        emailAddressCount+=1
    if enron_data[item]['total_payments']!='NaN':
        totalPaymentsCount+=1

print "Persons of interest count: ", poiCount

print ("James Prentice stock value: ", enron_data['PRENTICE JAMES']["total_stock_value"])

print("from Wesley Colwell to poi: ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

print "Jeff Skilling exercised options: ", enron_data['SKILLING JEFFREY K']['exercised_stock_options']

print "Lay total: ", enron_data['LAY KENNETH L']['total_payments']
print "Fastow total: ", enron_data['FASTOW ANDREW S']['total_payments']
print "Skilling total:", enron_data['SKILLING JEFFREY K']['total_payments']

print "salary count: ", salaryCount
print "known email address: ", emailAddressCount
print "total payments count: ", totalPaymentsCount
print "percentage total payments count: ", totalPaymentsCount/float(len(enron_data.keys()))
print "poi with NaN totaly payments count: ", poiTotalPaymentsNanCount
