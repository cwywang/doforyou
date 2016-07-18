from . import db
class Manager(db.Model):
	__tablename__="manager"
	id=db.Column(db.Integer,primary_key=True)
	account=db.Column(db.String(64),unique=True)
	password=db.Column(db.Integer)
	shcool=db.Column(db.String(64),unique=True)
	def __repr__(self):
		return '<Manager %r>'%self.name
class User(db.Model):
	__tablename__="user"
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(64),unique)
	mb_number=db.Column(db.Integer)
	content=db.Column(db.String(64))
