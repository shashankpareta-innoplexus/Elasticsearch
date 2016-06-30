var express = require('express');
var router = express.Router();

var elastic = require('../elasticsearch');


router.get('/suggest/:input', function(res, req, next){
    elastic.getSuggestions(req.params.input)
})
