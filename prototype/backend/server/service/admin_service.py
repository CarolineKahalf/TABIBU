import uuid
import datetime 
from .. import db
from server.model.admin import Admin

def generate_token(admin):

	try:
		# generate the auth token
		auth_token = admin.encode_auth_token()

		response_object = {
			"status": "success",
			"message": "Successfully registered.",
			"Authorization": auth_token
		}

		return response_object, 201
	
	except Exception as e:
		response_object = {
			"status": "fail",
			"message": "Some error occurred. Please try again."
		}

		return response_object, 401

# this function should only be accessed by a logged in admin
def create_admin(data):
	admin = Admin.query.filter_by(email=data['email']).first()

	if not admin:
		new_admin = Admin(
			public_id=str(uuid.uuid4()),
			email=data['email'],
			first_name=data['first_name'],
			last_name=data['last_name'],
			password=data['password'],
			date_registered=datetime.datetime.utcnow()
			)

		save_changes(new_admin)
		return generate_token(new_admin)
	else:

		response_object = {
			'status': 'fail',
			'message': 'user already exists. Please Log in.'
		}

		return response_object, 409

def get_a_admin(public_id):
	return Admin.query.filter_by(public_id=public_id).first()

# only an admin or super admin can view all admins
def get_all_admins():
	return Admin.query.all()

def create_admin(data):
	admin = Admin.query.filter_by(email=data['email']).first()

	if not admin:
		new_admin = admin(
			public_id=str(uuid.uuid4()),
			email=data['email'],
			first_name=data['first_name'],
			last_name=data['last_name'],
			password=data['password'],
			date_registered=datetime.datetime.utcnow()
		)
		save_changes(new_admin)
		return generate_token(new_admin)
	else:

		response_object = {
			'status': 'fail',
			'message': 'user already exists. Please Log in.'
		}

		return response_object, 409

def delete_admin(data):
	admin = Admin.query.filter_by(email=data['email']).first_or_404()

	db.session.delete(admin)
	db.session.commit()
	return {
		'status': 'success',
		'message': 'admin successfully deleted'
	}, 200
	
def delete_admin_by_id(id):
	admin = Admin.query.filter_by(public_id=id).first_or_404()

	db.session.delete(admin)
	db.session.commit()
	return {
		'status': 'success',
		'message': 'admin successfully deleted'
	}, 200

def update_admin(data):
	admin = Admin.query.filter_by(public_id=data['id']).first_or_404()
	admin.email=data['email']
	admin.first_name = data['first_name']
	admin.last_name = data['last_name']
	
	db.session.update(admin)
	db.session.commit()
	return {
		'status': 'success',
		'message': 'admin successfully updated'
	}, 200

def save_changes(data):
	db.session.add(data)
	db.session.commit()


