from django.http import HttpResponse
from schoolFinder import models
from django.shortcuts import render
import pandas as pd
import requests
import io
# Create your views here.
from schoolFinder.models import *

url = "https://raw.githubusercontent.com/nsumpter98/NourIsAwesome_CS/master/CSVFiles/schools.csv"
download = requests.get(url).content

df = pd.read_csv(io.StringIO(download.decode('utf-8')))


def index(request):
    return HttpResponse("<a href=\"/dbUpdater/update\">Update Database</a>")


def update_db(request):
    for i, row in df.iterrows():
        print(row[0])
        sc = School(institution_name=row[0],
                    number_applicants=int(row[1]) if row[1] != "-" else 0,
                    percent_applicants_admitted=float(row[2]) if row[2] != "-" else 0,
                    act_75=row[3],
                    act_25=row[4],
                    graduation_rate=float(row[5]) if row[5] != "-" else 0)
        sc.save()

    for row in School.objects.all().reverse():

        # row.delete()

        if School.objects.filter(institution_name=row.institution_name,
                                 number_applicants=row.number_applicants,
                                 percent_applicants_admitted=row.percent_applicants_admitted,
                                 act_75=row.act_75,
                                 act_25=row.act_25,
                                 graduation_rate=row.graduation_rate).count() > 1:
            print("Deleting - " + row.institution_name)
            row.delete()
        else:
            print("Ok - " + row.institution_name)

    """a = Degree(major="test school 123",
                    school=sc)
    a.save()"""
    return HttpResponse("DB Update - Success");
