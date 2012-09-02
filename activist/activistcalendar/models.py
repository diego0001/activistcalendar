from django.db import models

class AvatarPicture(models.Model):
    location = models.FileField(upload_to='user_pictures/')


class Priv (models.Model):
    read = models.BooleanField()
    write = models.BooleanField()
    delete = models.BooleanField()
    add_users = models.BooleanField()
    delete_users = models.BooleanField()
    add_admin = models.BooleanField()
    remove_admin = models.BooleanField()


class Photo (models.Model):
    location = models.FileField(upload_to='photos/')

class PhotoLink (models.Model):
    photo_type = models.CharField (max_length=255)
    photo = models.ForeignKey(Photo)

class User (models.Model):
    login = models.CharField (max_length=255)
    password = models.CharField(max_length=255)
    prefix = models.CharField (max_length=255)
    first_name = models.CharField (max_length=255)
    middle_name = models.CharField (max_length=255)
    last_name = models.CharField (max_length=255)
    suffix = models.CharField (max_length=255)
    nick_name = models.CharField (max_length=255)
    time_created = models.DateField(auto_now=True, auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    profile = models.TextField()
    photos = models.ForeignKey(PhotoLink)
    avatar_picture = models.ForeignKey(AvatarPicture)


class Group (models.Model):
    group_name = models.CharField (max_length=255)
    group_type = models.CharField (max_length=255)
    group_creator = models.ForeignKey(User)
    group_location = models.TextField()
    group_site = models.URLField()
    group_phone = models.CharField(max_length=255)
    group_email = models.EmailField()
    group_mission_statement = models.TextField()
    group_description = models.TextField()
    group_volunteers = models.TextField()    

class Event (models.Model):
    event_name = models.CharField (max_length=255)
    event_type = models.CharField (max_length=255)
    event_creator = models.ForeignKey(User, related_name="event_creator_user")
    event_host = models.ForeignKey(User, related_name="event_host_user")
    event_time = models.TimeField()
    event_date = models.DateField()
    group = models.ForeignKey(Group)
    location = models.TextField()
    description = models.TextField()
    photos = models.ForeignKey(PhotoLink)
    contact_info = models.TextField()
    contact_person = models.ForeignKey(User)
    volunteers = models.TextField()

class GuestList (models.Model):
    user_info = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    rsvp = models.NullBooleanField()

    
class UserGroup (models.Model):
    priv_level = models.ForeignKey(Priv)
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)

