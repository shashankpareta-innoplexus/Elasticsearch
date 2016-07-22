# Author: Shashank Pareta
# Description: This code converts existing format(array) of data structure to key vallue pairs of
# diffrent documents. (for old filter_data database)

import pymongo
from pymongo import MongoClient
import re


# creating connection with mongodb
client = MongoClient('localhost',27017)
# creating connection with KTL collection
db = client.filter_data
db1 = client.master_filters

j=0
a = db.filters.find()
for j in range(db.filters.count()):
    A = a.next()
    # check if moas document is at which position in type
    if j==3:
        #print A
        print type(A['moas'])
        for x in A['moas']:
            print x
            # Use this when field in mongo is a list of strings
            # db1.filters.insert({"indication":x['indication']})
            # Use this when field in mongo is a list of dictionaries
            # db1.filters.insert({'moas':x})
        break
    j=j+1
