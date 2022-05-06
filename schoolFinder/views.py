from django.http import HttpResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from schoolFinder.models import *


# Create your views here.

def index(request):
    numSchools = School.objects.count()
    total = 0

    for gr in School.objects.values_list('graduation_rate'):
        total += gr[0]

    context = {
        "schoolCount": str(numSchools),
        "schools": School.objects.order_by('-number_applicants')[:6],
        "average_gr": round((total / numSchools) * 100),
        "top_school_by_gr" : School.objects
                                .filter(graduation_rate__gt=.01)
                                    .filter(percent_applicants_admitted__gt=0.35)
                                 .order_by('percent_applicants_admitted')[:4]

    }

    print(context['top_school_by_gr'])

    return render(request, "dashboard/pages/dashboard.html", context)
