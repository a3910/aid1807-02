# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 13:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20171107_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20, verbose_name='用户名')),
                ('address', models.CharField(max_length=200, verbose_name='地址')),
                ('post', models.IntegerField()),
                ('cellphone', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo')),
            ],
        ),
    ]
