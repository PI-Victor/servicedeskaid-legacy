from viewpanel.collection import schema as sc
import flask.ext.mongoalchemy as ma

def test_user_insert():
	users_doc = sc.Users()
	
