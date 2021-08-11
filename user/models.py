from django.db import models
import datetime

class quickPollUser(models.Model):
	username = models.CharField(max_length=20, unique=True)
	dateJoined = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.username + "__#" + str(self.id)

	class Meta:
		verbose_name_plural = 'username'