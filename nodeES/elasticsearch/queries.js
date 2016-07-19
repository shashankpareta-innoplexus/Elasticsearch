var express = require('express');
var router = express.Router();
// var Promise = require('bluebird');
var settings = require('./settings.js');

var exports = module.exports = {};

exports.matchQuery = function(index_name, type_name, field_name, data_match){
  console.log(index_name);
  var query_body = {
    query: {
      match: {
        field_name : data_match
      }
    }
  };
  console.log(query_body);
  settings.client.search({
    index: index_name,
    type: type_name,
    body: query_body

  }).then(function(res){
      var hits = res.hits.hits;
      console.log("total: " + res.hits.total);
      var source = hits[0]._source;
      console.log('Voila, I am getting output !!');
      console.log(source);
    }, function(err){
    console.trace(err.message);
  });
}
