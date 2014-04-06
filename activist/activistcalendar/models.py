from django.db import models
from django import forms
from django.contrib.auth import models as authmodels
from uuidfield import UUIDField

class Profile(authmodels.User):
    user_id = UUIDField(auto=True)
    user_email = models.EmailField(max_length=2048, unique=True)
    phone_number = models.CharField(max_length=2048)
    website = models.URLField()
    personal_message = models.TextField()
    date_created = models.DateField(auto_now=True, auto_now_add=True)

class Group(models.Model):
    group_id = UUIDField(auto=True)
    name = models.TextField()
    description = models.TextField()
    address_line1 = models.TextField()
    address_line2 = models.TextField(blank=True)
    city = models.TextField()
    province = models.TextField()
    country = models.TextField(default="United States")
    group_url = models.URLField()

class Interest(models.Model):
    interest_id = UUIDField(auto=True)
    interest_name = models.TextField()


class Event(models.Model):
    event_id = UUIDField(auto=True)
    host_group = models.ForeignKey(Group)
    date = models.DateField()
    time = models.TimeField()
    address_line1 = models.TextField()
    address_line2 = models.TextField(blank=True)
    city = models.TextField()
    province = models.TextField()
    country = models.TextField(default="United States")
    contact_email = models.EmailField(max_length=2048)
    event_url = models.URLField()
    description = models.TextField()

class ProfileGroups(models.Model):
    profile = models.ForeignKey(Profile)
    group = models.ForeignKey(Group)

class ProfileInterest(models.Model):
    profile = models.ForeignKey(Profile)
    interest = models.ForeignKey(Interest)

class ProfileEvents(models.Model):
    profile = models.ForeignKey(Profile)
    event = models.ForeignKey(Event)
