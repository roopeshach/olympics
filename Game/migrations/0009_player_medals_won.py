# Generated by Django 4.1.1 on 2022-09-27 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='medals_won',
            field=models.CharField(blank=True, default=0, max_length=4),
        ),
    ]
