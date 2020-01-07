from django.db import models
from django.contrib.auth.models import User

class mysub(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE) #userid
	name=models.CharField(max_length=100)
	place=models.TextField()
	contact=models.TextField()
	

	def __str__(self):
		return self.name


class contact(models.Model):
	name=models.CharField(max_length=100)
	email=models.TextField()
	message=models.TextField()

	def __str__(self):
		return self.name

class Images(models.Model):
	mysub = models.ForeignKey(mysub,on_delete=models.CASCADE)
	image = models.FileField(upload_to = 'media/uploads',null=True)
	
	def __str__(self):
 		return self.image

