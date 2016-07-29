#AUTHOR: Shashank Pareta

from elasticsearch import Elasticsearch
from pymongo import MongoClient
import json
from bson import json_util
from elasticsearch import helpers

client = MongoClient('localhost',27017)

#db = client.oilbird
db = client.publications_filter

es = Elasticsearch(['192.168.0.64:9200'])


all_data = db.filters.find({},{"authors":1,"target_tag":1,"tag_v1":1,"intervention_tag":1,"intervention_search_tag":1,"article_title":1,"journal_title":1,"created_at":1,"impact_factor":1,"oncology_subindication":1}).batch_size(1000)
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

        # normalize last_name to name in authors
        if 'authors' in doc_sanitized.keys():
            i=0
            for y in doc_sanitized['authors']:
                # print x['catagory']
                if 'author_name' in y.keys():
                    doc_sanitized['authors'][i]['name'] = y['author_name']
                    del doc_sanitized['authors'][i]['author_name']
                i=i+1

        if 'authors' in doc_sanitized.keys():
            i=0
            for y in doc_sanitized['authors']:
                # print x['catagory']
                if 'country' in y.keys():
                    doc_sanitized['authors'][i]['master_country'] = y['country']
                    del doc_sanitized['authors'][i]['country']
                i=i+1

        action = {
            "_index" : "kols_publications_new",
            "_type" : "publications_new",
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
    helpers.bulk(es, actions, chunk_size=50, request_timeout=50)
