from django.db import models
import uuid

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length = 150)
    Email = models.CharField(max_length= 200)
    Message = models.TextField(null = False, blank = False)
    created = models.DateTimeField(auto_now_add = True)
    UUID    = models.UUIDField(default = uuid.uuid4,
                               unique = True,
                               primary_key = True,
                               editable = False
                               )
    def __str__(self):
        return self.Name

class Resume_Experience(models.Model):
    Work        = models.CharField(max_length = 250)
    Company     = models.CharField(max_length= 200)
    Date        = models.CharField(max_length= 200)
    Description = models.TextField(null = False, blank = False)
    Created     = models.DateTimeField(auto_now_add = True)
    UUID        = models.UUIDField(default = uuid.uuid4,
                               unique = True,
                               primary_key = True,
                               editable = False
                               )
    def __str__(self):
        return self.Work

class Resume_Education(models.Model):
    School          = models.CharField(max_length = 250)
    Course          = models.CharField(max_length = 250)
    Date            = models.CharField(max_length = 100)
    Description     = models.TextField()
    Created         = models.DateTimeField(auto_now_add = True)
    UUID    = models.UUIDField(default = uuid.uuid4,
                               unique = True,
                               primary_key = True,
                               editable = False
                               )
    def __str__(self):
        return self.School

class Resume_Course(models.Model):
    School          = models.CharField(max_length = 250)
    course          = models.CharField(max_length = 250)
    progress        = models.CharField(max_length = 3  )
    Date            = models.CharField(max_length = 100)
    Description     = models.TextField()
    created         = models.DateTimeField(auto_now_add = True)
    updated         = models.DateTimeField(auto_now = True)

    UUID    = models.UUIDField(default = uuid.uuid4,
                               unique = True,
                               primary_key = True,
                               editable = False
                               )
    def __str__(self):
        return self.course

class Resume_Skill(models.Model):
    skill          = models.CharField(max_length = 250)
    progress        = models.CharField(max_length = 2)
    created         = models.DateTimeField(auto_now_add = True)
    UUID    = models.UUIDField(default = uuid.uuid4,
                               unique = True,
                               primary_key = True,
                               editable = False
                               )
    def __str__(self):
        return self.skill

class Resume_Achievement(models.Model):
    achievements    = models.CharField(max_length = 250)
    created         = models.DateTimeField(auto_now_add = True)
    UUID            = models.UUIDField(default = uuid.uuid4,
                               unique = True,
                               primary_key = True,
                               editable = False
                               )
    def __str__(self):
        return self.achievements

class Projects_item(models.Model):
    Project = models.CharField(max_length = 250)
    Summary    = models.TextField()
    Image   = models.ImageField(upload_to = 'images/')
    Link = models.CharField(max_length =200)
    UUID    = models.UUIDField(default = uuid.uuid4,
                               unique = True,
                               primary_key = True,
                               editable = False
                               )
    def __str__(self):
        return self.Project
