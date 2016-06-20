from pymongo import MongoClient
import json
from elasticsearch import helpers
import elasticsearch
import collections


es = elasticsearch.Elasticsearch()
connection = MongoClient('localhost',27017)
db = connection.autocompleteassign.sample_patents

# def convert(data):
#     if isinstance(data, basestring):
#         return str(data)
#     elif isinstance(data, collections.Mapping):
#         return dict(map(convert, data.iteritems()))
#     elif isinstance(data, collections.Iterable):
#         return type(data)(map(convert, data))
#     else:
#         return data


a = db.find({},{'_id':0})
i=1
actions = []
for i in range(db.count()):
    A = a.next()
    #dummy_json = convert(A)
    # print A
    # break
    action = {
        "_index" : "testbulk4",
        "_type" : "type1",
        "_id" : i,
        "_source": json.dumps(A)
        }
    actions.append(action)
    i=i+1
    print i

if(len(actions)>0):
    helpers.bulk(es, actions, chunk_size=20)
