from django.http import HttpResponse
from schoolFinder import models
from django.shortcuts import render

# Create your views here.
from schoolFinder.models import MajorDegree, School


def index(request):
    sc = School(institution_name="test",
                number_applicants="12",
                percent_applicants_admitted="123",
                act_75="0",
                act_25="0",
                graduation_rate="0.023")
    sc.save()

    a = MajorDegree(major="test school 123",
                    school=sc)
    a.save()
    return HttpResponse("Success")



