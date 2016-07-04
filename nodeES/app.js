var express = require('express');
var router = express.Router();

var elastic = require('../elasticsearch');
var documents = require('./routes')

router.get('/suggest/:input', function(res, req, next){
    elastic.getSuggestions(req.params.input)
});

router.post('/', function(req, res, next){
    elastic.addDocuments(req.body).then(function(result){
      res.json(result);
    })
});

module.exports = router;
