<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>
            {% block title %}
            Service Desk Aid
            {% endblock %}
        </title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="shortcut icon" href="/static/favicon.ico"/>
        <!--styles-->
        <link rel="stylesheet" type="text/css" href="/static/css/bootstrap.css"/>
        <link rel="stylesheet" type="text/css" href="/static/css/custom.css"/>
        <link rel="stylesheet" type="text/css" href="/static//css/flipclock.css"/>
    </head>

    <body>
        {% block body %}
        {% endblock %}
	{% block footer %}
	<div class="navbar navbar-default navbar-fixed-bottom">
	  <div class="container-fluid">
            <div class="col-md-5 col-md-offset-5">
              <div class="clock"></div>
            </div>
	  </div>
	</div>
	{% endblock %}
        <!--scripts-->
        <script type="text/javascript" src="/static/js/jquery.js"></script>
        <script type="text/javascript" src="/static/js/bootstrap.js"></script>
        <script type="text/javascript" src="/static/js/flipclock.min.js"></script>
        <script type="text/javascript" src="/static/js/clock.js"></script>
    </body>
</html>
