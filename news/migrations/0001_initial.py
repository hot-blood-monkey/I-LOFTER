# Generated by Django 2.0.3 on 2018-05-15 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(default='news', max_length=100)),
                ('image', models.ImageField(default=None, upload_to='image/%Y/%m/%d')),
                ('image_url', models.URLField(default=None)),
                ('content', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('view_times', models.PositiveIntegerField(default=1)),
                ('tag', models.CharField(blank=True, choices=[('tech', 'Tech'), ('life', 'Life'), ('music', 'Music'), ('idol', 'Idol')], max_length=5, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]