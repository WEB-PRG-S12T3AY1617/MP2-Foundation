from django.db import models
from django.utils import timezone

class Degree(models.Model):
    degree_id = models.IntegerField()
    degree_name = models.CharField(max_length = 200)
    def __str__(self):
        return self.degree_name
    
class Office(models.Model):
    office_id = models.IntegerField()
    office_name = models.CharField(max_length = 200)
    def __str__(self):
        return self.office_name
    
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length = 200)
    user_username = models.CharField(max_length=200)
    user_password = models.CharField(max_length=200)
    user_degreefk=models.ForeignKey(Degree,on_delete = models.CASCADE)
    user_officefk=models.ForeignKey(Office,on_delete = models.CASCADE)
    user_occupation = {
        (1,'Office'),
        (0,'Degree'),
    }

    def __str__(self):
        return self.user_name