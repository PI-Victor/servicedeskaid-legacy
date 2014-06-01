from viewpanel.collection.schema import Users
import datetime as dt

def test_user_insert():
	print Users.get_fields()
	
	otherinfo = Users.OtherInfo(email_address='ip545k@intl.att.com',
		password='123123',
		)
	users_doc = Users( userid='vectra', 
		other_info = otherinfo,
		timestamp = dt.datetime.utcnow(),
		)
	result = users_doc.save()
	print result, '=------ result'
	db_user = users_doc.query.filter(
		Users.userid == 'ip545k').first()
	assert db_user.userid == users_doc.userid
	removed = users_doc.remove()
	#assert removed



	
