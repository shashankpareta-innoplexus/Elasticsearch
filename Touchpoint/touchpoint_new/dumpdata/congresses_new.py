#AUTHOR: Shashank Pareta

from elasticsearch import Elasticsearch
from pymongo import MongoClient
import json
from bson import json_util
from elasticsearch import helpers

client = MongoClient('localhost',27017)

#db = client.oilbird
db = client.congresses_filter

es = Elasticsearch(['192.168.0.64:9200'])


all_data = db.filters.find({},{"congress_category":1,"target_tag":1,"tag_v1":1,"intervention_tag":1,"author_scores":1,"title":1,"congress_catagory":1,"congress_name":1,"created_at":1,"congress_type":1,"intervention_search_tag":1,"symptoms":1,"oncology_indication":1}).batch_size(1000)
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

        # normalize category name in tag_v1
        # if 'tag_v1' in doc_sanitized.keys():
        #     i=0
        #     for y in doc_sanitized['tag_v1']:
        #         # print x['catagory']
        #         if 'catagory' in y.keys():
        #             doc_sanitized['tag_v1'][i]['category'] = y['catagory']
        #             del doc_sanitized['tag_v1'][i]['catagory']
        #             # print doc_sanitized['tag_v1'][i]['category']
        #         i=i+1

        # normalize author_scores to authors
        if 'author_scores' in doc_sanitized.keys():
            doc_sanitized['authors'] = doc_sanitized['author_scores']
            del doc_sanitized['author_scores']

        # normalize country name in authors
        # if 'authors' in doc_sanitized.keys():
        #     i=0
        #     for y in doc_sanitized['authors']:
        #         # print y
        #         # print type(y['master_country'])
        #         if 'master_country' in y.keys():
        #             doc_sanitized['authors'][i]['country'] = y['master_country']
        #             del doc_sanitized['authors'][i]['master_country']
        #             # print y
        #         i=i+1
        # ret_val = es.index(index="kols_congresses_new",doc_type="congresses_new",ignore=400,body=doc_sanitized,request_timeout=60)
        action = {
            "_index" : "kols_congresses_new",
            "_type" : "congresses_new",
            "_id" : objectId,
            "_source": doc_sanitized
            }
        actions.append(action)
        # if ret_val['created'] != True:
        #             print ret_val['created']
#    print ret_val
    except Exception, e:
        print "error...", e
        break
#        print x['_id']
        # print ret_val

if(len(actions)>0):
    helpers.bulk(es, actions, chunk_size=50, request_timeout=50)
