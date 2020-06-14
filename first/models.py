from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password= models.CharField(max_length=200)
    gender=models.CharField(max_length=10)
    coun=models.CharField(max_length=50)
    phone=models.CharField(max_length=13)
    img = models.ImageField(upload_to='media')
    Address = models.CharField(max_length=200)
    def __str__(Self):
       return Self.name

class Active(models.Model):
	email = models.CharField(max_length=200)
	date= models.CharField(max_length=200)
	def __str__(Self):
		return Self.email