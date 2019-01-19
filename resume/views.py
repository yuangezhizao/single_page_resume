from django.shortcuts import render
from django.http import HttpResponseRedirect
import datetime
from . import models


# Create your views here.

def homepage(request):
    return render(request, 'resume/homepage.html')


def index(request):
    messages = models.Message.objects.all()
    user = models.User.objects.all()[0]
    return render(request, 'resume/index.html', {'messages': messages, 'user':user})


def save_message(request):
    try:
        username = request.POST.get("username")
        content = request.POST.get("content")
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = models.Message(username=username, content=content, time=time)
        message.save()
    except Exception as e:
        print(e)
    return HttpResponseRedirect('/resume/')
