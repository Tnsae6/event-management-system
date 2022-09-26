from django.shortcuts import render

from .models import Event, Venue, Logo, Speaker, Sponsor, Galary, Summary
from Front_end.forms import RegisterForm
from django.urls import reverse
from .forms import RegisterForm
# Create your views here.
def home(request):
    slider = Event.objects.all()
    location = Venue.objects.all()
    logox = Logo.objects.all()
    sponsor = Sponsor.objects.all()
    galary = Galary.objects.all()
    summary = Summary.objects.all()
    context = {
        'slider':slider,
        'location':location,
        'logox':logox,
        'sponsor':sponsor,
        'galary':galary,
        'summary':summary,
    }
    return render(request,'index.html', context)

def register(request, slug_text):
    q = Event.objects.filter(slug = slug_text)
    if q.exists():
        q = q.first()
    else:
        return HttpResponse("<h1>page Not Found</h1>")
    form = RegisterForm(request.POST or None)
    speaker = Speaker.objects.all()
    context = {
        'speaker':speaker,
        'events':q,
    }
    if (form.is_valid()):
        form.save()

    return render(request,'register.html', context)

def comingsoon(request):
    return render(request,'comingsoon.html',)