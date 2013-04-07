from django.template import Context, loader
from django.http import Http404
from activistcalendar.models import User, Group, Event, Promotions, Priv
from activistcalendar.models import UserGroup, UserEvent, EventType

def userprofile(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        groups = [usergroup.objects.group for usergroup in UserGroup(user=user)]
        interests = [userinterest.objects.interest for userinterest in UserInterest(user=user)]
        media = [usermedia.objects.media for usermedia in UserMedia(user=user)]
        photos = [userphotos.objects.photos for userphotos in UserPhotos(user=user)]
    except User.DoesNotExist:
        raise Http404
    return render_to_response('views/personalprofile.html', {'user': user, 'groups': groups, 'interests': interests, 'media': media, 'photos': photos})

def groupprofile(request, group_id):
    try:
        group = Group.objects.get(pk=group_id)
        administrators = [administratorgroup.objects.user for \
                              administratorgroup in AdministratorGroup(group=group)]
        events = [groupevent.objects.event for groupevent in GroupEvent(group=group)]
        media = [groupmedia.objects.media for groupmedia in GroupMedia(group=group)]
        photos = [groupphotos.objects.photos for groupphotos in GroupPhotos(group=group)]
    except Group.DoesNotExist:
        raise Http404
    return render_to_response('views/groupprofile.html', {'group': group, 'administrators': administrators, 
                                                          'events': events, 'media': media, 'photos': photos})

def eventprofile(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
        group_sponsors = [groupevent.objects.group for groupevent in GroupEvent(event=event)]
        guests = [guestlist.objects.user for guestlist in GuestList(event=event)]
        media = [eventmedia.objects.media for eventmedia in EventMedia(event=event)]
        photos = [eventphotos.objects.photos for eventphotos in EventPhotos(event=event)]
    except Event.DoesNotExist:
        raise Http404
    return render_to_response('views/eventprofile.html', {'event': event, 'group_sponsors': group_sponsors,
                                                          'guests': guests, 'media': media, 'photos': photos})

def promotionprofile(request, promotion_id):
    try:
        promotion = Event.objects.get(pk=promotion_id)
        users = [userpromotion.objects.user for userpromotion in UserPromotion(promotion=promotion)]
        groups = [grouppromotion.objects.group for grouppromotion in GroupPromotion(promotion=promotion)]
        media = [promotionmedia.objects.media for promotionmedia in PromotionMedia(promotion=promotion)]
        photos = [promotionphotos.objects.photos for promotionphotos in PromotionPhotos(promotion=promotion)]
    except Promotion.DoesNotExist:
        raise Http404
    return render_to_response('views/promotionprofile.html', {'promotion': promotion, 'users': users, 
                                                              'groups': groups, 'media': media, 'photos': photos})
