from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import bcrypt, re

# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
	def validateReg(self, request):
		errors = self.validate_inputs(request)

		if len(errors) > 0:
			return (False, errors)

		pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

		user = self.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], pw_hash=pw_hash)

		return (True, user)

	def validateLogin(self, request):
		try: 
			user = User.objects.get(email = request.POST['email'])
			password =request.POST['password'].encode()
			if bcrypt.hashpw(password, user.pw_hash.encode()):
				return (True, user)

		except ObjectDoesNotExist:
			pass

		return (False, ['Email not match'])

	def validate_inputs(self, request):
		errors = []
		if len(request.POST['first_name']) < 2 or len(request.POST['last_name']) < 2:
			errors.append("no more than 2 chars")
		if not EMAIL_REGEX.match(request.POST['email']):
			errors.append("include email")
		if len(request.POST['password']) < 8 or request.POST['password'] != request.POST['confirm_pw']:
			errors.append("at least 8 chars")

		return errors

class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.CharField(max_length=45)
	pw_hash = models.CharField(max_length=45)

	objects = UserManager()




















