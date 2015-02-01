var express = require("express"),
    consolidate = require("consolidate"),
    mongoose = require("mongoose"),
    colors = require("colors"),
    swig = require("swig"),
    favicon = require("serve-favicon"),
    compress = require("compression"),
    logger = require("morgan"),
    path = require("path");

module.exports = function(app) {
    rootPath = path.dirname(path.resolve(__dirname)),
    viewsPath = path.join(rootPath, "views"),
    publicPath = path.join(rootPath, "public"),
    faviconPath = path.join(publicPath, "images/favicon.ico"),
    oneDay = 86400000;

    app.use(compress());
    app.use(favicon(faviconPath));
    app.use("static", express.static(publicPath, {maxAge: oneDay}));
    app.use(logger("dev"));
    app.engine("swig", consolidate.swig);
    app.set("view engine", "swig");
    app.set("views", viewsPath);
}
