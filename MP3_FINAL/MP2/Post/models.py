from django.db import models
from django.utils import timezone

class Course(models.Model):
	course_name = models.CharField(max_length=200)
	def __str__(self):
		return self.course_name
		
		
class Item(models.Model):
	item_name = models.CharField(max_length=200)
	item_quantity = models.IntegerField(default=1)
	item_condition = models.IntegerField(default=0)
	item_occupation = models.IntegerField(default=0)
	item_img = models.FileField()
	item_userfk = models.ForeignKey('Profile.User', on_delete = models.CASCADE)
	item_coursefk = models.ForeignKey(Course, on_delete = models.CASCADE)
	def __str__(self):
		return self.item_name

class Tag(models.Model):
	tag_word = models.CharField(max_length=200)
	tag_itemfk = models.ForeignKey(Item, on_delete = models.CASCADE)
	def __str__(self):
		return self.tag_word
# Create your models here.

