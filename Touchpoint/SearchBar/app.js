var elasticsearch = require('elasticsearch');
var express = require('express');
var ejs = require('ejs');
var app = express();

app.set('views', __dirname + '/views');
app.set('view engine', 'html');
app.engine('html', ejs.renderFile);
app.use(express.static(__dirname + '/public'));

app.get('/', function (req, res) {
  var client = new elasticsearch.Client({
    host: 'localhost:9200',
    log: 'trace'
  });
  client.search({
    index: 'oilbird_data',
    type: 'patents',
    body: {
      query: {
        match_all: {}
      }
    }
  }).then(function (resp) {
      var hits = resp.hits.hits;
      //console.log(hits)
      res.render('index',{
        result: hits
      });
  }, function (err) {
      console.trace(err.message);
  });
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});
