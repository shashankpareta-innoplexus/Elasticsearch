var express = require('express');
var elasticsearch = require('elasticsearch');
var router = express.Router();
var queries = require('../elasticsearch/queries');

router.route('/demo')
  .get(function(req, res){
      res.send('It is working');
  });

router.route('/author_names')
  .get(function(req, res){
    console.log('its here');
    // queries.matchQuery().then(function(response){
    //   console.log(response);
    // });
    // console.log(queries.matchQuery());
    // queries.matchQuery('kols', 'top_all_comb_congresses_data_v5', 'congress_category', 'Oncology');
    queries.matchQuery('kols', 'top_all_comb_congresses_data_v5', 'congress_category', 'Oncology');
    res.send('Hi');
  });

module.exports = router;
