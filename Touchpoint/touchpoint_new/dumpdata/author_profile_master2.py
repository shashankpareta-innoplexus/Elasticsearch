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
    getLink = db_social.filters.find({"name" : author_name})
    for y in getLink:
        if 'link' in y.keys():
            db_master.filters.update_one({"name":author_name}, {"$set": {"link": y['link']}})
    print 'link done'

    # adding email, phone, address
    email = "na"
    phone = "na"
    address = "na"
    a1 = []
    contact_info = db_contact.filters.find({"name" : author_name})
    for y in contact_info:
        if 'email' in y.keys():
            email = y['email']
        if 'phone' in y.keys():
            phone = y['phone']
        if 'address' in y.keys():
            address = y['address']
        a1.append({"email":email, "phone": phone, "address": address})
    db_master.filters.update_one({"name":author_name}, {"$set": {"contact_info": a1}})
    print 'contact info done'

    # adding created_at, article_title, journal_title
    article_title = "na"
    created_at = "na"
    journal_title = "na"
    a2 = []
    publication_info = db_publications.filters.find({"authors.author_name":author_name}).sort("created_at", pymongo.DESCENDING)
    for y in publication_info:
        if 'article_title' in y.keys():
            article_title = y['article_title']
        if 'created_at' in y.keys():
            created_at = y['created_at']
        if 'journal_title' in y.keys():
            journal_title = y['journal_title']
        a2.append({"article_title":article_title, "journal_title": journal_title, "created_at": created_at})
    db_master.filters.update_one({"name":author_name}, {"$set": {"publications": a2}})
    print 'publications info done'

    # adding created_at, scientific_title, clinical_id
    scientific_title = "na"
    ct_created_at = "na"
    clinical_id = "na"
    a3 = []
    clinicaltrials_info = db_clinical.filters.find({"investigators.last_name":author_name}).sort("created_at", pymongo.DESCENDING)
    for y in clinicaltrials_info:
        if 'scientific_title' in y.keys():
            scientific_title = y['scientific_title']
        if 'created_at' in y.keys():
            ct_created_at = y['created_at']
        if 'clinical_id' in y.keys():
            clinical_id = y['clinical_id']
        a3.append({"scientific_title":scientific_title, "created_at": ct_created_at, "clinical_id": clinical_id})
    db_master.filters.update_one({"name":author_name}, {"$set": {"clinicaltrials": a3}})
    print 'clinical trials info done'

    # # adding created_at, title, congress_name
    title = "na"
    cong_created_at = "na"
    congress_name = "na"
    a4 = []
    congresses_info = db_congresses.filters.find({"author_scores.name":author_name}).sort("created_at", pymongo.DESCENDING)
    for y in congresses_info:
        if 'title' in y.keys():
            title = y['title']
        if 'created_at' in y.keys():
            cong_created_at = y['created_at']
        if 'congress_name' in y.keys():
            congress_name = y['congress_name']
        a4.append({"congress_title":title, "congress_name": congress_name, "created_at": cong_created_at})
    db_master.filters.update_one({"name":author_name}, {"$set": {"congresses": a4}})
    print 'congresses info done'

    # adding created_at, patent_id
    patent_id = "na"
    created_at = "na"
    a5 = []
    patents_info = db_patents.filters.find({"inventors.name":author_name}).sort("created_at", pymongo.DESCENDING)
    for y in patents_info:
        if 'created_at' in y.keys():
            created_at = y['created_at']
        if 'patent_id' in y.keys():
            patent_id = y['patent_id']
        a5.append({"patent_id":patent_id, "created_at": created_at})
    db_master.filters.update_one({"name":author_name}, {"$set": {"patents": a5}})
    print 'patents info done'

    # adding society name
    guidelineName = "na"
    a6 = []
    society_info = db_societies.filters.find({"authorName":author_name}).sort("created_at", pymongo.DESCENDING)
    for y in society_info:
        if 'guidelineName' in y.keys():
            guidelineName = y['guidelineName']
        a6.append({"guidelineName":guidelineName})
    db_master.filters.update_one({"name":author_name}, {"$set": {"societies": a6}})
    print 'society info done'

    # adding body name
    body_name = "na"
    a7 = []
    regulatoryBodies_info = db_regbodies.filters.find({"authorName":author_name}).sort("created_at", pymongo.DESCENDING)
    for y in regulatoryBodies_info:
        if 'body_name' in y.keys():
            body_name = y['body_name']
        a7.append({"body_name":body_name})
    db_master.filters.update_one({"name":author_name}, {"$set": {"regulatorybodies": a7}})
    print 'regulatory info done'

    # adding guidelineName
    guidelineName2 = "na"
    a8 = []
    guidelines_info = db_guidelines.filters.find({"authorName":author_name}).sort("created_at", pymongo.DESCENDING)
    for y in guidelines_info:
        if 'guidelineName' in y.keys():
            guidelineName2 = y['guidelineName']
        a8.append({"guidelineName":guidelineName2})
    db_master.filters.update_one({"name":author_name}, {"$set": {"guidelines": a8}})
    print 'guidelines info done'
