# Generated by Django 2.2.7 on 2019-11-23 11:42

from django.db import migrations
import django_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191122_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_img',
            field=django_fields.fields.DefaultStaticImageField(blank=True, upload_to='profile_img/'),
        ),
    ]