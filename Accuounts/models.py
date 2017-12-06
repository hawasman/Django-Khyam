from django.db import models

# Create your models here.
class users(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=15)
    email = models.TextField()
    password = models.TextField()
    def __str__(self):
        return self.full_name