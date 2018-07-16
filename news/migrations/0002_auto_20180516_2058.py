# Generated by Django 2.0.3 on 2018-05-16 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='view_times',
            new_name='love_times',
        ),
        migrations.AddField(
            model_name='news',
            name='bad_times',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='good_times',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
