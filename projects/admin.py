from django.contrib import admin

# Register your models here.


from django.db import models
from .models import Contact, Resume_Experience, Resume_Education, Resume_Course, Resume_Skill, Resume_Achievement, Projects_item


# Create your models here.
admin.site.register([Contact, Resume_Experience, Resume_Education, Resume_Course, Resume_Skill, Resume_Achievement, Projects_item
])
