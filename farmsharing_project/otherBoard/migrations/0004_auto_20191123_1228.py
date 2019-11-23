# Generated by Django 2.2.7 on 2019-11-23 12:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('otherBoard', '0003_auto_20191123_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='scrap',
        ),
        migrations.AddField(
            model_name='join',
            name='scrap',
            field=models.ManyToManyField(blank=True, related_name='Profile_scrap', to=settings.AUTH_USER_MODEL),
        ),
    ]