from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import NullBooleanField
from django.db.models.fields.files import ImageField

class Profile(models.Model):
    user = models.OneToOneField(
        to=User, on_delete=models.CASCADE,
        related_name='profile'
    )
    region = models.CharField(max_length=255,
    choices=(
        ('O','Osh'),
        ('B','Bishkek'),
        ('N','Naryn'),
        ('A','Alai'),
        ('T','Talas'),
        ('J','Jalal-Abad'),
    ))
    
    photo = ImageField(
        upload_to='profile_photo',
        null=True,blank=True
    )

    def __str__(self):
        return self.user.username




# Create your models here.
