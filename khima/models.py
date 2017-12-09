from django.db import models
# Create your models here.
class khyams(models.Model):
    admin_id = models.ForeignKey('Accuounts.users',on_delete=models.PROTECT)
    name = models.CharField(max_length=150)
    discription = models.TextField()
    files_id = models.IntegerField()
    slug_name = models.CharField(max_length=15)

class members(models.Model):
    user_id = models.ForeignKey('Accuounts.users',on_delete=models.PROTECT)
    khima = models.ForeignKey('khyams',on_delete=models.PROTECT)

