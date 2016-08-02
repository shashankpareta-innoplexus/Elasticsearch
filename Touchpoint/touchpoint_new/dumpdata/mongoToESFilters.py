# Author : Shashank Pareta
# Description : this code dumps data from mongo collection to Elasticsearch


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

es = elasticsearch.Elasticsearch([{'host': '192.168.0.64', 'port': 9200}])

# getting collection from database
db = connection.master_filters.filters

# getting all object Ids of mongo and converting them to string, then storing them in array
objectId = []
j=0
# getting all documents of db in a
a = db.find()
for j in range(db.count()):
    A = a.next()
    x = str(A['_id'])
    objectId.append(x)
    j=j+1

# getting all documents from db in b leaving '_id' field
b = db.find({},{'_id':0})

i=0
# this contain list of actions i.e. indexing to be performed on all documents and then dumping them into ES.
# Index name is 'patents_standard' and type is 'sample_patents'
actions = []
for x in objectId:
# for i in range(db.count()):
    B = b.next()
    action = {
        "_index" : "kols_filters",
        "_type" : "filters",
        "_id" : x,
        "_source": json.dumps(B, default = json_util.default)
        }
    actions.append(action)
    #break
    print i
    i=i+1

# this adds data to elasticsearch using bulk api
if(len(actions)>0):
    helpers.bulk(es, actions, chunk_size=50, request_timeout=50)

# if(len(actions)>0):
#     helpers.parallel_bulk(es, actions, thread_count=4, chunk_size=100, max_chunk_bytes=104857600, raise_on_exception=False)
