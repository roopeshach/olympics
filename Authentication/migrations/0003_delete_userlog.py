# Generated by Django 4.1.1 on 2022-09-26 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0002_otp'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserLog',
        ),
    ]
