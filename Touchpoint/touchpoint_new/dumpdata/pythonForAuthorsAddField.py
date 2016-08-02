# Author: Shashank Pareta
# Description: This code prepares a collection with one field added in author_list

import pymongo
from pymongo import MongoClient
# import re


# creating connection with mongodb
client = MongoClient('localhost',27017)

# creating connection with KTL collection
db_master = client.authors_data
db_merck = client.final_merck

count=0
a = db_merck.data.find().batch_size(1000)
merck_author_names = []

for x in a:
    count += 1
    # print count
    objectId = str(x['_id'])
    del x['_id']
    merck_author_names.append(x['name'])

doc_count=0

for merck_author_name in merck_author_names:
    doc_count += 1
    # print doc_count
    i=0
    # adding company field to master author list data
    getName = db_master.sample_data.find({"name" : merck_author_name})
    for y in getName:
        if y is None:
            i=1
            print y['name']
        # db_master.sample_data.update_one({"name":merck_author_name}, {"$set": {"company": "merck"}})
    if i==1:
        break
    print i
