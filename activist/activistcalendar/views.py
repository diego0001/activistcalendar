from django.template import Context, loader
from django.http import Http404
from django.shortcuts import render_to_response
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from activistcalendar.models import ActivistProfile, ActivistGroup, ActivistInterest, ActivistEvent

def activist_profile(input_profile_id):
    try:
        profile = ActivistProfile.objects.get(user_id=input_profile_id)
    except ActivistProfile.DoesNotExist:
        raise Http404
    return render_to_response('views/profile.html', {'profile': profile})


def activist_profile_groups(input_profile_id):
    try:
        profile = ActivistProfile.objects.get(user_id=input_profile_id)
        groups = profile.groups.all()
    except ActivistProfile.DoesNotExist:
        raise Http404
    return render_to_response('views/profile_groups.html', {'groups': groups})

def activist_profile_events(input_profile_id):
    try:
        profile = ActivistProfile.objects.get(user_id=input_profile_id)
        events = profile.events.all()
    except ActivistProfile.DoesNotExist:
        raise Http404
    return render_to_response('views/profile_events.html', {'events': events})

def activist_profile_interests(input_profile_id):
    try:
        profile = ActivistProfile.objects.get(user_id=input_profile_id)
        interests = profile.interests.all()
    except ActivistProfile.DoesNotExist:
        raise Http404
    return render_to_response('views/profile_interests.html', {'interests': interests})

def activist_group(input_group_id):
    try:
        group = ActivistGroup.objects.get(user_id=input_group_id)
    except ActivistGroup.DoesNotExist:
        raise Http404
    return render_to_response('views/group.html', {'group': group})

def activist_group_events(input_group_id):
    try:
        group = ActivistGroup.objects.get(user_id=input_group_id)
        events = group.event_set.all()
    except ActivistGroup.DoesNotExist:
        raise Http404
    return render_to_response('views/events.html', {'events': events})

def create_activist_event(input_group_id, inputdate, inputtime, inputaddress1, inputaddress2,
                          inputcity, inputprovince, inputcountry, inputcontact_email, inputevent_url,
                          inputdescription):
    try:
        group = ActivistGroup.objects.get(user_id=input_group_id)
        event = ActivistEvent(host_group=group, date=inputdate, time=inputtime, 
                              address_line1=inputaddress1, address_line2=inputaddress2,
                              city=inputcity, province=inputprovince, country=inputcountry,
                              contact_email=inputcontact_email, event_url=inputevent_url, 
                              description=inputdescription)
        event.save()
        return render_to_response('views/events.html', {'events': [event]})
    except ValidationError as e:
        non_field_errors = e.message_dict[NON_FIELD_ERRORS]
        return render_to_response('views/events.html', {'events': None})

def delete_activist_event(input_event_id):
    try:
        event = ActivistEvent.objects.get(user_id=input_event_id)
        event.delete()
        return render_to_response('views/event_deleted.html', {'event_id': input_event_id})
    except ActivistEvent.DoesNotExist:
        raise Http404
    return render_to_response('views/event_deleted_failed.html', {'event_id': input_event_id})

def activist_event(input_event_id):
    try:
        event = ActivistEvent.objects.get(user_id=input_event_id)
    except ActivistEvent.DoesNotExist:
        raise Http404
    return render_to_response('views/event.html', {'event': event})

def activist_event_group(input_event_id):
    try:
        event = ActivistEvent.objects.get(user_id=input_event_id)
        group = event.group
    except ActivistEvent.DoesNotExist:
        raise Http404
    return render_to_response('views/group.html', {'group': group})

def activist_interest(input_interest_id):
    try:
        interest = ActivistInterest.objects.get(user_id=input_interest_id)
    except ActivistInterest.DoesNotExist:
        raise Http404
    return render_to_response('views/interest.html', {'interest': interest})

def activist_interest_profiles(input_interest_id):
    try:
        interest = ActivistInterest.objects.get(user_id=input_interest_id)
        profiles = interest.profiles.all()
    except ActivistInterest.DoesNotExist:
        raise Http404
    return render_to_response('views/interest_profiles.html', {'profiles': profiles})
