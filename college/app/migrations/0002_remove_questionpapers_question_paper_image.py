# Generated by Django 3.0.2 on 2021-02-22 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionpapers',
            name='question_paper_image',
        ),
    ]
