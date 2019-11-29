# Generated by Django 2.2.7 on 2019-11-29 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_fields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LandBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('land_area', models.FloatField()),
                ('sharing_term', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(null=True, verbose_name='Date published')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_landboard.landboard_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='SharingBoard',
            fields=[
                ('landboard_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='landBoard.LandBoard')),
                ('land_img', django_fields.fields.DefaultStaticImageField(blank=True, upload_to='land_img/')),
                ('is_free', models.BooleanField(default=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('choice_land', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Land')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_sb', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('landBoard.landboard',),
        ),
        migrations.CreateModel(
            name='SB_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField()),
                ('comment_writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sbcomment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landBoard.SharingBoard')),
            ],
        ),
        migrations.CreateModel(
            name='RequestBoard',
            fields=[
                ('landboard_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='landBoard.LandBoard')),
                ('purpose', models.CharField(max_length=100)),
                ('is_pay_for', models.BooleanField(default=False)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_rb', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('landBoard.landboard',),
        ),
        migrations.CreateModel(
            name='RB_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField()),
                ('comment_writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('land_writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Land')),
                ('rbcomment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landBoard.RequestBoard')),
            ],
        ),
        migrations.CreateModel(
            name='Land_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('is_completed', models.BooleanField(default=False)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='land_client', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='land_owner', to=settings.AUTH_USER_MODEL)),
                ('land', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='landBoard.SharingBoard')),
            ],
        ),
    ]
