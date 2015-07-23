var express = require('express'),
	reload = require('reload'),
	api = express();


require('application')(api)
require('routes')(api)

var server = api.listen(process.env.PORT || 3030, process.env.HOST || 'localhost', function(){
	var host = server.address().address;
	var port = server.address().port;
	console.log('Listening on http://%s:%s'.green, host, port);
});

reload(server, api)
