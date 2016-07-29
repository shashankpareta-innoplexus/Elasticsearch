#AUTHOR: Shashank Pareta

from elasticsearch import Elasticsearch
from pymongo import MongoClient
import json
from bson import json_util
from elasticsearch import helpers

client = MongoClient('localhost',27017)

db = client.master_data_filter

es = Elasticsearch(['192.168.0.64:9200'])


all_data = db.filters.find().batch_size(1000)
count = 0
actions = []

for x in all_data:
    count += 1
    print count
    objectId = str(x['_id'])
    del x['_id']
    try:
        doc_sanitized = json.loads(json_util.dumps(x))

        action = {
            "_index" : "kols_onco_master_new",
            "_type" : "onco_master_new",
            "_id" : objectId,
            "_source": doc_sanitized
            }
        actions.append(action)

    except Exception, e:
        print "error...",e
        break
        # print x['_id']
        # print ret_val

if(len(actions)>0):
    helpers.bulk(es, actions, chunk_size=10, request_timeout=50)
