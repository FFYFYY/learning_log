from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
	text=models.CharField(max_length=32)
	date_added=models.DateTimeField(auto_now_add=True)
	owner=models.ForeignKey(User)
	def __str__(self):
		return self.text

class Entry(models.Model):
	Topic=models.ForeignKey(Topic)
	text=models.TextField()
	date_added=models.DateTimeField(auto_now_add=True)
	lastchange_date=models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural='entries'

	def __str__(self):
		if len(self.text)>20:
			return self.text[:20]+'......'
		return self.text