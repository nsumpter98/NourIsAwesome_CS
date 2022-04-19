from django.db import models


class School(models.Model):  # Id: 1, 2, 3
    institution_name = models.CharField(max_length=200)
    number_applicants = models.CharField(max_length=200)
    percent_applicants_admitted = models.CharField(max_length=200)
    act_75 = models.CharField(max_length=200)
    act_25 = models.CharField(max_length=200)
    graduation_rate = models.CharField(max_length=200)

    def __str__(self):
        return self.institution_name


class Degree(models.Model):
    major = models.CharField(max_length=200)
    description = models.CharField(max_length=200)  # Id (school): 1, 2, 3

    def __str__(self):
        return self.major


class TopDegreesBySchool(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)

    def __str__(self):
        return "Degree - " + self.degree.major + " - School - " + self.school.institution_name

# Create your models here.
