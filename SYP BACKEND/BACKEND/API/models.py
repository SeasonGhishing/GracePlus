from django.db import models

# Create your models here.
class Member(models.Model):
    fullName = models.CharField(max_length=50)
    age = models.CharField(max_length=200)
    address = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    group = models.CharField(max_length=20)
    bloodGroup = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title[:20]