from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Message(models.Model):
	message = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
	comment = models.CharField(max_length=45)
	message_id = models.ForeignKey(Message)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
