var elasticsearch = require('elasticsearch');

var elasticClient = new elasticsearch.Client({
    host: "localhost:9200"
});

var indexName = "NodeES";

function deleteIndex(){
  return elasticClient.indices.delete({
      index: indexName
  })
}
exports.deleteIndex = deleteIndex;

function createIndex(){
  return elasticClient.indices.create({
      index: indexName
  })
}
exports.createIndex = createIndex;

function indexExists(){
  return elasticClient.indices.exists({
      index: indexName
  })
}
exports.indexExists = indexExists;

indexExists.then(function(exists){
    if(exists){
      return deleteIndex;
    }
}).then(createIndex);


var mapping = {
     "sample_data": {
     "date_detection": "False",
     "dynamic_templates": [{
             "string_fields": {
                 "mapping": {
                     "fields": {
                         "raw": {
                             "ignore_above": 256,
                             "index": "not_analyzed",
                             "type": "string"
                         }
                     },
                     "type": "string"
                 },
                 "match": "*",
                 "match_mapping_type": "string"
             }
         }]
     }
 }

function initMapping(){
  return elasticClient.indices.putMapping(mapping)
}
exports.initMapping = initMapping;


function addDocuments(document){
    return elasticClient.index({
        index: "NodeES",
        type: "sample_data",
        body: {
            title: document.title,
            content: document.content,
            suggest: {
                input: document.title.split(" "),
                output: document.title,
                payload: document.metadata || {}
            }
        }
    });
}
exports.addDocuments = addDocuments;

function getSuggestions(input) {
    return elasticClient.suggest({
        index: "NodeES",
        type: "sample_data",
        body: {
            docsuggest: {
                text: input,
                completion: {
                    field: "suggest",
                    fuzzy: true
                }
            }
        }
    })
}
exports.getSuggestions = getSuggestions;
