# Generated by Django 3.0.2 on 2021-02-24 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_questionpapers_semester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionpapers',
            name='year_of_subject',
        ),
        migrations.AddField(
            model_name='questionpapers',
            name='year',
            field=models.CharField(default='2018', max_length=200),
        ),
    ]
