# Generated by Django 2.2.6 on 2020-05-20 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200520_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz_section',
            name='quiz_type',
        ),
    ]