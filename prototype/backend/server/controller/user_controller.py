from flask import request
from flask_restplus import Resource, Namespace, fields

from ..util.dto import UserDto
from ..service.user_service import create_user, get_all_users, get_a_user, delete_user_by_id, update_user
from ..util.decorator import admin_token_required, token_required

api = UserDto.api 

_user = UserDto.user 

user_ = UserDto.outuser


@api.route('/')
class UserList(Resource):
	@api.doc('list_of_registered_users')
	@api.marshal_list_with(user_, envelope='data')
	def get(self):
		"""List all registered users"""
		return get_all_users()
		

	@api.response(201, 'User successfully created.')
	@api.doc('create new user')
	@api.expect(_user, validate=True)
	def post(self):
		"""Creates a new User"""

		data = request.json
		return create_user(data=data)
	
	@api.response(200, 'User successfully updated.')
	@api.doc('update a user')
	@api.expect(_user, validate=True)
	def update(self, data):
		""" update a user given the id"""

		data = request.json
		return update_user(data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):

	@api.doc('get a user')
	@api.marshal_with(user_)
	def get(self, public_id):
		""" get a user given its identifier """

		user = get_a_user(public_id)
		if not user:
			api.abort(404)

		else:
			return user
	
	@api.doc('delete a user')
	def delete(self, public_id):
		""" delete a user given the id """
		return delete_user_by_id(public_id)

	
	


