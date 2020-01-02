# Generated by Django 2.2 on 2020-01-02 17:10

import cart.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=60)),
                ('price', models.FloatField()),
                ('image', models.FileField(upload_to='user/items/')),
                ('quantity', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.Cart')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Farmer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=60)),
                ('price', models.FloatField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('location', models.CharField(default='', max_length=1000)),
                ('received', models.BooleanField(default=False)),
                ('e', models.CharField(default=cart.models.f, max_length=18)),
                ('farmer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Farmer')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.CartItem')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]