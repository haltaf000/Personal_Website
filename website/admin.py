from django.contrib import admin

# Register your models here.
from .models import Contact, Project, Skills, Post

admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(Skills)
admin.site.register(Post)