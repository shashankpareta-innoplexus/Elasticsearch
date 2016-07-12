from pymongo import MongoClient
from elasticsearch import helpers
from bson import json_util
import json
import elasticsearch
import collections

# elasticsearch client
es = elasticsearch.Elasticsearch([{'host': '192.168.0.106', 'port': 9200}])

# connection to mongoDB
connection = MongoClient('192.168.0.58',10080)

# getting collection
db = connection.pubmed.pubmed_data_total_simplified

objectId = []
j= 1
a = db.find()
for j in range(db.count()):
    A = a.next()
    x = str(A['_id'])
    if(j<552301):
        j=j+1
        continue
    if(j>552310):
        print j, 'first break'
        break
    objectId.append(x)
    j=j+1

print objectId

#print 'Fetched object ids'
b = db.find({},{'_id':0})

i=1
k=1
# this contain list of actions i.e. indexing to be performed on all json objects
actions = []
for i in range(db.count()):
# for i in range(db.count()):
    B = b.next()
    if(i<552301):
        i=i+1
        continue
    action = {
        "_index" : "pubmed1",
        "_type" : "pubmed_data_total_simplified",
        "_id" : objectId[k],
        "_source": json.dumps(B, default = json_util.default)
        }
    k=k+1
    if(i>552310):
        print i, 'second break'
        break
    actions.append(action)
    # break
    print i
    i=i+1

if(len(actions)>0):
    helpers.bulk(es, actions, chunk_size=100, request_timeout=50)

# action_bulk = []
# # this adds data to elasticsearch using bulk api
# for k in range(100000):
#     action_bulk.append(actions[k])
#     #print action_bulk
#     k= k+1
#     if(k%25000):
#         if(len(actions)>0):
#             helpers.bulk(es, action_bulk, chunk_size=10)
#         action_bulk = []

# if(len(actions)>0):
#     helpers.parallel_bulk(es, actions, thread_count=4, chunk_size=100, max_chunk_bytes=104857600, raise_on_exception=False)
