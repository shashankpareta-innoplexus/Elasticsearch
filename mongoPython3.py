from pymongo import MongoClient
from elasticsearch import helpers
from bson import json_util
import json
import elasticsearch
import collections

# elasticsearch client
es = elasticsearch.Elasticsearch()

# connection to mongoDB
connection = MongoClient('localhost',27017)

# getting collection
db = connection.congresses.sample_congresses

objectId = []
j=0
a = db.find()
for j in range(db.count()):
    A = a.next()
    x = str(A['_id'])
    objectId.append(x)
    # print A['_id']
    j=j+1

#print 'Fetched object ids'
b = db.find({},{'_id':0})

i=0
# this contain list of actions i.e. indexing to be performed on all json objects
actions = []
for x in objectId:
# for i in range(db.count()):
    B = b.next()
    action = {
        "_index" : "patents_standard",
        "_type" : "sample_patents",
        "_id" : x,
        "_source": json.dumps(B, default = json_util.default)
        }
    actions.append(action)
    #break
    print i
    i=i+1

if(len(actions)>0):
    helpers.bulk(es, actions, chunk_size=50)

# if(len(actions)>0):
#     helpers.parallel_bulk(es, actions, thread_count=4, chunk_size=100, max_chunk_bytes=104857600, raise_on_exception=False)
