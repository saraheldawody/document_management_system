from django.contrib.auth.models import AbstractUser
from django.db import models
import os

def get_file_path(instance, filename):
    return os.path.join('documents', str(instance.id), filename)

class User(AbstractUser):
    REQUIRED_FIELDS = ['username','password']
    USERNAME_FIELD = 'email'
    def get_username(self):
        return self.email

User._meta.get_field('email')._unique = True
User._meta.get_field('email')._blank = False


class metadata (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, blank=False)
    string = models.TextField(blank=False)

class document (models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, blank=False)
    doc = models.FileField(upload_to=get_file_path,blank=False)