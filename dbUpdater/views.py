from django.http import HttpResponse
from schoolFinder import models
from django.shortcuts import render
import pandas as pd
import requests
import io

url = "https://raw.githubusercontent.com/nsumpter98/NourIsAwesome_CS/master/CSVFiles/schools.csv"
download = requests.get(url).content

df = pd.read_csv(io.StringIO(download.decode('utf-8')))



# Create your views here.
from schoolFinder.models import Degree, School


def index(request):
    for i, row in df.iterrows():
        print(row[0])
        sc = School(institution_name=row[0],
                    number_applicants=row[1],
                    percent_applicants_admitted=row[2],
                    act_75=row[3],
                    act_25=row[4],
                    graduation_rate=row[5])
        sc.save()


    """a = Degree(major="test school 123",
                    school=sc)
    a.save()"""
    return HttpResponse("DB Update - Success");



