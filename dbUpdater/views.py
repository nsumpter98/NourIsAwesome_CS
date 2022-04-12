from django.http import HttpResponse
from schoolFinder import models
from django.shortcuts import render

# Create your views here.
from schoolFinder.models import MajorDegree, School


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def updateDB(request):
    a = MajorDegree(major="test school 123",
                    school=School(institution_name="test",
                                  number_applicants="12",
                                  percent_applicants_admitted="123",
                                  act_75="0",
                                  act_25="0",
                                  graduation_rate="0.023"))
    a.save()

    return HttpResponse("Hello, world. You're at the polls index.")
