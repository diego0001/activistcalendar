from django.db import models

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

class User (models.Model):
    email = models.EmailField(max_length=2048)
    nickname = models.CharField(max_length=2048)
    password = models.CharField(max_length=2048)
    prefix = models.CharField (max_length=2048)
    first_name = models.CharField (max_length=2048)
    middle_name = models.CharField (max_length=2048)
    last_name = models.CharField (max_length=2048)
    suffix = models.CharField (max_length=2048)
    nick_name = models.CharField (max_length=2048)
    region = models.TextField()
    address = models.TextField()
    time_created = models.DateField(auto_now=True, auto_now_add=True)
    last_updated = models.DateField(auto_now=True, auto_now_add=True)
    profile = models.TextField()
    avatar_picture = models.ForeignKey(AvatarPicture)

class UserInterest (models.Model):
    user = models.ForeignKey(User)
    interest = models.ForeignKey(Interest)

class UserMedia (models.Model):
    user = models.ForeignKey(User)
    media = models.ForeignKey(MediumLink)

class UserPhotos (models.Model):
    user = models.ForeignKey(User)
    photos = models.ForeignKey(PhotoLink)

class Group (models.Model):
    group_name = models.CharField (max_length=2048)
    group_type = models.CharField (max_length=2048)
    group_creator = models.ForeignKey(User, related_name = 'group_creator')
    group_location = models.TextField()
    group_region = models.TextField()
    group_address = models.TextField()
    group_site = models.URLField()
    group_phone = models.CharField(max_length=2048)
    group_email = models.EmailField()
    group_mission_statement = models.TextField()
    group_description = models.TextField()

class VolunteersGroup(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)

class AdministratorGroup(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)

class UserGroup (models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)

class EventType(models.Model):
    type_name = models.CharField (max_length=2048)

class Event (models.Model):
    event_name = models.CharField (max_length=2048)
    event_type = models.CharField (max_length=2048)
    event_creator = models.ForeignKey(User, related_name="event_creator_user")
    event_host = models.ForeignKey(User, related_name="event_host_user")
    event_type = models.ForeignKey(EventType)
    event_time = models.TimeField()
    event_date = models.DateField()
    event_summary = models.TextField()
    location = models.TextField()
    region = models.TextField()
    address = models.TextField()
    description = models.TextField()
    photos = models.ForeignKey(PhotoLink)
    contact_info = models.TextField()
    contact_person = models.ForeignKey(User)
    volunteers = models.TextField()

class GroupEvent(models.Model):
    group = models.ForeignKey(Group)
    event = models.ForeignKey(Event)

class GuestList (models.Model):
    user_info = models.ForeignKey(User)
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

    
class Promotion(models.Model):
    title = models.CharField(max_length=2048)
    summary = models.TextField()
    profile = models.URLField()

class PromotionMedia(models.Model):
    promotion = models.ForeignKey(Promotion)
    media = models.ForeignKey(MediumLink)

class PromotionPhotos(models.Model):
    promotion = models.ForeignKey(Promotion)
    photos = models.ForeignKey(PhotoLink)

class UserPromotion(models.Model):
    user = models.ForeignKey(User)
    promotion = models.ForeignKey(Promotion)

class GroupPromotion(models.Model):
    group = models.ForeignKey(Group)
    promotion = models.ForeignKey(Promotion)
