#AUTHOR: Shashank Pareta

from elasticsearch import Elasticsearch
from pymongo import MongoClient
import json
from bson import json_util
from elasticsearch import helpers

client = MongoClient('localhost',27017)

db = client.authors_data

es = Elasticsearch(['192.168.0.64:9200'])


all_data = db.sample_data.find().batch_size(1000)
count = 0
actions = []

for x in all_data:
    count += 1
    print count
    objectId = str(x['_id'])
    del x['_id']
    try:
        if count < 1462281:
            continue

        doc_sanitized = json.loads(json_util.dumps(x))
        print doc_sanitized['name']

        action = {
            "_index" : "kols_onco_author_list",
            "_type" : "onco_author_list",
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
    helpers.bulk(es, actions, chunk_size=100, request_timeout=50)
