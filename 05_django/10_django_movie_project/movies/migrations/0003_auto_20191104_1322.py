# Generated by Django 2.2.6 on 2019-11-04 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20191101_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='open_date',
            field=models.TextField(),
        ),
    ]
