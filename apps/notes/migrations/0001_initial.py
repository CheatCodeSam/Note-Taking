# Generated by Django 4.0.4 on 2022-04-16 21:38

import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=16, max_length=40, prefix='', primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=30)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
