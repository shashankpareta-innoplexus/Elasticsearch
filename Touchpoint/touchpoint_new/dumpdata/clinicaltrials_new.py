#AUTHOR: Shashank Pareta

from elasticsearch import Elasticsearch
from pymongo import MongoClient
import json
from bson import json_util
from elasticsearch import helpers

client = MongoClient('localhost',27017)

#db = client.oilbird
db = client.ct_filter

es = Elasticsearch(['192.168.0.64:9200'])


# check fields in clinical trials
all_data = db.filters.find({},{"investigators":1,"tag_v1":1,"principal_investigators":1,"phase_v1":1,"sponsors":1,"created_at":1,"clinical_id":1,"public_title":1,"target_tag":1,"intervention_tag":1,"intervention_search_tag":1,"oncology_indication":1}).batch_size(1000)

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

        # normalize investigators to authors
        if 'investigators' in doc_sanitized.keys():
            doc_sanitized['authors'] = doc_sanitized['investigators']
            del doc_sanitized['investigators']

        # normalize last_name to name in authors
        if 'authors' in doc_sanitized.keys():
            i=0
            for y in doc_sanitized['authors']:
                # print x['catagory']
                if 'last_name' in y.keys():
                    doc_sanitized['authors'][i]['name'] = y['last_name']
                    del doc_sanitized['authors'][i]['last_name']
                i=i+1


        # normalize master_country to name in authors
        # if 'authors' in doc_sanitized.keys():
        #     i=0
        #     for y in doc_sanitized['authors']:
        #         # print x['catagory']
        #         if 'country' in y.keys():
        #             del doc_sanitized['authors'][i]['country']
        #
        #         if 'master_country' in y.keys():
        #             doc_sanitized['authors'][i]['country'] = y['master_country']
        #             del doc_sanitized['authors'][i]['master_country']
        #         i=i+1

            # print doc_sanitized['authors']

        action = {
            "_index" : "kols_clinical_trials_new",
            "_type" : "clinical_trials_new",
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
