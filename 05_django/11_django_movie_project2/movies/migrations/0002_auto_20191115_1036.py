# Generated by Django 2.2.6 on 2019-11-15 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={'ordering': ['-pk']},
        ),
    ]
