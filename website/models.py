from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.  
 
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    description = models.TextField(default="Add description here.")
    date = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("article_details", kwargs={"pk": self.pk})
    
    
class Writes(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    description = models.TextField(default="Add description here.")
    date = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("article_details", kwargs={"pk": self.pk})
    
    

class Skills(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("skill_details", kwargs={"pk": self.pk})
    

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="Add description here.") 
    url = models.URLField(max_length=300, default=True)
    github = models.URLField(max_length=300, default=True)
    
    def __str__(self):
        return self.title    
    
    def get_absolute_url(self):
        return reverse("Project_details", kwargs={"pk": self.pk})


    
class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email