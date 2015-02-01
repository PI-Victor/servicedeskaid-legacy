var mongoose = require("mongoose"),
    mongoUri = "mongodb://127.0.0.1:27017/deskdb";


module.exports = function connectDb() {
    mongoose.connect(mongoUri);
    mongoose.connection;
    mongoose.connection.on("open", function(){
	console.log("Connection successful to mongodb".cyan);
    });
    mongoose.connection.on("error", function(){
	console.log("Connection failed to: %s".red, mongoUri);
    });
}
