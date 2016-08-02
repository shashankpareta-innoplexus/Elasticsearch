#AUTHOR: Shashank Pareta

from elasticsearch import Elasticsearch
from pymongo import MongoClient
import json
from bson import json_util
from elasticsearch import helpers

client = MongoClient('localhost',27017)

#db = client.oilbird
db = client.regbodies_filter

es = Elasticsearch(['192.168.0.64:9200'])


# check fields in clinical trials
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
        # print type(doc_sanitized['oncology_sub_indication'])
        # print doc_sanitized['oncology_sub_indication'][0]

        if 'authorName' in doc_sanitized.keys():
            doc_sanitized['name'] = doc_sanitized['authorName']
            del doc_sanitized['authorName']

        action = {
            "_index" : "kols_regbodies_new",
            "_type" : "regbodies_new",
            "_id" : objectId,
            "_source": doc_sanitized
            }
        actions.append(action)

        # print doc_sanitized
        # break
        # ret_val = es.index(index="kols_congresses_new",doc_type="congresses_new",ignore=400,body=doc_sanitized,request_timeout=60)
        # if ret_val['created'] != True:
        #             print ret_val['created']
        # print ret_val
    except Exception, e:
        print "error...",e
        break
        # print x['_id']
        # print ret_val

if(len(actions)>0):
    helpers.bulk(es, actions, chunk_size=50, request_timeout=50)
