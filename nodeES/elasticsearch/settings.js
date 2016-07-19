var express = require('express');
var router = express.Router();
var elasticsearch = require('elasticsearch');

var exports = module.exports = {};

exports.client = elasticsearch.Client({
      host: 'localhost:9200'
    });
