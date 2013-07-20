from django.db import models
from django import forms
from django.contrib.auth import models as authmodels

class AvatarPicture(models.Model):
    location = models.FileField(upload_to='user_pictures/')

class Medium (models.Model):
    location = models.FileField(upload_to='media/')

class MediumLink (models.Model):
    media_type = models.CharField(max_length=2048)
    media = models.ForeignKey(Medium)

class Photo (models.Model):
    location = models.FileField(upload_to='photos/')

class PhotoLink (models.Model):
    photo_type = models.CharField (max_length=2048)
    photo = models.ForeignKey(Photo)

class Interest(models.Model):
    interest = models.TextField()

class ActivistUser (authmodels.User):
    nickname = models.CharField(max_length=2048, unique=True)
    middle_name = models.CharField (max_length=2048)
    region = models.TextField()
    address = models.TextField()
    time_created = models.DateField(auto_now=True, auto_now_add=True)
    profile = models.TextField()
    avatar_picture = models.ForeignKey(AvatarPicture)

class ActivistUserInterest (models.Model):
    user = models.ForeignKey(ActivistUser)
    interest = models.ForeignKey(Interest)

class ActivistUserMedia (models.Model):
    user = models.ForeignKey(ActivistUser)
    media = models.ForeignKey(MediumLink)

class ActivistUserPhotos (models.Model):
    user = models.ForeignKey(ActivistUser)
    photos = models.ForeignKey(PhotoLink)

class Group (models.Model):
    group_name = models.CharField (max_length=2048, unique=True)
    group_type = models.CharField (max_length=2048)
    group_creator = models.ForeignKey(ActivistUser, 
                                      related_name = 'group_creator', unique=True)
    group_location = models.TextField()
    group_region = models.TextField()
    group_address = models.TextField()
    group_site = models.URLField()
    group_phone = models.CharField(max_length=2048)
    group_email = models.EmailField()
    group_mission_statement = models.TextField()

class VolunteersGroup(models.Model):
    user = models.ForeignKey(ActivistUser)
    group = models.ForeignKey(Group)

class AdministratorGroup(models.Model):
    user = models.ForeignKey(ActivistUser)
    group = models.ForeignKey(Group)

class ActivistUserGroup (models.Model):
    user = models.ForeignKey(ActivistUser)
    group = models.ForeignKey(Group)

class EventType(models.Model):
    type_name = models.CharField (max_length=2048)

class Event (models.Model):
    event_name = models.CharField (max_length=2048, unique=True)
    event_type = models.CharField (max_length=2048)
    event_creator = models.ForeignKey(ActivistUser, 
                                      related_name="event_creator_user")
    event_host = models.ForeignKey(ActivistUser, 
                                   related_name="event_host_user")
    event_type = models.ForeignKey(EventType)
    event_time = models.TimeField()
    event_date = models.DateField()
    location = models.TextField()
    event_title = models.CharField(max_length=2048)
    event_purpose = models.TextField()
    description = models.TextField()
    volunteers = models.ForeignKey(ActivistUser, related_name="volunteers")

class GroupEvent(models.Model):
    group = models.ForeignKey(Group)
    event = models.ForeignKey(Event)

class GuestList (models.Model):
    user_info = models.ForeignKey(ActivistUser)
    event = models.ForeignKey(Event)
    rsvp = models.NullBooleanField()

class GroupEvent(models.Model):
    group = models.ForeignKey(Group)
    event = models.ForeignKey(Event)

class GroupMedia(models.Model):
    group = models.ForeignKey(Group)
    media = models.ForeignKey(MediumLink)

class GroupPhotos(models.Model):
    group = models.ForeignKey(Group)
    photo = models.ForeignKey(PhotoLink)

class EventMedia(models.Model):
    event = models.ForeignKey(Event)
    media = models.ForeignKey(MediumLink)

class EventPhotos(models.Model):
    event = models.ForeignKey(Event)
    photo = models.ForeignKey(PhotoLink)
    
