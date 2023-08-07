from django.shortcuts import render
from app1.models import *


# Create your views here.
def displaytopics(request):
    topics=Topic.objects.all()
    LT=Topic.objects.filter(Topic_name='rose')
    d={'topics':topics}
    return render (request,'displaytopics.html',d)

