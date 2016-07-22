# Author: Shashank Pareta
# Description: This code converts existing format(array) of data structure to key vallue pairs of
# diffrent documents. (for those datasets in which filters are taken from their main database)
# with checking whether that filter already exists in master_filters database (to avoid repetition).

import pymongo
from pymongo import MongoClient
import re


# creating connection with mongodb
client = MongoClient('localhost',27017)
# creating connection with KTL collection
db = client.ct_filter
db1 = client.master_filters

j=0
filters_new = []
filters_existing = []
k=0

b = db1.filters.find()
for k in range(db1.filters.count()):
    B = b.next()
    if 'interventions' in B.keys():
        print B['interventions']
        filters_existing.append(B['interventions'])
    # print k
    k=k+1

#for nested objects
a = db.filters.find()
for j in range(db.filters.count()):
    A = a.next()
    print type(A)
    print A['sponsor']
    #db.new_societies.insert({'societies': A['guidelineName']})
    filters_new.append(A['patent_office'])
    j=j+1

# for simple fields
a = db.filters.find()
for j in range(db.filters.count()):
    A = a.next()
    print A['oncology_indication']
    # db.new_societies.insert({'societies': A['guidelineName']})
    filters_new.append(A['oncology_indication'])
    j=j+1

# for field : ["string1", "string2"] format in a document
a = db.filters.find()
for j in range(db.filters.count()):
    A = a.next()
    if 'intervention_tag' in A.keys():
        for x in A['intervention_tag']:
            print x
            filters_new.append(x)
    j=j+1

# for field : [{"key1":"value", "key2":"value"] format in a document
a = db.filters.find()
for j in range(db.filters.count()):
    A = a.next()
    if 'sponsors' in A.keys():
        for x in A['sponsors']:
            print x['sponsor']
            filters_new.append(x['sponsor'])
    j=j+1

print len(filters_new)
for x in filters_new:
    print x
    # db1.filters.insert({'sponsor': x})


# for matching whether this data already exists in our master_filters or not. If not then add it.
m=0
print len(filters_new)
filters_new = list(set(filters_new))
print len(filters_new)
for x in patents:
    if(x in filters_existing):
        continue
    # print x
    m=m+1
    db1.filters.insert({'interventions': x})

print m
