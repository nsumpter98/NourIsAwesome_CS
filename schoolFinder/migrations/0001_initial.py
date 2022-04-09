# Generated by Django 4.0.3 on 2022-04-09 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=200)),
                ('number_applicants', models.CharField(max_length=200)),
                ('percent_applicants_admitted', models.CharField(max_length=200)),
                ('act_75', models.CharField(max_length=200)),
                ('act_25', models.CharField(max_length=200)),
                ('graduation_rate', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MajorDegree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(max_length=200)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolFinder.school')),
            ],
        ),
    ]
