from django.http import HttpResponse
from schoolFinder import models
from django.shortcuts import render

# Create your views here.
#from schoolFinder.models import MajorDegree, School


def index(request):

    return HttpResponse("Success")



