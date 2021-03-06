# Generated by Django 2.2 on 2020-01-02 17:10

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
            name='Farmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('address', models.TextField()),
                ('mid', models.CharField(default='iSSLla27754627519933', max_length=100)),
                ('mkey', models.CharField(default='2tvvg2qwvazCh5tD', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('address', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
