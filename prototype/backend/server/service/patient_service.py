import uuid
import datetime 
from .. import db
from server.model.patient import Patient

def generate_token(patient):

	try:
		# generate the auth token
		auth_token = patient.encode_auth_token()

		response_object = {
			"status": "succes",
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

# this function should only be accessed by a logged in patient
def create_patient(data):
	patient = Patient.query.filter_by(email=data['email']).first()

	if not patient:
		new_patient = Patient(
			public_id=str(uuid.uuid4()),
			email=data['email'],
			first_name=data['first_name'],
			last_name=data['last_name'],
			password=data['password'],
			date_registered=datetime.datetime.utcnow()
			)

		save_changes(new_patient)
		return generate_token(new_patient)
	else:

		response_object = {
			'status': 'fail',
			'message': 'user already exists. Please Log in.'
		}

		return response_object, 409

def get_a_patient(public_id):
	return Patient.query.filter_by(public_id=public_id).first()

# only an patient or super patient can view all patients
def get_all_patients():
	return Patient.query.all()

def create_patient(data):
	patient = Patient.query.filter_by(email=data['email']).first()

	if not patient:
		new_patient = Patient(
			public_id=str(uuid  .uuid4()),
			email=data['email'],
			first_name=data['first_name'],
			last_name=data['last_name'],
			password=data['password'],
			date_registered=datetime.datetime.utcnow()
		)
		save_changes(new_patient)
		return generate_token(new_patient)
	else:

		response_object = {
			'status': 'fail',
			'message': 'user already exists. Please Log in.'
		}

		return response_object, 409

def delete_patient(data):
	patient = Patient.query.filter_by(email=data['email']).first_or_404()

	db.session.delete(patient)
	db.session.commit()
	return {
		'status': 'success',
		'message': 'patient successfully deleted'
	}, 200
	
def delete_patient_by_id(id):
	patient = Patient.query.filter_by(public_id=id).first_or_404()

	db.session.delete(patient)
	db.session.commit()
	return {
		'status': 'success',
		'message': 'patient successfully deleted'
	}, 200

def update_patient(data):
	patient = Patient.query.filter_by(public_id=data['id']).first_or_404()
	patient.email=data['email']
	patient.first_name = data['first_name']
	patient.last_name = data['last_name']
	
	db.session.update(patient)
	db.session.commit()
	return {
		'status': 'success',
		'message': 'patient successfully updated'
	}, 200

def save_changes(data):
	db.session.add(data)
	db.session.commit()