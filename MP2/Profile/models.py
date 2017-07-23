from django.db import models
from django.utils import timezone

class Degree(models.Model):
	degree_name = models.CharField(max_length=200)
	def __str__(self):
		return self.degree_name
		
class Office(models.Model):
	office_name = models.CharField(max_length=200)
	def __str__(self):
		return self.office_name
		
class User(models.Model):
	user_name = models.CharField(max_length=200)
	user_username = models.CharField(max_length=200)
	user_password = models.CharField(max_length=200)
	user_degreefk = models.ForeignKey(Degree, on_delete = models.CASCADE, blank=True, null=True)
	user_officefk = models.ForeignKey(Office, on_delete = models.CASCADE, blank=True, null=True)
	user_occupation = models.IntegerField(default=0)
	def __str__(self):
		return self.user_name
	
# Create your models here.
