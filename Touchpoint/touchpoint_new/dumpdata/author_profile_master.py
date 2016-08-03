# Author: Shashank Pareta
# Description: This code prepares a collection of onco_master_data for author profile

import pymongo
from pymongo import MongoClient
# import re


# creating connection with mongodb
client = MongoClient('localhost',27017)

# creating connection with KTL collection
db_master = client.master_data_filter

db_social = client.social_media_filter
db_contact = client.contact_info_filter
db_publications = client.publications_filter
db_clinical = client.ct_filter
db_congresses = client.congresses_filter
db_patents = client.patents_filter
db_societies = client.societies_filter
db_regbodies = client.regbodies_filter
db_guidelines = client.guidelines_filter

count=0
a = db_master.filters.find().batch_size(1000)
author_names = []

for x in a:
    count += 1
    print count
    objectId = str(x['_id'])
    del x['_id']
    author_names.append(x['name'])

doc_count=0
i=0
for author_name in author_names:
    doc_count += 1
    print doc_count

    # adding link to master data
    # getLink = db_social.filters.find({"name" : author_name})
    # for y in getLink:
    #     if 'link' in y.keys():
    #         db_master.filters.update_one({"name":author_name}, {"$set": {"link": y['link']}})
    # print 'link done'

    # adding email, phone, address
    # contact_info = db_contact.filters.find({"name" : author_name})
    # for y in contact_info:
    #     if 'email' in y.keys():
    #         db_master.filters.update_one({"name":author_name}, {"$set": {"email": y['email']}})
    #     if 'phone' in y.keys():
    #         db_master.filters.update_one({"name":author_name}, {"$set": {"phone": y['phone']}})
    #     if 'address' in y.keys():
    #         db_master.filters.update_one({"name":author_name}, {"$set": {"address": y['address']}})
    # print 'contact info done'


    # adding created_at, article_title, journal_title
    # publication_info = db_publications.filters.find({"authors.author_name":author_name}).sort("created_at", pymongo.DESCENDING)
    # for y in publication_info:
    #     if 'article_title' in y.keys():
    #         db_master.filters.update_one({"name":author_name}, {"$push": {"article_title": y['article_title']}})
    #     if 'created_at' in y.keys():
    #         db_master.filters.update_one({"name":author_name}, {"$push": {"pub_created_at": y['created_at']}})
    #     if 'journal_title' in y.keys():
    #         db_master.filters.update_one({"name":author_name}, {"$push": {"journal_title": y['journal_title']}})
    # print 'publications info done'
    #
    # # adding created_at, scientific_title, clinical_id
    # clinicaltrials_info = db_clinical.filters.find({"investigators.last_name":author_name}).sort("created_at", pymongo.DESCENDING)
    # for y in clinicaltrials_info:
    #     if 'scientific_title' in y.keys():
    #         db_master.filters.update_one({"name":author_name}, {"$push": {"scientific_title": y['scientific_title']}})
    #     if 'created_at' in y.keys():
    #         db_master.filters.update_one({"name":author_name}, {"$push": {"ct_created_at": y['created_at']}})
    #     if 'clinical_id' in y.keys():
    #         db_master.filters.update_one({"name":author_name}, {"$push": {"clinical_id": y['clinical_id']}})
    # print 'clinical trials info done'
    #
    # # adding created_at, title, congress_name
    # congresses_info = db_congresses.filters.find({"author_scores.name":author_name}).sort("created_at", pymongo.DESCENDING)
    # for y in congresses_info:
    #     if 'title' in y.keys():
    #         db_master.filters.update_one({"name":author_name}, {"$push": {"title": y['title']}})
    #     if 'created_at' in y.keys():
    #         db_master.filters.update_one({"name":author_name}, {"$push": {"cong_created_at": y['created_at']}})
    #     if 'congress_name' in y.keys():
    #         db_master.filters.update_one({"name":author_name}, {"$push": {"congress_name": y['congress_name']}})
    # print 'congresses info done'
    #
    # # adding created_at, patent_id
    # patents_info = db_patents.filters.find({"inventors.name":author_name}).sort("created_at", pymongo.DESCENDING)
    # for y in patents_info:
    #     if 'created_at' in y.keys():
    #         db_master.filters.update_one({"name":author_name}, {"$push": {"pat_created_at": y['created_at']}})
    #     if 'patent_id' in y.keys():
    #         db_master.filters.update_one({"name":author_name}, {"$push": {"patent_id": y['patent_id']}})
    # print 'patents info done'
    #
    # # adding society name
    # society_info = db_societies.filters.find({"authorName":author_name}).sort("created_at", pymongo.DESCENDING)
    # for y in society_info:
    #     if 'guidelineName' in y.keys():
    #         db_master.filters.update_one({"name":author_name}, {"$push": {"society_name": y['guidelineName']}})
    # print 'society info done'
    #
    # # adding body name
    # regulatoryBodies_info = db_regbodies.filters.find({"authorName":author_name}).sort("created_at", pymongo.DESCENDING)
    # for y in regulatoryBodies_info:
    #     if 'body_name' in y.keys():
    #         db_master.filters.update_one({"name":author_name}, {"$push": {"body_name": y['body_name']}})
    # print 'regulatory info done'
    #
    # # adding guidelineName
    # guidelines_info = db_guidelines.filters.find({"authorName":author_name}).sort("created_at", pymongo.DESCENDING)
    # for y in guidelines_info:
    #     if 'guidelineName' in y.keys():
    #         db_master.filters.update_one({"name":author_name}, {"$push": {"guidelineName": y['guidelineName']}})
    # print 'guidelines info done'
