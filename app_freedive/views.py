from django.shortcuts import render, redirect
from .models import Events, Event_Chat, Participants
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

from .forms import Send_Message, Event_Image


def participate_chat(request, side, room_id):
    form = Send_Message
    if request.user.is_anonymous:
        return redirect('user:login')
    room = Events.objects.get(id=room_id)
    if side != 'check':
        chat_room = Event_Chat()
        chat_room.chat_room = room
        chat_room.sender = request.user.username
        chat_room.sender_image = request.user.email

        if side == 'join':
            chat_room.message = request.user.username + ' has joined the room'
            chat_room.save()
            return redirect('freedive:participate_chat', side='check', room_id=room_id)

        elif side == 'leave':
            chat_room.message = request.user.username + ' has left the room'
            chat_room.save()
            return redirect('freedive:participate_chat', side='check', room_id=room_id)

    elif side == 'check':
        chats = Event_Chat.objects.filter(
            chat_room=room_id).order_by('timestamp').reverse()

        return render(request, 'application/freedive/socials.html', {
            'chats': chats,
            'form': form,
            'event': room
        })


def join(request, room_id):
    if request.user.is_anonymous:
        return redirect('user:login')
    try:
        old_participant = Participants.objects.get(
            participant=request.user.username)
        room = Events.objects.get(id=room_id)
        room.event_participants.remove(
            old_participant)
        old_participant.delete()
        participate_chat(request, 'leave', room_id)
        return redirect('freedive:home')
        # return home(request)
    except:

        new_participant = Participants()
        new_participant.participant = request.user.username
        new_participant.participant_image = request.user.email
        new_participant.save()
        # add to event room
        room = Events.objects.get(id=room_id)
        room.event_participants.add(
            new_participant)
        participate_chat(request, 'join', room_id)
        return participate_chat(request, 'check', room_id)
        # return room(request, room_id)
    print('return')


def send(request, room_id):
    if request.user.is_anonymous:
        return redirect('user:login')
    if request.method == 'POST':

        form = Send_Message(request.POST)
        event = Events.objects.get(id=room_id)
        if form.is_valid():
            message = form.cleaned_data['message']
            new_chat = Event_Chat()
            new_chat.chat_room = event
            new_chat.sender = request.user.username
            new_chat.sender_image = request.user.email

            new_chat.message = message
            new_chat.save()
            return redirect('freedive:participate_chat', side='check', room_id=room_id)
            # return participate_chat(request, 'check', room_id)
            # return room(request, room_id)
        else:
            return redirect('freedive:participate_chat')

            # return redirect('freedive:send', side='check', room_id=room_id)

            # return participate_chat(request, 'check', room_id)
            # return render(request, 'applications/freedive/socials.html', {
            #     'chats': Event_Chat.objects.filter(room_id=room_id).order_by('id').all(),
            #     'form': form
            # })


def room(request, room_id):
    chats = Event_Chat.objects.get(chat_room=room_id).order_by('id').all()
    return render(request, 'application/freedive/socials.html', {
        'chats': chats
    })


def index(request):
    return render(request, 'application/freedive/index.html')


def home(request):
    # from datetime import datetime
    # from django_user_agents.utils import get_user_agent

    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # if x_forwarded_for:
    #     ip = x_forwarded_for.split(',')[0]
    # else:
    #     ip = request.META.get('REMOTE_ADDR')
    # now = datetime.now()
    # x = request.user_agent.device
    # y = request.META['HTTP_USER_AGENT']
    # print('-------------------\n')
    # print(now)
    # print(x.brand)
    # print(y)
    # print(ip)
    # print('\n-----------------\n')

    return render(request, 'application/freedive/home.html', {
        'events': Events.objects.order_by('-start_time').reverse()
    })


def events(request):
    if request.user.is_anonymous:
        return redirect('user:login')
    if request.method == 'POST':
        form = Event_Image(request.POST, request.FILES)

        print('check if valid', form.is_valid())
        if form.is_valid():
            print('valid')
            form.save()
            img_obj = form.instance
            return render(request, 'application/freedive/events.html', {'img_obj': img_obj})
    print('goes')
    form = Event_Image()
    return render(request, 'application/freedive/events.html', {'form': form})


def add_event(request):
    import datetime
    if request.method == 'POST':

        start_time = request.POST.get(
            'start-time')
        start_time = datetime.datetime.strptime(
            start_time, '%Y-%m-%dT%H:%M').strftime("%d %B %A, at %I:%M %p -- %Y")

        end_time = request.POST.get(
            'end-time')
        end_time = datetime.datetime.strptime(
            end_time, '%Y-%m-%dT%H:%M').strftime("%A, %B %d at %I:%M %p -- %Y")

        organizer = request.user.username
        organizer_image = request.user.email
        organizer_contact = request.POST.get('contact')

        event_type = request.POST.get('event-type')
        event_name = request.POST.get('event-name')
        event_description = request.POST.get('event-description')
        event_image = request.POST.get('event-image')
        event_cost = request.POST.get('event-cost')

        new_event = Events()

        new_event.start_time = start_time
        new_event.end_time = end_time

        new_event.organizer = organizer
        new_event.organizer_image = organizer_image
        new_event.organizer_contact = organizer_contact
        new_event.event_cost = event_cost

        new_event.event_type = event_type
        new_event.event_description = event_description
        new_event.event_name = event_name
        new_event.event_image = event_image

        new_event.save()

        # create participant
        participant = Participants()
        participant.participant = organizer
        participant.save()
        new_event.event_participants.add()
        # ------
        # create chat room
        chat_room = Event_Chat()
        chat_room.chat_room = new_event
        chat_room.message = request.user.username + ' has created the room'
        chat_room.sender = request.user.username
        chat_room.sender_image = request.user.email
        chat_room.save()

        print('NEW EVENT SAVED !!!')
        print(start_time)
        print(end_time)
        print(organizer)
        print(event_type)
        print(event_name)
        print(event_description)
        return redirect('freedive:home')

    return redirect('freedive:events')
    # return render(request, 'application/freedive/events.html')


def socials(request):
    return render(request, 'application/freedive/socials.html', {
        'form': form
    })


def community(request):
    return render(request, 'application/freedive/community.html')
