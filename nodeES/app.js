var express = require('express');
var timeout = require('connect-timeout');
var bodyParser = require('body-parser');

var demo = require('./routes/controller.js');

// CORS middleware
var allowCrossDomain = function(req, res, next) {
  res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE');
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Content-Type, x-access-token');

  next();
}

var haltOnTimedout = function(req, res, next) {
  if (!req.timedout){
    next();
  }
}

var app = express();

app.use(timeout('100s'));
app.use(haltOnTimedout);
app.use(allowCrossDomain);
app.use(haltOnTimedout);
app.use(bodyParser.json());
app.use(haltOnTimedout);
app.use(bodyParser.urlencoded({
  extended: true
}));
app.use(haltOnTimedout);
app.use('/myapp', demo);
app.use(haltOnTimedout);

// app.use(function(err, req, res, next){
//   err.status = 400
// })

module.exports = app;
