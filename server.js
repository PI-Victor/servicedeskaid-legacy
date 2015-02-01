var express = require("express"),
    reload = require("reload"),
    db = require("database"),
    app = express();

//create the db connection
db()

//bootstrap application config
require("application")(app);
//routes
//require("routes")(app);

var server = app.listen(process.env.PORT || 3000, function() {
    var host = server.address().address;
    var port = server.address().port;
    console.log("App accessible on http://%s:%s".green, host, port);
});

//reload app whenever something changes
reload(server, app);
