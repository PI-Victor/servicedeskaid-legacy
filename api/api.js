var express = require("express"),
    reload = require("reload"),
    app = express();


//create only the basic layout for a simple rest api


//temporary local handlers

app.get('/', function(req, res){
    res.send({id: 1});
});


console.log('Listening on port 3000');
app.listen(3000);
