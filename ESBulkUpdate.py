from elasticsearch import helpers
import json
import elasticsearch
import collections

# elasticsearch client
es = elasticsearch.Elasticsearch()

actions = []
actions.append({
    '_op_type': 'update',
    '_index': 'hospital_data',
    '_type': 'sample_data',
    '_id': "55bb6cc3385c124d7414640e",
    'doc': {'fellowships': 'Shashank pareta'}
})
actions.append({
    '_op_type': 'update',
    '_index': 'hospital_data',
    '_type': 'sample_data',
    '_id': "55bb6cc8385c124d7414641b",
    'doc': {'clean_name': 'Abhilash bolla'}
})
actions.append({
    '_op_type': 'update',
    '_index': 'hospital_data',
    '_type': 'sample_data',
    '_id': "55bb6cc8385c124d7414641b",
    'doc': {'new_country_intitute': {
                    'hospital_name':'It is working'
                    }
    }
})
actions.append({
    '_op_type': 'delete',
    '_index': 'patents_standard',
    '_type': 'sample_patents',
    '_id': '56b1ab6fbc836c6ef06817b5',
})

# this adds data to elasticsearch using bulk api
if(len(actions)>0):
    helpers.bulk(es, actions)

# if(len(actions)>0):
#     helpers.parallel_bulk(es, actions, thread_count=4, chunk_size=100, max_chunk_bytes=104857600, raise_on_exception=False)
