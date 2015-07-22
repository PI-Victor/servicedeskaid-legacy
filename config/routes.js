var main = require('main');

module.exports = function(api) {
	api.get('/', main.show)
} 

