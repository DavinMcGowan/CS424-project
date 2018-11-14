from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse

from django.contrib.auth.decorators import login_required

from IPython import embed

from events.forms import EventForm

from events.models import Event


def event(request,event_id):
    event = Event.objects.get(id=event_id)
    
#     return HttpResponse('%s'%(event.event_name))
    response = render(request,'events/event_detail.html',{
       'event':event
       })
    return response

def event_list(request):
    allEvents = Event.objects.all()
    
    response=render(request,'events/event_list.html',{
            'eventlist':allEvents
    })
    return response

@login_required
def event_update(request,event_id):
    #embed()
    #was in sample but caused crash
    event = Event.objects.get(id=event_id)
    if event.owner == request.user:
        if request.method=="POST":
            form = EventForm(request.POST, instance=event)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('event_profile',kwargs={'event_id':event_id}))
            else:
                return HttpResponseRedirect('/')
    else:
        return HttpResponse('You are not the owner of this event')
        
    form = EventForm(instance=event)
    return render(request,'events/event_update.html',{
            'form':form
        })
