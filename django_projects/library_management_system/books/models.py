from django.db import models
class Books(models.Model):
	name=models.CharField(max_length=100)
	title=models.TextField()
	date=models.DateField()


	def __str__(self):
		return self.name