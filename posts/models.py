from django.db import models


# Create your models here.
class post(models.Model):
	user = models.ForeignKey('Accuounts.users',on_delete=models.PROTECT)
	khima = models.ForeignKey('khima.khyams',on_delete=models.PROTECT)
	title = models.CharField(max_length=80)
	body = models.TextField()
	tag = models.CharField(max_length=15)
	pub_date = models.DateTimeField('date published')
	rate = models.IntegerField()
	def __str__(self):
		return self.title

	
class comment(models.Model):
	post = models.ForeignKey('post',on_delete=models.PROTECT)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.body

class masseges(models.Model):
	sender = models.ForeignKey('Accuounts.users',on_delete=models.PROTECT)
	reciver = models.ForeignKey('Accuounts.users',on_delete=models.PROTECT)
	massege = models.TextField()
	
