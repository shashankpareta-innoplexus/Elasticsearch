var app = require('../app.js');
var http = require('http').Server(app);

app.set('port', (process.env.PORT || 3000));

http.listen(app.get('port'), function(){
	console.log('Server listening on port ' +  app.get('port'));
});
