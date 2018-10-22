from django.shortcuts import render
from django.http import HttpResponse


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
    s=''
    
    for event in allEvents:
        s+=event.event_name
        s+=', '
    
    return HttpResponse('%s'%(s))
