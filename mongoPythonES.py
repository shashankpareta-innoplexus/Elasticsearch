from mongoengine import *
from elasticsearch import helpers
import elasticsearch
import json

es = elasticsearch.Elasticsearch()
connect('test')

class DummyData(Document):
    meta = {
        'collection' : 'dummycollection'
    }
    term_guid = StringField()
    term_balance = StringField()
    term_age = StringField()
    term_eyeColor = StringField()
    name = StringField()
    term_gender = StringField()
    company = StringField()
    term_email = StringField()
    term_phone_mob = StringField()
    address = StringField()
    about = StringField()

    def to_dict(self):
        return {
            'term_guid': self.term_guid,
            'term_balance': self.term_balance,
            'term_age': self.term_age,
            'term_eyeColor': self.term_eyeColor,
            'name': self.name,
            'term_gender': self.term_gender,
            'company': self.company,
            'term_email': self.term_email,
            'term_phone_mob': self.term_phone_mob,
            'address': self.address,
            'about': self.about
        }

class DummyDataEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, DummyData):
            return obj.to_dict()
        return json.JSONEncoder.default(self, obj)

# this is for entering data to ES one by one
# i=1
# for dummy in DummyData.objects:
#     dummy_json = json.dumps(dummy, cls=DummyDataEncoder)
#     es.index(index='test', doc_type='dummydata', id=i, body=dummy_json)
#     i=i+1


# this is for entering data to ES using bulk api
i=1
actions = []
for dummy in DummyData.objects:
    dummy_json = json.dumps(dummy, cls=DummyDataEncoder)
    action = {
        "_index" : "testbulk",
        "_type" : "type1",
        "_id" : i,
        "_source": dummy_json
        }
    actions.append(action)
    i=i+1

if(len(actions)>0):
    helpers.bulk(es, actions)
