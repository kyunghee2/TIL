# Generated by Django 2.2.6 on 2019-11-15 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20191115_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]