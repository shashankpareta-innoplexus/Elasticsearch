# Author: Shashank Pareta
# Description: This code prepares a collection of onco_master_data for author profile

import pymongo
from pymongo import MongoClient
# import re


# creating connection with mongodb
client = MongoClient('localhost',27017)

# creating connection with KTL collection
db_filters = client.master_filters
db_city = client.country_city_filters

count=0
a = db_filters.filters.find({"countries" : {"$exists":"true"}}).batch_size(1000)
country_names = []

for x in a:
    count += 1
    print count
    objectId = str(x['_id'])
    del x['_id']
    country_names.append(x['countries'])

doc_count=0
for country_name in country_names:
    doc_count += 1
    print doc_count

    # adding link to master data
    getCities = db_city.filters.find({"country" : country_name})
    for y in getCities:
        if 'city' in y.keys():
            db_filters.filters.update_one({"countries":country_name}, {"$set": {"cities": y['city']}})

    print country_name,' country added'
