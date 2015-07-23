var assert = require('assert'),
	express = require('express'),
	request = require('supertest'),
	app = express();


require('application')(app);
require('routes')(app);

app.listen(process.env.PORT || 3000);

describe('Basic application test', function(){

	it('GET to index should return 200', function(done){
		request(app)
		.get('/')
		.expect(200, done)
	});

});